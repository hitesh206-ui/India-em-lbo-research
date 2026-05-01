"""Illustrative standard vs India-adapted LBO model used in Version 4.0.

This script is intentionally simple and transparent. It is not a valuation
of a real company and should not be used as investment advice. The purpose is
to show how lower leverage, higher cost of debt, and weaker cash sweep change
sponsor returns in an India-adapted LBO structure.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class LBOCase:
    name: str
    entry_ebitda: float = 500.0
    entry_multiple: float = 10.0
    transaction_fees_pct: float = 0.02
    ebitda_cagr: float = 0.12
    fcf_conversion_pre_interest: float = 0.55
    exit_multiple: float = 10.0
    holding_period: int = 5
    initial_debt_ebitda: float = 2.5
    cash_interest_rate: float = 0.13
    cash_sweep_pct: float = 0.45
    regulatory_friction_score: float = 4.0


def run_lbo_case(case: LBOCase) -> Dict[str, float | List[Dict[str, float]]]:
    entry_ev = case.entry_ebitda * case.entry_multiple
    transaction_fees = entry_ev * case.transaction_fees_pct
    initial_debt = case.entry_ebitda * case.initial_debt_ebitda
    sponsor_equity = entry_ev + transaction_fees - initial_debt

    debt = initial_debt
    schedule = []
    for year in range(1, case.holding_period + 1):
        ebitda = case.entry_ebitda * ((1 + case.ebitda_cagr) ** year)
        fcf_before_debt = ebitda * case.fcf_conversion_pre_interest
        interest = debt * case.cash_interest_rate
        repayment_capacity = max(0.0, (fcf_before_debt - interest) * case.cash_sweep_pct)
        repayment = min(debt, repayment_capacity)
        ending_debt = debt - repayment
        schedule.append({
            "year": year,
            "ebitda": ebitda,
            "fcf_before_debt_service": fcf_before_debt,
            "opening_debt": debt,
            "cash_interest": interest,
            "debt_repayment": repayment,
            "ending_debt": ending_debt,
        })
        debt = ending_debt

    year_5_ebitda = schedule[-1]["ebitda"]
    exit_ev = year_5_ebitda * case.exit_multiple
    exit_equity_value = exit_ev - debt
    moic = exit_equity_value / sponsor_equity
    irr = (moic ** (1 / case.holding_period)) - 1

    return {
        "case": case.name,
        "entry_enterprise_value": entry_ev,
        "transaction_fees": transaction_fees,
        "initial_debt": initial_debt,
        "sponsor_equity_contribution": sponsor_equity,
        "year_5_ebitda": year_5_ebitda,
        "exit_enterprise_value": exit_ev,
        "ending_net_debt": debt,
        "exit_equity_value": exit_equity_value,
        "moic": moic,
        "irr": irr,
        "regulatory_friction_score": case.regulatory_friction_score,
        "schedule": schedule,
    }


if __name__ == "__main__":
    standard = LBOCase(
        name="Standard developed-market case",
        initial_debt_ebitda=5.0,
        cash_interest_rate=0.095,
        cash_sweep_pct=0.70,
        regulatory_friction_score=1.5,
    )
    india = LBOCase(
        name="India-adapted case",
        initial_debt_ebitda=2.5,
        cash_interest_rate=0.13,
        cash_sweep_pct=0.45,
        regulatory_friction_score=4.0,
    )

    for result in [run_lbo_case(standard), run_lbo_case(india)]:
        print("\n" + result["case"])
        for key in [
            "entry_enterprise_value",
            "initial_debt",
            "sponsor_equity_contribution",
            "year_5_ebitda",
            "exit_enterprise_value",
            "ending_net_debt",
            "exit_equity_value",
            "moic",
            "irr",
            "regulatory_friction_score",
        ]:
            print(f"{key}: {result[key]:,.4f}")
