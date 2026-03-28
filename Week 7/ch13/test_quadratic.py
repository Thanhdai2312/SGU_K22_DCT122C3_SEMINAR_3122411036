import pytest
from quadratic import compute_quadratic_roots

def test_two_distinct_real_roots():
    # Trường hợp 2 nghiệm phân biệt: x^2 - 3x + 2 = 0 => x=1, x=2
    roots = compute_quadratic_roots(1, -3, 2)
    assert set(roots) == {1.0, 2.0}

def test_one_real_root():
    # Trường hợp nghiệm kép: x^2 - 2x + 1 = 0 => x=1
    roots = compute_quadratic_roots(1, -2, 1)
    assert roots == (1.0, 1.0)

def test_complex_roots():
    # Trường hợp vô nghiệm: x^2 + x + 1 = 0
    with pytest.raises(ValueError, match="Phương trình vô nghiệm"):
        compute_quadratic_roots(1, 1, 1)

def test_a_is_zero():
    # Trường hợp a = 0 (Không phải phương trình bậc 2)
    with pytest.raises(ValueError, match="Hệ số 'a' không được bằng 0"):
        compute_quadratic_roots(0, 1, 1)