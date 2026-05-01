"""Core LBO metrics and helper functions."""

from __future__ import annotations


def debt_to_ebitda(debt: float, ebitda: float) -> float:
    """Return debt / EBITDA. Raises ValueError if EBITDA is non-positive."""
    if ebitda <= 0:
        raise ValueError("EBITDA must be positive.")
    return debt / ebitda


def enterprise_value(ebitda: float, ev_ebitda_multiple: float) -> float:
    """Calculate enterprise value from EBITDA and EV/EBITDA multiple."""
    if ebitda < 0:
        raise ValueError("EBITDA cannot be negative.")
    return ebitda * ev_ebitda_multiple


def equity_contribution(enterprise_value_amount: float, debt_amount: float, fees: float = 0.0) -> float:
    """Calculate sponsor equity contribution."""
    return enterprise_value_amount + fees - debt_amount


def simple_moic(exit_equity_value: float, initial_equity: float) -> float:
    """Calculate multiple on invested capital."""
    if initial_equity <= 0:
        raise ValueError("Initial equity must be positive.")
    return exit_equity_value / initial_equity


def simple_irr_from_moic(moic: float, holding_period_years: float) -> float:
    """Approximate annualized IRR from MOIC and holding period."""
    if moic <= 0:
        raise ValueError("MOIC must be positive.")
    if holding_period_years <= 0:
        raise ValueError("Holding period must be positive.")
    return moic ** (1 / holding_period_years) - 1
