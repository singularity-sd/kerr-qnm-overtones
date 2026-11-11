"""Reproduces the accuracy numbers of the paper and writes them to results.json.

Compares the closed-form fits in code/kerr_qnm_fit.py with the Leaver continued-fraction frequencies of the
confirmation spin grid (code/data/, disjoint from the calibration grid):
- version A: l = m = 2..7, overtones n = 0..4;
- version B (the 72-number formula of the paper): l = m = 3..7, overtones n = 0..7;
- version C (40 numbers): l = m = 2, overtones n = 0..4.
For each case it reports the worst relative error on omega_R and omega_I.

Run: python experiment.py   (needs only numpy)
"""

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "code"))
from kerr_qnm_fit import omega_A, omega_B, omega_C  # noqa: E402

DATA = HERE / "code" / "data"


def worst(f, path, ns):
    d = np.genfromtxt(path, delimiter=",", names=True)
    k = np.isin(d["n"], ns)
    w = f(d["a"][k], d["n"][k])
    return (float((np.abs(w.real - d["omega_R"][k]) / d["omega_R"][k]).max()),
            float((np.abs(-w.imag - d["omega_I"][k]) / d["omega_I"][k]).max()))


def main():
    res = {"description": "worst relative error against Leaver frequencies on the confirmation spin grid",
           "A": {}, "B": {}, "C": {}}
    for l in range(2, 8):
        r, i = worst(lambda a, n: omega_A(a, l, n), DATA / f"confirmation_l{l}m{l}.csv", range(5))
        res["A"][f"l={l}"] = {"omega_R": r, "omega_I": i}
    for l in range(3, 8):
        r, i = worst(lambda a, n: omega_B(a, l, n), DATA / f"confirmation_high_l{l}m{l}.csv", range(8))
        res["B"][f"l={l}"] = {"omega_R": r, "omega_I": i}
    r, i = worst(omega_C, DATA / "confirmation_l2m2.csv", range(5))
    res["C"]["l=2"] = {"omega_R": r, "omega_I": i}
    res["B_max"] = {"omega_R": max(v["omega_R"] for v in res["B"].values()),
                    "omega_I": max(v["omega_I"] for v in res["B"].values())}
    (HERE / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    for v in ("A", "B", "C"):
        for l, e in res[v].items():
            print(f"{v}  {l}: worst error Re {e['omega_R']:.2%}, Im {e['omega_I']:.2%}")
    print(f"version B, all l: Re {res['B_max']['omega_R']:.2%}, Im {res['B_max']['omega_I']:.2%}")


if __name__ == "__main__":
    main()
