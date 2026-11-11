# A single closed-form fit for Kerr quasinormal overtones up to near-extremal spin



**Paper:** [paper.pdf](paper.pdf) · **Page:** [singularitysd.com/research/kerr.html](https://singularitysd.com/research/kerr.html) · Preprint, not yet peer reviewed.

## Abstract

Compact fitting formulas for Kerr quasinormal-mode (QNM) frequencies are a basic ingredient of ringdown modelling. The standard ones cover only the fundamental mode and the first one or two overtones, and they lose accuracy as the spin approaches extremality. We present a single closed-form expression for the prograde $l=m$ gravitational modes. The damping rate is written as $(n+\tfrac12)$ times the Lyapunov exponent of the prograde equatorial light ring, and the oscillation frequency as $m/2$ times a correction factor. Each base is multiplied by one rational correction in $s=\sqrt{1-a}$, whose coefficients are low-order polynomials in the overtone index $n$ and in $1/(l+\tfrac12)$. With 72 numbers in total, the formula reproduces Leaver continued-fraction frequencies for $l=m=3$–$7$, overtones $n=0$–$7$ and $0\le a\le 0.9999$. The maximum relative error is $0.61\%$ on $\omega_R$ and $0.32\%$ on $\omega_I$, measured on a spin grid disjoint from the calibration grid. It also predicts modes never used in the fit, with errors of $0.18\%/0.07\%$ at $l=7$ and below $1.5\%/0.7\%$ up to $l=12$. A dedicated 40-number variant covers the dominant $l=m=2$ mode ($n=0$–$4$) with errors of $1.2\%/1.0\%$. Every comparison was preregistered and run once. In all of them the formulas are more accurate than the Berti–Cardoso–Will and two-term London–Fauchon-Jones fits calibrated separately on each mode and overtone.

## How it was made

The plan of the test was fixed before looking at the confirmation data, and the test was run once.

## What is in this repository

| file | what it is |
|---|---|
| `code/` | the formula (`kerr_qnm_fit.py`) and the Leaver frequencies of the confirmation grid |
| `coefficients.tex` | coefficient table used by the paper |
| `experiment.py` | recomputes the accuracy of the formula on the confirmation grid |
| `fig_errors_l7.png` | figure |
| `main.tex` | LaTeX source of the paper |
| `paper.pdf` | the paper |
| `results.json` | worst relative errors per mode, as reported in the paper |

## Reproduce

```bash
pip install numpy
python experiment.py
```

It writes `results.json`.

## Cite

```bibtex
@misc{singularity_kerr_qnm_overtones_2026,
  title  = {A single closed-form fit for Kerr quasinormal overtones up to near-extremal spin},
  author = {Singularity},
  year   = {2026},
  url    = {https://github.com/singularity-sd/kerr-qnm-overtones}
}
```

## License

Code: MIT (`LICENSE`). Paper, text and figures: CC BY 4.0 (`LICENSE-paper.md`). Third-party data keep their own licence where stated.

---

Part of [Singularity](https://singularitysd.com): forecasting where science goes next, then testing it.
