# viscoelastic-startup

![Left: the posed plate velocity, a step, and the ramp 1 - exp(-t/t_r) that the erroneous solutions actually solve. Right: start-up of plane Couette flow of an Oldroyd-B fluid at three times, the correct profile in blue with arrows, the erroneous series vermillion dashed, lagging as if the plate were ramped](assets/cover.png)

This is a GitHub repository for the verification of exact solutions for **start-up flows of viscoelastic fluids**, maintained by Prof. [Ivan C. Christov](https://christov.tmnt-lab.org). A plate, at rest for all $t < 0$, is suddenly set into motion at $t = 0^+$ and drags a [viscoelastic](https://en.wikipedia.org/wiki/Viscoelasticity) fluid (modeled by the second-grade, [Oldroyd-B](https://en.wikipedia.org/wiki/Oldroyd-B_model) or Gordon&ndash;Schowalter models, for example) along with it. Variants include [Stokes' first](https://en.wikipedia.org/wiki/Rayleigh_problem) and [second](https://en.wikipedia.org/wiki/Stokes_problem) problems on an unbounded domain, and the [start-up of plane Couette flow](https://en.wikipedia.org/wiki/Couette_flow#Startup) in a channel.

Over the last two decades, many (sometimes) highly cited papers have presented "new exact solutions" to these classical problems that are incorrect. The mathematical error is elementary, and it is the same one each time. Together with C. I. Christov and P. M. Jordan, I have been correcting these papers, one Comment at a time, in a project I loosely call _On Stokes' problems: a study in repetitive errors in the fluid mechanics literature_. This is the open-source GitHub version of the project.

## Nullius in verba

Although these Comments definitively settled the mathematics and solutions over a decade ago, the same errors continue to pop up and be promulgated. In this area of mechanics, everything is demonstrably true or false; there are no gray areas. So, rather than ask the reader to take my word for it, **each notebook in this repository reproduces one of those corrections from scratch**: the corrected solution, the erroneous published solution implemented exactly as printed, an independent check of both, and the paper's comparison figure(s), regenerated.

🚀 Getting started: the notebooks are independent of each other; [christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) is the shortest route to the main idea. From there, the two [christov_2010_stokes1_*](notebooks/christov_2010_stokes1_second_grade.ipynb) notebooks collect the correct solutions against which all the erroneous ones are checked, while [jordan_2005_second_grade_couette](notebooks/jordan_2005_second_grade_couette.ipynb) and [christov_2013_oldroydb_couette](notebooks/christov_2013_oldroydb_couette.ipynb) show the same mistake reached by a different route: an eigenfunction expansion in a channel, rather than an integral transform in a half-space.

| Notebook | Problem | Reproduces |
|---|---|---|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2013_oldroydb_couette.ipynb)<br>[christov_2013_oldroydb_couette](notebooks/christov_2013_oldroydb_couette.ipynb) | Start-up of plane Couette flow, Oldroyd-B (Jeffreys) fluid: the textbook eigenfunction expansion versus the causal one | [[1]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2009_oldroydb_porous.ipynb)<br>[christov_jordan_2009_oldroydb_porous](notebooks/christov_jordan_2009_oldroydb_porous.ipynb) | Stokes' first problem, Oldroyd-B fluid in a porous half-space | [[2]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_christov_2010_second_grade.ipynb)<br>[christov_christov_2010_second_grade](notebooks/christov_christov_2010_second_grade.ipynb) | Stokes' first problem, second-grade fluid | [[3]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_second_grade.ipynb)<br>[christov_2010_stokes1_second_grade](notebooks/christov_2010_stokes1_second_grade.ipynb) | Stokes' first problem, second-grade fluid: three correct representations of the solution | [[4]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2010_stokes1_oldroydb.ipynb)<br>[christov_2010_stokes1_oldroydb](notebooks/christov_2010_stokes1_oldroydb.ipynb) | Stokes' first problem, Oldroyd-B fluid: three correct representations of the solution | [[4]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_jordan_2012_second_grade_stokes2.ipynb)<br>[christov_jordan_2012_second_grade_stokes2](notebooks/christov_jordan_2012_second_grade_stokes2.ipynb) | Transient Stokes' second problem (oscillating plate), second-grade fluid, half-space and strip | [[5]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/jordan_2005_second_grade_couette.ipynb)<br>[jordan_2005_second_grade_couette](notebooks/jordan_2005_second_grade_couette.ipynb) | Start-up of plane Couette flow, second-grade fluid | [[6]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/christov_2011_jordan_2010_nonrwa.ipynb)<br>[christov_2011_jordan_2010_nonrwa](notebooks/christov_2011_jordan_2010_nonrwa.ipynb) | The Laplace transform of a suddenly moved plate's velocity; Stokes' first problem, second-grade fluid in a porous half-space | [[7, 8]](#citing) |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ichristov/viscoelastic-startup/blob/main/notebooks/balan_2023_startup_couette.ipynb)<br>[balan_2023_startup_couette](notebooks/balan_2023_startup_couette.ipynb) | Start-up of plane Couette flow, Gordon&ndash;Schowalter fluid, Oldroyd-B and corotational (Jaumann) cases: initial data that are inconsistent with a retardation time, and the figure of a submitted Comment | [[9]](#citing) |

