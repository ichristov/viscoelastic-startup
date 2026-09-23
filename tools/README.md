# Digitizing the figures of Balan (2023)

The notebook [`balan_2023_startup_couette`](../notebooks/balan_2023_startup_couette.ipynb) compares the exact
solutions with values read off the published figures of C. Balan, [Note on the start-up of Couette flow for
viscoelastic fluids](https://doi.org/10.1063/5.0173510), _Phys. Fluids_ **35** (2023) 113108. Those values are
listed in the notebook cells that use them, and these two scripts are how they were obtained, so that anyone
can check them rather than take them on trust.

**The article's PDF is not redistributed here**, because it is copyrighted. Download it from the DOI above and
pass its path to either script:

```bash
python3 tools/digitize_balan_fig4a.py path/to/Balan-Phys.Fluids.35.pdf
python3 tools/digitize_balan_fig3a_fig2.py path/to/Balan-Phys.Fluids.35.pdf
```

Both need [pdftoppm](https://poppler.freedesktop.org) (poppler), [Pillow](https://python-pillow.org) and
[SciPy](https://scipy.org); the second also needs [mpmath](https://mpmath.org). They render the page at 600 dpi,
calibrate the axes on the centers of the tick labels, and read each curve as the mean row of its pixels in a
narrow column, keeping only the columns where the curve is unambiguous: not crossed by an annotation, not merged
with a neighboring curve, and of the right color.

- `digitize_balan_fig4a.py` reads $v(x^\star = 95, t)$ from the first two panels of Fig. 4(a), that is
  $\kappa = 1$ and $0.4$ from the first and $\kappa = 0.2$ from the second, and writes
  [`balan_fig4a_digitized.csv`](balan_fig4a_digitized.csv). Each panel is calibrated separately, because the
  three panels of Fig. 4(a) were pasted at slightly different scales (2 per cent in $v$, 7 per cent in $t$).
- `digitize_balan_fig3a_fig2.py` reads $v(\xi, t)$ from the velocity panel of Fig. 3(a) at the six distances
  from the plate, $\sigma(\xi, t)$ from its shear-stress panel, and the Newtonian velocity profiles of
  Fig. 2, and compares all three with the exact solutions. The 35 stress values it recovers differ from the
  exact ramped plate by a median of $3\times10^{-4}$ and from the consistent start-up by up to 0.036.

What the readings show is in the notebook: the values of Fig. 3(a) and of the $\kappa = 0.4$ panel of Fig. 4(a)
follow the exact ramped-plate solution rather than the start-up solution, while the $\kappa = 0.2$ panel of
Fig. 4(a) repeats the $\kappa = 0.4$ curve.

Reading a printed curve is not exact. The calibration residuals are about $10^{-4}$ in $v$, and the readings
themselves are good to a few times $10^{-4}$, which the notebook's comparisons take into account.
