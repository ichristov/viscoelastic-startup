# viscoelastic-startup

![Left: the velocity of a plate started impulsively, a unit step, and the ramp 1 - exp(-t/t_r) that the erroneous solutions actually describe. Right: velocity profiles of a second-grade fluid above the plate at three times, the correct solution in blue with arrows and the erroneous one as a vermillion dashed curve lagging behind it](assets/cover.png)

This is a GitHub repository for the verification and reproducibility of exact solutions for **start-up flows of viscoelastic fluids**, maintained by Prof. [Ivan C. Christov](https://christov.tmnt-lab.org). A plate, at rest for all $t < 0$, is suddenly set into motion at $t = 0^+$ and drags a second-grade, Oldroyd-B, or Jeffreys fluid along with it: Stokes' first and second problems, and the start-up of plane Couette flow.

Over the last two decades, dozens of (apparently) highly cited papers have presented "new exact solutions" to these classical problems that are, generally speaking, incorrect. The mathematical error is elementary, and it is the same one each time. Together with C. I. Christov and P. M. Jordan, I have been correcting these papers, one Comment at a time, in a project I call _On Stokes' problems: a study in repetitive errors in the fluid mechanics literature_. Although these Comments definitively settled the solutions years ago, the same errors continue to be duplicated and promulgated. In this area of mechanics, everything is demonstrably true or false by the rules of mathematics using deductive logic, and there are no gray areas. So, rather than ask the reader to take my word for it, **each notebook here reproduces one of those Comments from scratch**: the corrected solution, the erroneous published solution implemented exactly as printed, an independent check of both (a numerical inversion of the Laplace transform and a finite-difference solution), and the paper's comparison figure, regenerated.

🚀 Getting started (the notebooks are independent of each other; [christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) is the shortest route to the main idea):

| Notebook | Problem | Reproduces |
|---|---|---|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2013_oldroydb_couette.ipynb) [christov_2013_oldroydb_couette](notebooks/christov_2013_oldroydb_couette.ipynb) | Start-up of plane Couette flow, Oldroyd-B (Jeffreys) fluid: the textbook eigenfunction expansion versus the causal one | [[1]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2009_oldroydb_porous.ipynb) [christov_jordan_2009_oldroydb_porous](notebooks/christov_jordan_2009_oldroydb_porous.ipynb) | Stokes' first problem, Oldroyd-B fluid in a porous half-space | [[2]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_christov_2010_second_grade.ipynb) [christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) | Stokes' first problem, second-grade fluid | [[3]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_second_grade.ipynb) [christov_2010_stokes1_second_grade](notebooks/christov_2010_stokes1_second_grade.ipynb) | Stokes' first problem, second-grade fluid: three correct representations of the solution | [[4]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_oldroydb.ipynb) [christov_2010_stokes1_oldroydb](notebooks/christov_2010_stokes1_oldroydb.ipynb) | Stokes' first problem, Oldroyd-B fluid: three correct representations of the solution | [[4]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2012_second_grade_stokes2.ipynb) [christov_jordan_2012_second_grade_stokes2](notebooks/christov_jordan_2012_second_grade_stokes2.ipynb) | Transient Stokes' second problem (oscillating plate), second-grade fluid, half-space and strip | [[5]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/jordan_2005_second_grade_couette.ipynb) [jordan_2005_second_grade_couette](notebooks/jordan_2005_second_grade_couette.ipynb) | Start-up of plane Couette flow, second-grade fluid | [[6]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2011_jordan_2010_nonrwa.ipynb) [christov_2011_jordan_2010_nonrwa](notebooks/christov_2011_jordan_2010_nonrwa.ipynb) | The Laplace transform of a suddenly moved plate's velocity; Stokes' first problem, second-grade fluid in a porous half-space | [[7, 8]](#citing) |

## One mistake, many papers

