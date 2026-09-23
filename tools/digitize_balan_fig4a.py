#!/usr/bin/env python3
"""Digitize Fig. 4(a) of Balan (2023), Phys. Fluids 35, 113108: v(x* = 95, t) for a = 1, Re = 1.

Fig. 4(a) is three stacked panels sharing their axes. The first shows kappa = 1 (black, Newtonian) and
kappa = 0.4 (red), the second kappa = 0.2 (red), the third kappa = 0.0001; only the first two are read
here. Each panel is calibrated on its own tick labels, because the three were pasted at slightly
different scales (the pixels per unit differ by 2 per cent in v and 7 per cent in t).

A curve is read at t = 3, 3.5, ..., 10 as the mean row of its pixels in a 3-pixel-wide column, and only
where that column is clean: no blue annotation (the t_c markers, the tangent line, the arrows) nearby,
and exactly one cluster of the curve's color, since the black annotation text is the color of the
Newtonian curve.

The article's PDF is copyrighted and is not redistributed with this repository. Download it from
https://doi.org/10.1063/5.0173510 and pass its path:

    python3 tools/digitize_balan_fig4a.py path/to/Balan-Phys.Fluids.35.pdf

Needs pdftoppm (poppler), Pillow and SciPy. Writes tools/balan_fig4a_digitized.csv.
"""
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from scipy import ndimage

PDF = sys.argv[1] if len(sys.argv) > 1 else 'Balan-Phys.Fluids.35.pdf'
OUT = 'tools/balan_fig4a_digitized.csv'
TIMES = np.arange(3, 10.01, 0.5)

# the two panels read here, on page 5 of the PDF (the page numbered 113108-4), rendered at 600 dpi:
# crop, the row below which the y tick labels sit, the row band of the x tick labels, the rows holding
# the curves, and the color of each curve
PANELS = [
    {'crop': (520, 2080, 2700, 3340), 'y_below': 1260, 'x_band': (1140, 1200), 'curve': (60, 1140),
     'curves': [(1.0, 'black'), (0.4, 'red')]},
    {'crop': (520, 3271, 2700, 4531), 'y_below': 900, 'x_band': (1040, 1100), 'curve': (40, 1020),
     'curves': [(0.2, 'red')]},
]


def label_boxes(boxes, key, gap):
    """Merge glyph bounding boxes (row0, row1, col0, col1) that are closer than gap along key into labels."""
    boxes = sorted(boxes, key=key)
    labels = []
    for b in boxes:
        if labels and key(b) - key(labels[-1][-1]) < gap:
            labels[-1].append(b)
        else:
            labels.append([b])
    return [(min(b[0] for b in g), max(b[1] for b in g), min(b[2] for b in g), max(b[3] for b in g)) for g in labels]


def read_panel(page, panel):
    """Digitize one panel: returns (kappa, t, v) rows and the calibration, as text."""
    pixels = np.asarray(page.crop(panel['crop'])).astype(int)
    R, G, B = pixels[..., 0], pixels[..., 1], pixels[..., 2]

    # glyphs of the tick labels
    dark = (R < 120) & (G < 120) & (B < 120)
    glyphs, count = ndimage.label(dark)
    boxes = [(sl[0].start, sl[0].stop, sl[1].start, sl[1].stop) for sl in ndimage.find_objects(glyphs)]
    boxes = [b for b in boxes if 10 < b[1] - b[0] < 40]
    y_labels = label_boxes([b for b in boxes if b[3] < 150 and b[0] < panel['y_below']], lambda b: b[0], 30)[:5]
    x_labels = label_boxes([b for b in boxes if panel['x_band'][0] < b[0] < panel['x_band'][1]], lambda b: b[2], 25)
    x_labels = x_labels[:4] + [(x_labels[4][0], x_labels[4][1], x_labels[4][2], x_labels[5][3])]   # "1" and "0" of 10

    y_rows = np.array([(b[0] + b[1])/2 for b in y_labels])
    x_cols = np.array([(b[2] + b[3])/2 for b in x_labels])
    v_slope, v_intercept = np.polyfit(y_rows, [0.25, 0.20, 0.15, 0.10, 0.05], 1)
    t_slope, t_intercept = np.polyfit(x_cols, [2, 4, 6, 8, 10.0], 1)
    v_residual = np.abs(v_slope*y_rows + v_intercept - [0.25, 0.20, 0.15, 0.10, 0.05]).max()
    t_residual = np.abs(t_slope*x_cols + t_intercept - [2, 4, 6, 8, 10.0]).max()

    masks = {'black': (R < 90) & (G < 90) & (B < 90), 'red': (R > 170) & (G < 100) & (B < 100)}
    blue = (B > 150) & (R < 140) & (G < 190) & (B - R > 60)
    top, bottom = panel['curve']

    rows = []
    for kappa, color in panel['curves']:
        for t in TIMES:
            col = int(round((t - t_intercept)/t_slope))
            if blue[top:bottom, col-12:col+13].any():
                continue                                  # an annotation crosses the curve here
            column = masks[color][top:bottom, col-1:col+2].any(axis=1)
            clusters, number = ndimage.label(column)
            if number != 1:
                continue                                  # no curve, or the annotation text as well
            pixel_rows = np.nonzero(column)[0] + top
            rows.append(f'{kappa:g},{t:g},{v_slope*pixel_rows.mean() + v_intercept:.4f}')
    calibration = (f'#   crop {panel["crop"]}: v = {v_slope:.6e}*row + {v_intercept:.6f} '
                   f'(max residual {v_residual:.1e}), t = {t_slope:.6e}*col + {t_intercept:.5f} '
                   f'(max residual {t_residual:.1e})')
    return rows, calibration


def main():
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-f', '5', '-l', '5', '-r', '600', '-png', PDF, tmp + '/page'], check=True)
    page = Image.open(tmp + '/page-05.png').convert('RGB')

    lines = ['kappa,t,v',                                 # the header first, for numpy.genfromtxt(names=True)
             '# Fig. 4(a) of Balan (2023), Phys. Fluids 35, 113108: v(x* = 95, t), a = 1, Re = 1',
             '# page 5 rendered at 600 dpi by pdftoppm; each panel calibrated on its own tick labels:']
    rows = []
    for panel in PANELS:
        panel_rows, calibration = read_panel(page, panel)
        lines.append(calibration)
        rows = rows + panel_rows
    lines.append('# t kept only where the column is free of the blue annotations; the curves end before t = 10')
    open(OUT, 'w').write('\n'.join(lines + rows) + '\n')
    print('\n'.join(lines + rows))


if __name__ == '__main__':
    main()
