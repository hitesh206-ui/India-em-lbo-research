import pytest
from india_em_lbo.lbo_metrics import debt_to_ebitda, enterprise_value, simple_moic, simple_irr_from_moic


def test_debt_to_ebitda():
    assert debt_to_ebitda(500, 100) == 5


def test_enterprise_value():
    assert enterprise_value(100, 12) == 1200


def test_simple_moic():
    assert simple_moic(300, 100) == 3


def test_simple_irr_from_moic():
    irr = simple_irr_from_moic(2, 5)
    assert round(irr, 4) == 0.1487


def test_debt_to_ebitda_invalid():
    with pytest.raises(ValueError):
        debt_to_ebitda(100, 0)