The velocity of a plate suddenly set into motion at $t = 0^+$ is $\widetilde U(t)H(t)$, where $H$ is the Heaviside unit step function. In the sense of distributions, its derivative contains $\widetilde U(0)\delta(t)$. The Dirac-$\delta$ distribution has no point values; however, when it is the forcing term of an ODE in $t$, it contributes to the solution. **Every erroneous solution reproduced here loses that $\delta(t)$**: it is treated as identically zero when the Fourier sine transform meets a mixed derivative, or it is hidden in an initial condition when the steady state is "subtracted off" before an eigenfunction expansion.

What is lost has a clean physical meaning. For a fluid with a retardation time $t_r$ (second-grade, Oldroyd-B, Jeffreys), the erroneous solution is the _exact_ solution for a different plate, one whose start-up jump is ramped on the retardation time:
$$
u(0,t) = \left[\widetilde U(t) - \widetilde U(0)\,\mathrm{e}^{-t/t_r}\right]H(t).
$$
For a plate moved at constant velocity, the Laplace transform of the erroneous solution is the correct one divided by $1 + t_r s$. C. I. Christov and I found this ramped plate for Stokes' first problem of a second-grade fluid [[3]](#citing); each notebook with an erroneous solution shows, in its section _What problem does the wrong solution actually solve?_, that the same holds for its erroneous solution. For the oscillating plate, this answers the question that P. M. Jordan and I left open in [[5]](#citing) (p. 330), of "what kind of boundary condition the wrong solution satisfies, or whether it has any physical meaning."

Two consequences follow. For a Newtonian or Maxwell fluid ($t_r = 0$), or a plate started without a jump ($\widetilde U(0) = 0$, such as $\sin\omega t$), the error disappears, **so reducing a solution to one of these limits does not validate it.** And since the two plates agree after a few retardation times, the erroneous solution looks right at long times; the difference is in the start-up, which is what the problem is about.

## Running the notebooks

Click a Colab badge, or run locally:

```bash
git clone https://github.com/ichristov/viscoelastic-startup
cd viscoelastic-startup
python3 -m pip install -r requirements.txt     # or: conda env create -f environment.yml
jupyter lab notebooks/
```

Each notebook runs top to bottom on a fresh kernel and regenerates every number and figure it shows; there are no data files. On a laptop, all eight together take under four minutes, the slowest ([christov_2010_stokes1_oldroydb](notebooks/christov_2010_stokes1_oldroydb.ipynb)) about two. The notebooks are committed executed, so they can also be read on GitHub without running them, with a static plot in place of each interactive one. The regenerated paper figures are also in [`figures/`](figures/).

⚠️ The notebooks are unlikely to be robust and may require updates to run on different platforms, and as underlying Python libraries evolve.

## Reading a notebook