Four notebooks depart from that pattern and say so at the top: the two Christov (2010) notebooks collect correct representations instead of correcting one paper; the Christov (2011) and Jordan (2010) notebook corrects a method rather than a formula, and neither of its papers has a figure, so its figure is new; and the Balan (2023) notebook reproduces initial data rather than a printed solution.

## One mistake, many papers

Let $V_\mathrm{plate}(t) \equiv v_x(0,t)$ be the velocity of the plate. For a plate at rest until it is suddenly set into motion at $t = 0^+$,
**posed start-up:**

```math
V_\mathrm{plate}(t) = V_0 f(t)H(t),
```

where $V_0$ is the plate's speed, $f$ the shape of its motion ($f \equiv 1$ for start-up, $\cos(\omega t)$ or $\sin(\omega t)$ for an oscillating plate), and $H$ the [Heaviside unit step function](https://en.wikipedia.org/wiki/Heaviside_step_function). In the sense of [distributions](https://en.wikipedia.org/wiki/Distribution_(mathematics)), the derivative of $V_\mathrm{plate}$ contains $V_0f(0)\delta(t)$. The [Dirac delta distribution](https://en.wikipedia.org/wiki/Dirac_delta_function), $\delta(t)$, has no point values; however, when it is the forcing term of an ODE in $t$, it contributes to the solution. (Prof. Arthur Mattuck's outstanding MIT 18.03 video lectures on [discontinuous inputs](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-22-using-laplace-transform-to-solve-odes-with-discontinuous-inputs/) and [impulse inputs](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-23-use-with-impulse-inputs/) explain this beautifully.) **Every erroneous solution reproduced here loses that $\delta(t)$**: it is treated as identically zero when the [Fourier sine transform](https://en.wikipedia.org/wiki/Sine_and_cosine_transforms) meets a mixed derivative, or it is hidden in an initial condition when the steady state is "subtracted off" before an [eigenfunction expansion](https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory). The [Laplace transform](https://en.wikipedia.org/wiki/Laplace_transform) in time, applied to the problem as posed, cannot make this mistake.

What is lost has a clean physical meaning. For a fluid with a retardation timescale $t_r$ ($\lambda_2$ for Oldroyd-B, $\alpha/\nu$ for second grade), the erroneous solution is the _exact_ solution for a different plate, one whose start-up jump is ramped on that timescale:
**solved ramp-up:**

```math
V_\mathrm{plate}(t) = V_0\left[f(t) - f(0)\,\mathrm{e}^{-t/t_r}\right]H(t).
```

For a plate moved at constant velocity ($f \equiv 1$), the Laplace transform of the erroneous solution is the correct one divided by $1 + t_r s$. C. I. Christov and I realized the connection to this ramped plate for Stokes' first problem of a second-grade fluid [[3]](#citing); each notebook shows the same for its own erroneous solution. For the oscillating plate, it answers the question P. M. Jordan and I left open in [[5]](#citing) (p. 330), of "what kind of boundary condition the wrong solution satisfies, or whether it has any physical meaning." A recent numerical study [[9]](#citing) solves that same ramped plate: its initial data set the shear stress to zero while the plate is already moving, losing the $\delta(t)$ in a method-of-lines code rather than in a transform.

🎲 No experiment ramps a plate on the fluid's own retardation time: $t_r$ is a material property, not a setting on an apparatus, so the ramp is an artifact of the error and not a boundary condition anyone would have chosen to impose.

Two consequences follow. For a Newtonian or Maxwell fluid ($t_r = 0$), or a plate started without a jump ($f(0) = 0$, such as $f = \sin(\omega t)$), the error disappears, **so reducing a solution to one of these limits does not validate it.** And since the two plates agree after a few $t_r$, the erroneous solution looks right at long times; the difference is in the start-up, which is what the problem is about.

## Running the notebooks

Click a Colab badge, or run locally:

```bash
git clone https://github.com/ichristov/viscoelastic-startup
cd viscoelastic-startup
python3 -m pip install -r requirements.txt     # or: conda env create -f environment.yml
jupyter lab notebooks/
```

Each notebook runs top to bottom on a fresh kernel and regenerates every number and figure it shows, except the values read off Balan's published figures, which are listed in the cell that uses them and can be re-derived with the digitizers in [`tools/`](tools/); the notebooks themselves read no data files. On a laptop, each takes up to a few minutes. The notebooks are committed executed, so they can also be read on GitHub without running them, with a static plot in place of each interactive one. The regenerated paper figures are also in [`figures/`](figures/).

⚠️ The notebooks are not meant to be robust: they may need updates on other platforms, or as the Python libraries evolve.

💡 To run a notebook as a standalone Python script (stripping all the Markdown commentary), convert it:

```bash
jupyter nbconvert notebooks/christov_christov_2010_second_grade.ipynb --to python --PythonExporter.exclude_markdown=True
ipython notebooks/christov_christov_2010_second_grade.py
```

Run the script with `ipython`, not `python`, because the notebooks use IPython "magic" commands such as `%matplotlib inline`.

## Reading a notebook

- **The erroneous solutions are marked so they cannot be mistaken for correct ones.** Each is bracketed by &#x26A0;&#xFE0F; banners, implemented in a function named `wrong_<author>_<equation>`, and drawn as a vermillion dashed curve labeled "wrong:". It is transcribed from the original paper, with its page, and never fixed.
- **Misprints in the Comments themselves are corrected in place, with a note** saying what was printed and why it is corrected.
- **Every claim is checked twice**, against a numerical inversion of the Laplace transform ([de Hoog _et al._, 1982](https://doi.org/10.1137/0903022), via [mpmath](https://mpmath.org)) and against a finite-difference scheme, with convergence tables.
- **Anything a notebook shows that its paper does not state** (the ramped-plate identifications) is marked "shown here".
- **Each notebook keeps its paper's notation**, so the unit step function is $H(t)$ in some of them and $\theta(t)$ in others.
- **Oldroyd-B and Jeffreys are used interchangeably**, here and in the notebooks: in these unidirectional flows the convective terms of the Oldroyd-B model drop out of the shear-stress equation, leaving the linear Jeffreys model. Only the Gordon&ndash;Schowalter slip parameter keeps the normal stresses coupled in.

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
9. C. Balan, [Note on the start-up of Couette flow for viscoelastic fluids](https://doi.org/10.1063/5.0173510), _Phys. Fluids_ **35** (2023) 113108; the notebook reproduces its start-up computations and my submitted Comment on it.

## Repetitive errors, near and far

📝 Three more Comments in the same series are not (yet) reproduced here:

- I. C. Christov, [Comment on &ldquo;The velocity field due to an oscillating plate in an Oldroyd-B fluid&rdquo;](https://doi.org/10.1139/cjp-2015-0374) by C. C. Hopkins and J. R. de Bruyn [Can. J. Phys. 92, 533 (2014)], _Can. J. Phys._ **93** (2015) 1651&ndash;1652.
- I. C. Christov, [Comment on: &ldquo;Stokes' first problem for heated flat plate with Atangana&ndash;Baleanu fractional derivative&rdquo;](https://doi.org/10.1016/j.chaos.2021.110999) [Chaos Solitons Fractals 117 (2018) 68], _Chaos Solitons Fractals_ **147** (2021) 110999. It shows that a 2018 paper commits the mathematical mistake already identified and corrected in [[3]](#citing).
- I. C. Christov, [Comment on &ldquo;Scattering Cancellation-Based Cloaking for the Maxwell&ndash;Cattaneo Heat Waves&rdquo;](https://doi.org/10.1103/PhysRevApplied.15.058001) [Phys. Rev. Applied 11, 044089 (2019)], _Phys. Rev. Applied_ **15** (2021) 058001. [arXiv:1908.02188](https://arxiv.org/abs/1908.02188)

George Santayana wrote that ["Those who cannot remember the past are condemned to repeat it"](https://en.wikiquote.org/wiki/George_Santayana), a line more often misattributed to Churchill than read. Indeed.

Nor is the genre new. Reviewing a 1950 paper in _Mathematical Reviews_, C. Truesdell wrote:

> This paper, whose intent is stated in its title, gives wrong solutions to trivial problems. The basic error, however, is not new: &hellip; the stress-strain relations used are those once proposed by St.-Venant &hellip;, whose incorrect confusion of coordinates in the deformed and undeformed states of the body was pointed out by Brill and Boussinesq &hellip;
>
> &mdash; C. Truesdell, review of G. Garc&iacute;a, _Equations of finite vibratory motions in isotropic elastic media_, _Actas Acad. Ci. Lima_ **13** (1950) 29&ndash;38, [MR0039515 (12,561a)](https://mathscinet.ams.org/mathscinet-getitem?mr=0039515)

On Truesdell himself: J. M. Ball, R. D. James, [The scientific life and influence of Clifford Ambrose Truesdell III](https://doi.org/10.1007/s002050100178), _Arch. Rational Mech. Anal._ **161** (2002) 1&ndash;26. [Free copy](https://people.maths.ox.ac.uk/ball/Miscelleaneous%20Articles/truesdell.pdf)

🔁 Nor is it confined to viscoelasticity, or to me. Corrections of the same kind are written in neighboring fields, and catalogues of the genre exist:

- E. Pucci, G. Saccomandi, R. Vitolo, [Bogus transformations in mechanics of continua](https://doi.org/10.1016/j.ijengsci.2015.10.009), _Int. J. Eng. Sci._ **99** (2016) 13&ndash;21.
- G. Romano, [Comment on the paper &ldquo;Exact solution of Eringen's nonlocal integral model for bending of Euler&ndash;Bernoulli and Timoshenko beams&rdquo; by Meral Tuna &amp; Mesut Kirca](https://doi.org/10.1016/j.ijengsci.2016.09.009), _Int. J. Eng. Sci._ **109** (2016) 240&ndash;242.
- P. M. Jordan, N. Valdivia, [Comment on &ldquo;On some geometrical aspects of the potential structure of the equations of evolution: The case of Navier&ndash;Stokes&rdquo;](https://doi.org/10.1209/0295-5075/ae7754), _Europhys. Lett._ **155** (2026) 33003.
- A. Pantokratoras has done the same for boundary-layer flows, in dozens of Comments and in two surveys: [A common error made in investigation of boundary layer flows](https://doi.org/10.1016/j.apm.2007.11.009), _Appl. Math. Model._ **33** (2009) 413&ndash;422, and [Four usual errors made in investigation of boundary layer flows](https://doi.org/10.1016/j.powtec.2019.05.060), _Powder Technol._ **353** (2019) 505&ndash;508.
- N. A. Kudryashov, [Seven common errors in finding exact solutions of nonlinear differential equations](https://doi.org/10.1016/j.cnsns.2009.01.023), _Commun. Nonlinear Sci. Numer. Simul._ **14** (2009) 3507&ndash;3529, continued by R. O. Popovych, O. O. Vaneeva, [More common errors in finding exact solutions of nonlinear differential equations: Part I](https://doi.org/10.1016/j.cnsns.2010.01.037), _ibid._ **15** (2010) 3887&ndash;3899.
- F. M. Fern&aacute;ndez has published dozens of such Comments, on methods as well as on solutions: [Comment on &ldquo;The asymptotic iteration method revisited&rdquo;](https://doi.org/10.1063/5.0008333), _J. Math. Phys._ **61** (2020) 064101, and [Comment on &ldquo;Semi-exact solutions of sextic potential plus a centrifugal term&rdquo;](https://doi.org/10.1007/s10910-023-01458-8), _J. Math. Chem._ **61** (2023) 893&ndash;895. Unpublished, but the best title of the genre: [Homotopy perturbation method: when infinity equals five](https://arxiv.org/abs/0810.3318) ([arXiv:0810.3318](https://arxiv.org/abs/0810.3318), 2008), on a heat-transfer paper whose infinity turns out to be five.

Why such errors persist, and why mathematics corrects them more slowly than other fields, is itself a subject: J. F. Grcar, [Errors and corrections in mathematics literature](https://doi.org/10.1090/noti988), _Notices Amer. Math. Soc._ **60** (2013) 418&ndash;425.

## AI use

This repository&mdash;the notebooks, their organization, this README and the supporting scripts&mdash;was designed and implemented with Claude (Anthropic) as a coding and calculus assistant, working throughout from I.C.C.'s Comments and his existing Matlab and Mathematica codes, under his direction. Every number and figure is regenerated and cross-checked inside the notebook that shows it, and all results were independently verified by I.C.C., who is responsible for the content.

## Licenses

Two licenses, split by what the thing is, cell by cell:

- **Code &mdash; [BSD-3-Clause](LICENSE).** The code cells of the notebooks, and the scripts and configuration files.
- **Text and figures &mdash; [CC-BY-4.0](LICENSE-TEXT).** The markdown cells of the notebooks, this README, the figures and the cover art.

Neither covers the papers being reproduced or the papers they correct: those are their authors' work, cited and quoted with attribution, and not redistributed here.
