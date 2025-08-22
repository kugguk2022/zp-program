# Z(p) Irrationality & Transcendence Program

> A focused, reproducible research repo for the arithmetic nature of
> <p align="center">
> $ Z(p) \;=\; e^{\pi\,\zeta(p-1)/p} + 1 \qquad (p \text{ prime }\ge 3,\ p \text{ odd}) .$
</p>
This project keeps things **tight**: only the math needed for $Z(p)$.  
We derive the exact rational coefficient $\(c_p\)$, explain **why** transcendence here is hard,
state **clean conditional theorems**, and provide **reproducible numeric evidence** (PSLQ scans) — clearly marked as *heuristics*, not proofs.

---

## 🧭 TL;DR
- For any odd prime $\(p\ge 3\)$, write
<p align="center">
  $ Z(p) = e^{c_p\,\pi^p} + 1, $
</p>
  where
  <p align="center">
  $ c_p \;=\; (-1)^{\frac{p+1}{2}}\;\frac{2^{\,p-2}\, B_{p-1}}{p\,(p-1)!}\;\in\;\mathbb{Q}\setminus\{0\},$
  </p>
  and $\(B_{n}\)$ is the $\(n\)-th$ Bernoulli number.
- Proving $\(Z(p)\)$ is transcendental reduces to proving $\(e^{c_p\pi^{p}}\)$ is transcendental.  
  This is **not** settled by standard theorems (LW, Gelfond–Schneider, Baker–Wüstholz).  
- We outline **conditional routes** (Schanuel, Four Exponentials, “π-power Lindemann”) and supply **numerical evidence** via PSLQ with reproducibility.

---

## 🧮 Math snapshot

Using the classical even–zeta formula
<p align="center">
$\zeta(2k)=\frac{(-1)^{k+1} B_{2k}(2\pi)^{2k}}{2(2k)!},$
</p>
let $\(k=(p-1)/2\)$. Then
<p align="center">
$\frac{\pi\,\zeta(2k)}{p} \;=\; \frac{(-1)^{k+1} B_{2k}\,2^{2k-1}\,\pi^{2k+1}}{(2k)!\,(2k+1)} \;=\; c_p\,\pi^{p}.$

Therefore $\(Z(p)=e^{c_p\pi^{p}}+1\)$ with
<p align="center">
$\boxed{\,c_p = (-1)^{\frac{p+1}{2}} \,\frac{2^{\,p-2}\, B_{p-1}}{p\, (p-1)!}\in\mathbb{Q}\,}.$
</p>
**Sanity checks**
<p align="center">
| p | \(c_p\) | Reason |
|---|---------|--------|
| 3 | $\(1/18\)$ | $\(\pi\zeta(2)/3 = \pi^3/18\)$ |
| 5 | $\(1/450\)$ | $\(\pi\zeta(4)/5 = \pi^5/450\)$ |
| 7 | $\(1/6615\)$ | $\(\pi\zeta(6)/7 = \pi^7/6615\) since \(\zeta(6)=\pi^6/945\)$ |
</p>
---

## 🧱 Why this is hard
- **Lindemann–Weierstrass** proves $\(e^{\alpha}\)$ transcendental when $\(\alpha\)$ is **algebraic** and $\(\alpha\neq 0\)$. Here $\(\alpha=c_p\pi^p\)$ is not known to be algebraic (indeed, $\(\pi\)$ is transcendental), so LW **does not apply**.
- **Gelfond–Schneider** concerns $\(a^b\)$ with algebraic $\(a\neq 0,1\)$ and irrational algebraic $\(b\)$ — not our form.
- **Linear forms in logarithms** handle logs of algebraic numbers — again, $\(\pi^p\)$ falls outside their direct scope.

**Takeaway:** Showing $\(e^{c_p\pi^p}\)$ transcendental demands tools beyond current unconditional results.

---

## ✅ What we *can* do now

### Conditional routes (clean implications)
- **(A) π-power Lindemann (hypothetical).** If for all nonzero algebraic $\(q\)$ and integers $\(m\ge 1\)$, $\(e^{q\pi^{m}}\)$ is transcendental, then **all** $\(Z(p)\)$ are transcendental for odd primes $\(p\ge 3\)$.
- **(B) Four Exponentials / Schanuel (conditional).** Under standard independence assumptions, arrange a $\(2\times2\)$ setup with $\(\{1,\pi\}\)$ vs $\(\{c_p,\pi^{p-1}\}\)$ to force transcendence of one of the relevant exponentials and isolate $\(e^{c_p\pi^p}\)$.
- **(C) Periods extension (speculative).** Since $\(\zeta(2k)\)$ are periods, an “LW-for-periods” principle would also settle the case.

### Unconditional numerical evidence (heuristic)
We use **PSLQ** to search for small-degree/height algebraic relations for $\(Z(p)\)$.  
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
  test_cp.py               # Unit tests for $c_p at p=3,5,7$
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
# $Z(p)$ PSLQ scan
# Columns: p, c_p (rational), PSLQ_relation (or None)

p= 3  c_p=1/18     PSLQ=None
p= 5  c_p=1/450    PSLQ=None
...
```
`None` means *no* integer relation among $\([1,x,x^2,\dots,x^{\deg}]\)$ up to `height` was detected at the chosen precision.

---

## 🧪 Testing
```bash
pytest -q
```
The tests verify the closed forms $\(c_3=1/18\)$, $\(c_5=1/450\)$, $\(c_7=1/6615\)$. Add more checks as you extend the program.

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