- **The erroneous solutions are marked so they cannot be mistaken for correct ones.** Each is bracketed by &#x26A0;&#xFE0F; banners, implemented in a function named `wrong_<author>_<equation>`, and drawn as a vermillion dashed curve labeled "wrong:". It is transcribed from the original paper, with its page, and never fixed.
- **Misprints in the Comments themselves are corrected in place, with a note** saying what was printed and why it is corrected.
- **Every claim is checked twice**, against a numerical inversion of the Laplace transform ([de Hoog _et al._, 1982](https://doi.org/10.1137/0903022), via [mpmath](https://mpmath.org)) and against a finite-difference scheme, with convergence tables.
- **Anything a notebook shows that its paper does not state** (the ramped-plate identifications) is marked "shown here".

## Citing

Please cite the Comment whose results you use; each notebook's REFERENCES cell has the entry. To cite the notebooks themselves, cite this repository by its URL and the commit you used. The notebooks reproduce:

1. I. C. Christov, [On a difficulty in the formulation of initial and boundary conditions for eigenfunction expansion solutions for the start-up of fluid flow](https://doi.org/10.1016/j.mechrescom.2013.05.005), _Mech. Res. Commun._ **51** (2013) 86&ndash;92. [arXiv:1305.5999](https://arxiv.org/abs/1305.5999)
2. C. I. Christov, P. M. Jordan, [Comment on &ldquo;Stokes' first problem for an Oldroyd-B fluid in a porous half space&rdquo;](https://doi.org/10.1063/1.3126503) [Phys. Fluids 17, 023101 (2005)], _Phys. Fluids_ **21** (2009) 069101.
3. I. C. Christov, C. I. Christov, [Comment on &ldquo;On a class of exact solutions of the equations of motion of a second grade fluid&rdquo;](https://doi.org/10.1007/s00707-010-0300-2) by C. Fetec&#259;u and J. Zierep (Acta Mech. 150, 135&ndash;138, 2001), _Acta Mech._ **215** (2010) 25&ndash;28. [arXiv:1003.2188](https://arxiv.org/abs/1003.2188)
4. I. C. Christov, [Stokes' first problem for some non-Newtonian fluids: Results and mistakes](https://doi.org/10.1016/j.mechrescom.2010.09.006), _Mech. Res. Commun._ **37** (2010) 717&ndash;723. [arXiv:1009.4416](https://arxiv.org/abs/1009.4416)
5. I. C. Christov, P. M. Jordan, [Comments on: &ldquo;Starting solutions for some unsteady unidirectional flows of a second grade fluid&rdquo;](https://doi.org/10.1016/j.ijengsci.2011.10.012) [Int. J. Eng. Sci. 43 (2005) 781], _Int. J. Eng. Sci._ **51** (2012) 326&ndash;332. [arXiv:1111.4464](https://arxiv.org/abs/1111.4464)
6. P. M. Jordan, [A note on start-up, plane Couette flow involving second-grade fluids](https://doi.org/10.1155/MPE.2005.539), _Math. Probl. Eng._ **2005** (2005) 539&ndash;545.
7. I. C. Christov, [Comments on: &ldquo;Energetic balance for the Rayleigh&ndash;Stokes problem of an Oldroyd-B fluid&rdquo;](https://doi.org/10.1016/j.nonrwa.2011.06.025) [Nonlinear Anal. RWA 12 (2011) 1], _Nonlinear Anal. RWA_ **12** (2011) 3687&ndash;3690. [arXiv:1107.2947](https://arxiv.org/abs/1107.2947)
8. P. M. Jordan, [Comments on: &ldquo;Exact solution of Stokes' first problem for heated generalized Burgers' fluid in a porous half-space&rdquo;](https://doi.org/10.1016/j.nonrwa.2009.01.010) [Nonlinear Anal. RWA 9 (2008) 1628], _Nonlinear Anal. RWA_ **11** (2010) 1198&ndash;1200.

📝 Two more Comments in the same series are not (yet) reproduced here: I. C. Christov, [Comment on &ldquo;The velocity field due to an oscillating plate in an Oldroyd-B fluid&rdquo;](https://doi.org/10.1139/cjp-2015-0374) by C. C. Hopkins and J. R. de Bruyn [Can. J. Phys. 92, 533 (2014)], _Can. J. Phys._ **93** (2015) 1651&ndash;1652, and I. C. Christov, [Comment on: &ldquo;Stokes' first problem for heated flat plate with Atangana&ndash;Baleanu fractional derivative&rdquo;](https://doi.org/10.1016/j.chaos.2021.110999) [Chaos Solitons Fractals 117 (2018) 68], _Chaos Solitons Fractals_ **147** (2021) 110999. The latter shows that a 2018 paper commits the mathematical mistake already identified and corrected in [[3]](#citing). It is claimed that Winston Churchill wrote that "Those that fail to learn from history are doomed to repeat it." Indeed.

## Licenses

Two licenses, split by what the thing is, cell by cell:

- **Code &mdash; [BSD-3-Clause](LICENSE).** The code cells of the notebooks, and the scripts and configuration files.
- **Text and figures &mdash; [CC-BY-4.0](LICENSE-TEXT).** The markdown cells of the notebooks, this README, the figures and the cover art.

Neither covers the papers being reproduced or the papers they correct: those are their authors' work, cited and quoted with attribution, and not redistributed here.
