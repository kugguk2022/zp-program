import sympy as sp
from z_p.experiments.pslq_scan import c_p_rational

def test_cp_p3():
    assert c_p_rational(3) == sp.Rational(1, 18)

def test_cp_p5():
    assert c_p_rational(5) == sp.Rational(1, 450)

def test_cp_p7():
    assert c_p_rational(7) == sp.Rational(1, 6615)
