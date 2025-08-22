# Z(p) Irrationality & Transcendence — Program Sketch

Define \( Z(p)=e^{\pi \zeta(p-1)/p}+1 = e^{c_p \pi^{p}}+1 \) with \(c_p\in\mathbb{Q}\setminus\{0\}\).

## 1) What existing theorems give (and don't)
- **Lindemann–Weierstrass**: proves \(e^{\alpha}\) transcendental for nonzero **algebraic** \(\alpha\). Here \(\alpha=c_p\pi^{p}\) is not known/algebraic ⇒ LW does **not** apply directly.
- **Gelfond–Schneider**: about \(a^b\) with algebraic \(a\ne 0,1\) and irrational algebraic \(b\). Not applicable.
- **Baker–Wüstholz**: linear forms in logs of algebraic numbers; again not directly applicable to \(\pi^p\).

**Implication:** If \(e^{c_p\pi^p}\) is transcendental, then \(Z(p)\) is transcendental (sum with 1).

## 2) Conditional routes
- **(A) π-power Lindemann (hypothetical).** If for every nonzero algebraic \(q\) and integer \(m\ge 1\), \(e^{q\pi^{m}}\) is transcendental, then \(Z(p)\) is transcendental for all odd primes.
- **(B) Four Exponentials / Schanuel.** Arrange a \(2\\times 2\) matrix with \(\{1,\pi\}\) vs \(\{c_p,\pi^{p-1}\}\) to force transcendence of at least one exponential and isolate \(e^{c_p\pi^{p}}\) under mild independence assumptions.
- **(C) Periods extension (speculative).** Treat \(c_p\pi^p\) via even zeta values (periods) and posit an LW-like statement for exponentials of periods.

## 3) Unconditional partials (evidence, not proofs)
- Special cases \(p=3,5,7\): numerical irrationality evidence via **PSLQ** (bounded degree/height).
- Lower bounds on rational approximation growth prohibit \(Z(p)\) from being a “small” algebraic number for these \(p\) (document limits).

## 4) Barriers
- Deciding algebraicity of \(e^{\beta}\) when \(\beta\) is a nonzero **transcendental** period like \(c_p\pi^p\) is beyond current methods.
- Conjectures (Schanuel, Four/Six Exponentials) would settle the question if true.

## 5) Artifacts in this repo
- Correct derivation of \(c_p\).
- Conditional theorems written precisely.
- Reproducible PSLQ scans with logs.
