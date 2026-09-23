#!/usr/bin/env python3
"""Digitize Fig. 3(a) (velocity panel) and the Newtonian velocity inset of Fig. 2 of Balan (2023), and compare with
the exact start-up (Tanner, erfc) and the exact ramped plate, by de Hoog's inversion.

Fig. 3(a): v(xi, t) at xi = 0.5, 1, 2, 3.5, 5, 8, kappa = 0.2, Re = 1, read at integer t = 1..9. Calibrated on the tick
labels; a curve is identified by the color of its darkest pixels (violet, blue-violet, pink, black, blue, red) and
kept only where its pixel cluster is thin (not merged with another curve), matches a curve color, is not within 15 px
of the annotation circle, and v > 0.01.
Fig. 2 (left, inset): Newtonian v(x, t) for 90 < x <= 100; the curves are matched by value, not color (the colors
repeat), against erfc(xi/(2 sqrt t)) and the Newtonian ramped plate at t = 10, 8, 7, 5, 2, 1, 0.5, 0.2.
The article's PDF is copyrighted and is not redistributed with this repository. Download it from
https://doi.org/10.1063/5.0173510 and pass its path:

    python3 tools/digitize_balan_fig3a_fig2.py path/to/Balan-Phys.Fluids.35.pdf

Needs pdftoppm (poppler), Pillow, SciPy and mpmath. Writes tools/balan_fig3a_digitized.csv.
"""
import subprocess
import sys
import tempfile
import numpy as np
import mpmath as mp
from PIL import Image
from scipy import ndimage
from scipy.special import erfc

PDF = sys.argv[1] if len(sys.argv) > 1 else 'Balan-Phys.Fluids.35.pdf'
OUT = 'tools/balan_fig3a_digitized.csv'
tmp = tempfile.mkdtemp()


def page(n):
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '600', '-png', PDF, f'{tmp}/p'], check=True)
    return Image.open(f'{tmp}/p-{n:02d}.png').convert('RGB')


def clusters(image, col, top, bottom):
    """Row, height and darkest color of each non-white run of pixels in a 3-pixel column."""
    band = image[top:bottom, col-1:col+2]
    runs, count = ndimage.label((band.sum(2) < 600).any(1))
    out = []
    for i in range(1, count+1):
        rows = np.nonzero(runs == i)[0]
        pixels = band[rows].reshape(-1, 3)
        pixels = pixels[pixels.sum(1) < 600]
        darkest = pixels[np.argsort(pixels.sum(1))[:3]].mean(0)
        out.append((rows.mean() + top, rows.max() - rows.min(), darkest))
    return out


# ---------------------------------------------------------------- Fig. 3(a), velocity panel, page 4
fig3a = np.asarray(page(4).crop((736, 2400, 2481, 3560))).astype(float)
t_slope, t_intercept = 0.0063713511252823, -0.8606708917039847      # tick labels 2, 4, ..., 10 (max residual 0.015)
v_slope, v_intercept = -0.001032522871287789, 0.9850276187874389    # tick labels 0.2, ..., 0.8 (max residual 4e-4)
colors = {0.5: (131, 24, 254), 1.0: (90, 25, 254), 2.0: (252, 24, 131), 3.5: (20, 20, 20), 5.0: (24, 24, 252),
          8.0: (250, 30, 68), 'extra': (210, 40, 40), 'circle': (95, 110, 133)}
mp.mp.dps = 20


def exact(xi, t, kappa, ramp):
    F = lambda s: mp.exp(-xi*mp.sqrt(s*(1 + s)/(1 + kappa*s)))/s/((1 + kappa*s) if ramp else 1)
    return float(mp.invertlaplace(F, t, method='dehoog'))


print('FIG. 3(a) OF BALAN (2023), kappa = 0.2: read, ramped plate, start-up')
rows = []
for t in range(1, 10):
    found = []
    for r, h, c in clusters(fig3a, int(round((t - t_intercept)/t_slope)), 40, 960):
        d = {k: np.linalg.norm(c - np.array(v)) for k, v in colors.items()}
        k = min(d, key=d.get)
        found.append((r, h, k, d[k]))
    bad = [r for r, h, k, dk in found if k == 'circle' or dk > 60 or h > 20]
    seen = {}
    for r, h, k, dk in found:
        if k in ('circle', 'extra') or dk > 60 or h > 20 or any(abs(r - b) <= 15 for b in bad if b != r):
            continue
        seen[k] = None if k in seen else v_slope*r + v_intercept
    for xi, v in sorted(seen.items()):
        if v is not None and v > 0.01:
            rows.append((xi, t, v, exact(xi, t, 0.2, True), exact(xi, t, 0.2, False)))
rows.sort()
for xi, t, v, ramp, step in rows:
    print(f'  xi = {xi:3}, t = {t}: {v:.4f}  {ramp:.4f} ({v - ramp:+.4f})  {step:.4f} ({v - step:+.4f})')
diff = np.array([[r[2] - r[3], r[2] - r[4]] for r in rows])
print(f'  {len(rows)} values; max|read - ramp| = {np.abs(diff[:, 0]).max():.4f}, median {np.median(np.abs(diff[:, 0])):.4f}; '
      f'read - start-up from {diff[:, 1].min():.4f} to {diff[:, 1].max():.4f}')
csv = [f'v,{xi:g},{t:g},{value:.4f}' for xi, t, value, ramp, step in rows]

