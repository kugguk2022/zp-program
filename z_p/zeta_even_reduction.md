# Reduction of the exponent for \( Z(p) \)

For prime \(p\ge 3\) set \(k=(p-1)/2\). Using the standard even-zeta formula
\[\zeta(2k)=\frac{(-1)^{k+1} B_{2k} (2\pi)^{2k}}{2(2k)!},\]
we obtain
\[\frac{\pi\,\zeta(2k)}{p}
= \frac{(-1)^{k+1} B_{2k} \, 2^{2k-1}\, \pi^{2k+1}}{(2k)!\,(2k+1)}.\]

Since \(2k+1=p\) and \(2k=p-1\), this equals \(c_p \pi^{p}\) with
\[\boxed{~c_p = (-1)^{\frac{p+1}{2}} \,\frac{2^{\,p-2}\, B_{p-1}}{p\, (p-1)!} \in \mathbb{Q}~}.\]

**Sanity checks**
- \(p=3\): \(c_3=\frac{1}{18}\) because \(\pi\zeta(2)/3 = \pi^3/18\).
- \(p=5\): \(c_5=\frac{1}{450}\) because \(\pi\zeta(4)/5 = \pi^5/450\).
- \(p=7\): \(c_7=\frac{1}{6615}\) because \(\pi\zeta(6)/7 = \pi^7/6615\) (since \(\zeta(6)=\pi^6/945\)).
