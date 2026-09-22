# viscoelastic-startup

![Left: the velocity of a plate started impulsively, a unit step, and the ramp 1 - exp(-t/t_r) that the erroneous solutions actually describe. Right: velocity profiles of a second-grade fluid above the plate at three times, the correct solution in blue with arrows and the erroneous one as a vermillion dashed curve lagging behind it](assets/cover.png)

Verification and reproducibility of exact solutions for **start-up flows of viscoelastic fluids**: a plate, at rest for all $t<0$, starts moving at $t = 0^+$ and drags a second-grade, Oldroyd-B or Jeffreys fluid with it.

Since the early 2000s, "new exact solutions" to these problems have been published that are wrong, and a series of Comment papers by [Ivan C. Christov](https://christov.tmnt-lab.org), C. I. Christov and P. M. Jordan corrected them. **Each notebook here reproduces one of those Comments from scratch**: the corrected solution, the erroneous published solution implemented exactly as printed, an independent check of both (a numerical inversion of the Laplace transform and a finite-difference solution), and the paper's comparison figure, regenerated.

## The notebooks

| Notebook | Problem | Reproduces |
|---|---|---|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2013_oldroydb_couette.ipynb) [christov_2013_oldroydb_couette](notebooks/christov_2013_oldroydb_couette.ipynb) | Start-up of plane Couette flow, Oldroyd-B (Jeffreys) fluid: the textbook eigenfunction series versus the causal one | I. C. Christov, [On a difficulty in the formulation of initial and boundary conditions for eigenfunction expansion solutions for the start-up of fluid flow](https://doi.org/10.1016/j.mechrescom.2013.05.005), _Mech. Res. Commun._ **51** (2013) 86&ndash;92 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2009_oldroydb_porous.ipynb) [christov_jordan_2009_oldroydb_porous](notebooks/christov_jordan_2009_oldroydb_porous.ipynb) | Stokes' first problem, Oldroyd-B fluid in a porous half-space | C. I. Christov, P. M. Jordan, [Comment on &ldquo;Stokes' first problem for an Oldroyd-B fluid in a porous half space&rdquo;](https://doi.org/10.1063/1.3126503), _Phys. Fluids_ **21** (2009) 069101 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_christov_2010_second_grade.ipynb) [christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) | Stokes' first problem, second-grade fluid | I. C. Christov, C. I. Christov, [Comment on &ldquo;On a class of exact solutions of the equations of motion of a second grade fluid&rdquo;](https://doi.org/10.1007/s00707-010-0300-2), _Acta Mech._ **215** (2010) 25&ndash;28 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_second_grade.ipynb) [christov_2010_stokes1_second_grade](notebooks/christov_2010_stokes1_second_grade.ipynb) | Stokes' first problem, second-grade fluid: three correct representations | I. C. Christov, [Stokes' first problem for some non-Newtonian fluids: Results and mistakes](https://doi.org/10.1016/j.mechrescom.2010.09.006), _Mech. Res. Commun._ **37** (2010) 717&ndash;723 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_oldroydb.ipynb) [christov_2010_stokes1_oldroydb](notebooks/christov_2010_stokes1_oldroydb.ipynb) | Stokes' first problem, Oldroyd-B fluid: three correct representations | the same paper |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2012_second_grade_stokes2.ipynb) [christov_jordan_2012_second_grade_stokes2](notebooks/christov_jordan_2012_second_grade_stokes2.ipynb) | Transient Stokes' second problem (oscillating plate), second-grade fluid, half-space and strip | I. C. Christov, P. M. Jordan, [Comments on: &ldquo;Starting solutions for some unsteady unidirectional flows of a second grade fluid&rdquo;](https://doi.org/10.1016/j.ijengsci.2011.10.012), _Int. J. Eng. Sci._ **51** (2012) 326&ndash;332 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/jordan_2005_second_grade_couette.ipynb) [jordan_2005_second_grade_couette](notebooks/jordan_2005_second_grade_couette.ipynb) | Start-up of plane Couette flow, second-grade fluid | P. M. Jordan, [A note on start-up, plane Couette flow involving second-grade fluids](https://doi.org/10.1155/MPE.2005.539), _Math. Probl. Eng._ **2005** (2005) 539&ndash;545 |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2011_jordan_2010_nonrwa.ipynb) [christov_2011_jordan_2010_nonrwa](notebooks/christov_2011_jordan_2010_nonrwa.ipynb) | The Laplace transform of a suddenly moved plate's velocity; Stokes' first problem, second-grade fluid in a porous half-space | I. C. Christov, [Comments on: &ldquo;Energetic balance for the Rayleigh&ndash;Stokes problem of an Oldroyd-B fluid&rdquo;](https://doi.org/10.1016/j.nonrwa.2011.06.025), _Nonlinear Anal. RWA_ **12** (2011) 3687&ndash;3690; P. M. Jordan, [Comments on: &ldquo;Exact solution of Stokes' first problem for heated generalized Burgers' fluid in a porous half-space&rdquo;](https://doi.org/10.1016/j.nonrwa.2009.01.010), _Nonlinear Anal. RWA_ **11** (2010) 1198&ndash;1200 |

The notebooks are independent of each other; start with any of them. [christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) is the shortest route to the main idea.

## One mistake, many papers

The velocity of a plate set in motion at $t = 0^+$ is $\widetilde U(t)H(t)$, and its time derivative contains $\widetilde U(0)\delta(t)$. **Every erroneous solution reproduced here loses that $\delta(t)$**: it is dropped when the Fourier sine transform meets a mixed derivative, or hidden in an initial condition when the steady state is subtracted before an eigenfunction expansion.

What is lost has a clean physical meaning. For a fluid with a retardation time $t_r$ (second-grade, Oldroyd-B, Jeffreys), the erroneous solution is the _exact_ solution for a different plate, one whose start-up jump is ramped on the retardation time:
$$
u(0,t) = \left[\widetilde U(t) - \widetilde U(0)\,\mathrm{e}^{-t/t_r}\right]H(t),
$$
For a plate moved at constant velocity, the Laplace transform of the erroneous solution is the correct one divided by $1 + t_r s$. I. C. Christov & C. I. Christov (2010) found this ramped plate for Stokes' first problem of a second-grade fluid; each notebook with an erroneous solution shows, in its section _What problem does the wrong solution actually solve?_, that the same holds for its erroneous solution. For the oscillating plate this answers the question that Christov & Jordan (2012, p. 330) left open, of "what kind of boundary condition the wrong solution satisfies, or whether it has any physical meaning."

Two consequences follow. For a Newtonian or Maxwell fluid ($t_r = 0$), or a plate started without a jump ($\widetilde U(0) = 0$, such as $\sin\omega t$), the error disappears, **so reducing a solution to one of these limits does not validate it.** And since the two plates agree after a few retardation times, the erroneous solution looks right at long times; the difference is in the start-up, which is what the problem is about.

## Run them

Click a Colab badge, or run locally:

```bash
git clone https://github.com/ichristov/viscoelastic-startup
cd viscoelastic-startup
python3 -m pip install -r requirements.txt     # or: conda env create -f environment.yml
jupyter lab notebooks/
```

Each notebook runs top to bottom on a fresh kernel and regenerates every number and figure it shows; there are no data files. On a laptop, all eight together take under four minutes, the slowest ([christov_2010_stokes1_oldroydb](notebooks/christov_2010_stokes1_oldroydb.ipynb)) about two. The notebooks are committed executed, so they can also be read on GitHub without running them, with a static plot in place of each interactive one. The regenerated paper figures are also in [`figures/`](figures/).

⚠️ The notebooks may need updates to run on other platforms, and as the underlying Python libraries evolve.

## Reading a notebook

- **The erroneous solutions are marked so they cannot be mistaken for correct ones.** Each is bracketed by &#x26A0;&#xFE0F; banners, implemented in a function named `wrong_<author>_<equation>`, and drawn as a vermillion dashed curve labeled "wrong:". It is transcribed from the original paper, with its page, and never fixed.
- **Misprints in the Comments themselves are corrected in place, with a note** saying what was printed and why it is corrected.
- **Every claim is checked twice**, against a numerical inversion of the Laplace transform ([de Hoog _et al._, 1982](https://doi.org/10.1137/0903022), via [mpmath](https://mpmath.org)) and against a finite-difference scheme, with convergence tables.
- **Anything a notebook shows that its paper does not state** (the ramped-plate identifications) is marked "shown here".

## Citing

Cite the Comment paper whose results you use; the notebook's REFERENCES cell has the entry. To cite the notebooks themselves, cite this repository by its URL and the commit you used.

## Licenses

Two licenses, split by what the thing is, cell by cell:

- **Code &mdash; [BSD-3-Clause](LICENSE).** The code cells of the notebooks, and the scripts and configuration files.
- **Text and figures &mdash; [CC-BY-4.0](LICENSE-TEXT).** The markdown cells of the notebooks, this README, the figures and the cover art.

Neither covers the papers being reproduced or the papers they correct: those are their authors' work, cited and quoted with attribution, and not redistributed here.