# ---------------------------------------------------------------- Fig. 3(a), shear-stress panel, page 4
# the right half of the same figure, same six distances and the same colors; no annotation circle here
fig3a_sigma = np.asarray(page(4).crop((2600, 2350, 4400, 3450))).astype(float)
ts_slope, ts_intercept = 0.00636622050772, -0.581398760882          # tick labels 2, 4, ..., 10 (max residual 0.019)
ss_slope, ss_intercept = -0.000644527436555, 0.646755760866         # tick labels 0.1, ..., 0.5 (max residual 1e-3)


def exact_sigma(xi, t, kappa, ramp):
    """sigma at a distance xi from the plate: the inverse of [(1 + kappa s)/(1 + s)] k exp(-k xi)/s, Re = 1."""
    def F(s):
        k = mp.sqrt(s*(1 + s)/(1 + kappa*s))
        value = (1 + kappa*s)/(1 + s)*k*mp.exp(-k*xi)/s
        return value/(1 + kappa*s) if ramp else value
    return float(mp.invertlaplace(F, t, method='dehoog'))


print('\nFIG. 3(a) OF BALAN (2023), SHEAR STRESS, kappa = 0.2: read, ramped plate, start-up')
rows = []
for t in range(1, 10):
    seen = {}
    for r, h, c in clusters(fig3a_sigma, int(round((t - ts_intercept)/ts_slope)), 40, 1000):
        d = {k: np.linalg.norm(c - np.array(v)) for k, v in colors.items() if k not in ('extra', 'circle')}
        k = min(d, key=d.get)
        if d[k] > 70 or h > 25:          # an ambiguous color, or two curves merged into one cluster
            continue
        seen[k] = None if k in seen else ss_slope*r + ss_intercept
    for xi, sigma in sorted(seen.items()):
        if sigma is not None and sigma > 0.01:
            rows.append((xi, t, sigma, exact_sigma(xi, t, 0.2, True), exact_sigma(xi, t, 0.2, False)))
rows.sort()
for xi, t, sigma, ramp, step in rows:
    print(f'  xi = {xi:3}, t = {t}: {sigma:.4f}  {ramp:.4f} ({sigma - ramp:+.4f})  {step:.4f} ({sigma - step:+.4f})')
diff = np.array([[r[2] - r[3], r[2] - r[4]] for r in rows])
print(f'  {len(rows)} values; max|read - ramp| = {np.abs(diff[:, 0]).max():.4f}, '
      f'median {np.median(np.abs(diff[:, 0])):.4f}; '
      f'|read - start-up| up to {np.abs(diff[:, 1]).max():.4f}')
csv = csv + [f'sigma,{xi:g},{t:g},{value:.4f}' for xi, t, value, ramp, step in rows]
open(OUT, 'w').write('\n'.join(
    ['quantity,xi,t,value',                          # the header first, for numpy.genfromtxt(names=True)
     '# Fig. 3(a) of Balan (2023), Phys. Fluids 35, 113108: Oldroyd-B (a = 1), kappa = 0.2, Re = 1',
     '# v and sigma at the distance xi from the moving plate, that is at x = 100 - xi in his coordinate;',
     '# then v_newtonian from Fig. 2, where the column is his x itself, matched to a curve by value;',
     '# page 4 rendered at 600 dpi by pdftoppm, the velocity panel cropped to (736, 2400, 2481, 3560) and the',
     '# shear-stress panel to (2600, 2350, 4400, 3450), each calibrated on its own tick labels',
     '# a reading is kept only where its curve is unambiguous: of a known color, thin enough not to be two',
     '# merged curves, and clear of the annotation circle'] + csv) + '\n')
print(f'wrote {OUT}')

# ---------------------------------------------------------------- Fig. 2, Newtonian velocity inset, page 3
s = 600/110
fig2 = np.asarray(page(3).crop((int(95*s), int(770*s), int(470*s), int(1030*s)))).astype(float)
v_slope2, v_intercept2 = np.polyfit([55.5, 225.5, 394, 563, 732.5], [1.0, 0.8, 0.6, 0.4, 0.2], 1)
x_slope2, x_intercept2 = np.polyfit([525, 791.5, 1058, 1325, 1592.5], [92, 94, 96, 98, 100.0], 1)
fig2_rows = []
print('\nFIG. 2 OF BALAN (2023), NEWTONIAN VELOCITY: nearest read value versus erfc and versus the ramped plate')
print('     t   matched to erfc (within 0.006)   median|read - erfc|   median|read - ramp|')
for t in [10, 8, 7, 5, 2, 1, 0.5, 0.2]:
    to_step, to_ramp = [], []
    for x in np.arange(91, 99.6, 0.5):
        xi = 100 - x
        step = erfc(xi/(2*np.sqrt(t)))
        if step < 0.02 or step > 0.97:
            continue
        read = np.array([v_slope2*r + v_intercept2 for r, h, c in clusters(fig2, int(round((x - x_intercept2)/x_slope2)), 80, 900) if h <= 16])
        if len(read) == 0:
            continue
        to_step.append(np.abs(read - step).min())
        to_ramp.append(np.abs(read - exact(xi, t, 1.0, True)).min())
        fig2_rows.append(f'v_newtonian,{x:g},{t:g},{read[np.argmin(np.abs(read - step))]:.4f}')
    to_step, to_ramp = np.array(to_step), np.array(to_ramp)
    print(f'  {t:4}   {(to_step < 0.006).sum():2d}/{len(to_step):2d}   {np.median(to_step):.4f}   {np.median(to_ramp):.4f}')

open(OUT, 'a').write('\n'.join(fig2_rows) + '\n')
print(f'appended {len(fig2_rows)} Fig. 2 readings to {OUT}')
