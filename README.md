# Z(p) Irrationality & Transcendence Program

[![CI](https://github.com/kugguk2022/zp-program/actions/workflows/ci.yml/badge.svg)](https://github.com/kugguk2022/zp-program/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A focused, reproducible research repo for the arithmetic nature of the number:
> <p align="center">
>  <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20Z(p)%20\;=\;%20e^{\pi\,\zeta(p-1)/p}%20+%201%20\qquad%20(p%20\text{%20prime%20}\ge%203,%20p%20\text{%20odd})" alt="Z(p) definition" />
> </p>

This project keeps things **tight**: only the math needed for <img src="https://latex.codecogs.com/svg.latex?Z(p)" alt="Z(p)" />.  
We derive the exact rational coefficient <img src="https://latex.codecogs.com/svg.latex?c_p" alt="c_p" />, explain **why** transcendence here is hard,
state **clean conditional theorems**, and provide **reproducible numeric evidence** (PSLQ scans) — clearly marked as *heuristics*, not proofs.

---

## 🧭 TL;DR
- For any odd prime <img src="https://latex.codecogs.com/svg.latex?p\ge%203" alt="p>=3" />, write
  <p align="center">
    <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20Z(p)%20=%20e^{c_p\pi^p}%20+%201" alt="Z(p) in terms of c_p" />
  </p>
  where
  <p align="center">
    <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20c_p%20\;=\;%20(-1)^{\frac{p+1}{2}}\;\frac{2^{\,p-2}\,%20B_{p-1}}{p\,(p-1)!}\;\in\;\mathbb{Q}\setminus\{0\}" alt="c_p definition" />
  </p>
  and <img src="https://latex.codecogs.com/svg.latex?B_{n}" alt="B_n" /> is the <img src="https://latex.codecogs.com/svg.latex?n" alt="n" />-th Bernoulli number.
- Proving <img src="https://latex.codecogs.com/svg.latex?Z(p)" alt="Z(p)" /> is transcendental reduces to proving <img src="https://latex.codecogs.com/svg.latex?e^{c_p\pi^{p}}" alt="e^(c_p*pi^p)" /> is transcendental.  
  This is **not** settled by standard theorems (LW, Gelfond–Schneider, Baker–Wüstholz).  
- We outline **conditional routes** (Schanuel, Four Exponentials, “π-power Lindemann”) and supply **numerical evidence** via PSLQ with reproducibility.

---

## 🧮 Math snapshot

Using the classical even-zeta formula
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20\zeta(2k)=\frac{(-1)^{k+1}%20B_{2k}(2\pi)^{2k}}{2(2k)!}" alt="Even zeta formula" />
</p>
let <img src="https://latex.codecogs.com/svg.latex?k=(p-1)/2" alt="k=(p-1)/2" />. Then
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20\frac{\pi\,\zeta(2k)}{p}%20\;=\;%20\frac{(-1)^{k+1}%20B_{2k}\,2^{2k-1}\,\pi^{2k+1}}{(2k)!\,(2k+1)}%20\;=\;%20c_p\,\pi^{p}" alt="Derivation of c_p" />
</p>

Therefore <img src="https://latex.codecogs.com/svg.latex?Z(p)=e^{c_p\pi^{p}}+1" alt="Z(p) formula" /> with
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?\displaystyle%20\boxed{\,c_p%20=%20(-1)^{\frac{p+1}{2}}%20\,\frac{2^{\,p-2}\,%20B_{p-1}}{p\,%20(p-1)!}\in\mathbb{Q}\,}" alt="c_p boxed formula" />
</p>

**Sanity checks**
| p | <img src="https://latex.codecogs.com/svg.latex?c_p" alt="c_p" /> | Reason |
|---|---------|--------|
| 3 | <img src="https://latex.codecogs.com/svg.latex?1/18" alt="1/18" /> | <img src="https://latex.codecogs.com/svg.latex?\pi\zeta(2)/3%20=%20\pi^3/18" alt="c_3 reason" /> |
| 5 | <img src="https://latex.codecogs.com/svg.latex?1/450" alt="1/450" /> | <img src="https://latex.codecogs.com/svg.latex?\pi\zeta(4)/5%20=%20\pi^5/450" alt="c_5 reason" /> |
| 7 | <img src="https://latex.codecogs.com/svg.latex?1/6615" alt="1/6615" /> | <img src="https://latex.codecogs.com/svg.latex?\pi\zeta(6)/7%20=%20\pi^7/6615" alt="c_7 reason" /> since <img src="https://latex.codecogs.com/svg.latex?\zeta(6)=\pi^6/945" alt="zeta(6)" /> |

---

## 🧱 Why this is hard
- **Lindemann–Weierstrass** proves <img src="https://latex.codecogs.com/svg.latex?e^{\alpha}" alt="e^alpha" /> transcendental when <img src="https://latex.codecogs.com/svg.latex?\alpha" alt="alpha" /> is **algebraic** and <img src="https://latex.codecogs.com/svg.latex?\alpha\neq%200" alt="alpha != 0" />. Here <img src="https://latex.codecogs.com/svg.latex?\alpha=c_p\pi^p" alt="alpha = c_p*pi^p" /> is not known to be algebraic (indeed, <img src="https://latex.codecogs.com/svg.latex?\pi" alt="pi" /> is transcendental), so LW **does not apply**.
- **Gelfond–Schneider** concerns <img src="https://latex.codecogs.com/svg.latex?a^b" alt="a^b" /> with algebraic <img src="https://latex.codecogs.com/svg.latex?a\neq%200,1" alt="a != 0,1" /> and irrational algebraic <img src="https://latex.codecogs.com/svg.latex?b" alt="b" /> — not our form.
- **Linear forms in logarithms** handle logs of algebraic numbers — again, <img src="https://latex.codecogs.com/svg.latex?\pi^p" alt="pi^p" /> falls outside their direct scope.

**Takeaway:** Showing <img src="https://latex.codecogs.com/svg.latex?e^{c_p\pi^p}" alt="e^(c_p*pi^p)" /> transcendental demands tools beyond current unconditional results.

---

## ✅ What we *can* do now

### Conditional routes (clean implications)
- **(A) π-power Lindemann (hypothetical).** If for all nonzero algebraic <img src="https://latex.codecogs.com/svg.latex?q" alt="q" /> and integers <img src="https://latex.codecogs.com/svg.latex?m\ge%201" alt="m >= 1" />, <img src="https://latex.codecogs.com/svg.latex?e^{q\pi^{m}}" alt="e^(q*pi^m)" /> is transcendental, then **all** <img src="https://latex.codecogs.com/svg.latex?Z(p)" alt="Z(p)" /> are transcendental for odd primes <img src="https://latex.codecogs.com/svg.latex?p\ge%203" alt="p >= 3" />.
- **(B) Four Exponentials / Schanuel (conditional).** Under standard independence assumptions, arrange a <img src="https://latex.codecogs.com/svg.latex?2\times2" alt="2x2" /> setup with <img src="https://latex.codecogs.com/svg.latex?\{1,%20\pi\}" alt="{1, pi}" /> vs <img src="https://latex.codecogs.com/svg.latex?\{c_p,%20\pi^{p-1}\}" alt="{c_p, pi^(p-1)}" /> to force transcendence of one of the relevant exponentials and isolate <img src="https://latex.codecogs.com/svg.latex?e^{c_p\pi^p}" alt="e^(c_p*pi^p)" />.
- **(C) Periods extension (speculative).** Since <img src="https://latex.codecogs.com/svg.latex?\zeta(2k)" alt="zeta(2k)" /> are periods, an “LW-for-periods” principle would also settle the case.

### Unconditional numerical evidence (heuristic)
We use **PSLQ** to search for small-degree/height algebraic relations for <img src="https://latex.codecogs.com/svg.latex?Z(p)" alt="Z(p)" />.  
- **If PSLQ returns `None`** up to given bounds: *no* relation found at that scale (evidence **against** low-degree algebraicity, not a proof).  
- **If PSLQ finds a relation:** we validate with higher precision; if stable, that’s a red flag to investigate.

---

## 📦 Repository map

```
z_p/
  zeta_even_reduction.md   # Derivation of c_p
  proof_sketch.md          # Conditional routes, barriers, plan
  experiments/
    pslq_scan.py           # Reproducible PSLQ exploration
tests/
  test_cp.py               # Unit tests for c_p at p=3,5,7
.github/workflows/
  ci.yml                   # Python 3.11 CI: lint+tests
requirements.txt
LICENSE
```

---

## 🚀 Quick start

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

Run a PSLQ scan (example):
```bash
python z_p/experiments/pslq_scan.py --pmin 3 --pmax 31 --prec 300 --deg 6 --height 2000
```
- `--prec`: decimal precision for mpmath (increase if you raise degree/height).
- `--deg`: maximal polynomial degree tested.
- `--height`: bound on integer coefficients in relations.

**Interpreting output**
```
# Z(p) PSLQ scan
# Columns: p, c_p (rational), PSLQ_relation (or None)

p= 3  c_p=1/18     PSLQ=None
p= 5  c_p=1/450    PSLQ=None
...
```
`None` means *no* integer relation among \([1,x,x^2,\dots,x^{\deg}]\) up to `height` was detected at the chosen precision.

---

## 🧪 Testing
```bash
pytest -q
```
The tests verify the closed forms \(c_3=1/18\), \(c_5=1/450\), \(c_7=1/6615\). Add more checks as you extend the program.

---

## 🛣️ Roadmap
- **R1 — Numerics:** increase precision, degree/height; log stability of PSLQ outcomes across \(p \le 101\).
- **R2 — Conditional proofs:** formalize (A)–(C) in `proof_sketch.md` with crisp statements and dependency graphs.
- **R3 — Subsequence targets:** look for provable irrationality for specific \(p\)-families (if any feasible Diophantine method applies).
- **R4 — Documentation:** short survey of related transcendence problems; glossary; FAQ.

---

## 🤝 Contributing
PRs are welcome if they keep the repo focused on **Z(p)**. Please add tests and doc notes when you change math or numerics.

---

## 📚 Pointers (non-exhaustive)
- Even zeta values and Bernoulli numbers (classical).  
- Lindemann–Weierstrass theorem.  
- Four/Six Exponentials; Schanuel’s conjecture.  
*(Use your preferred references; this repo avoids bundling large PDFs.)*

---

## 📝 License
MIT — see `LICENSE`.
