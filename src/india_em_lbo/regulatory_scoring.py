"""Regulatory friction scoring for emerging-market LBOs."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class RegulatoryFactor:
    name: str
    severity: int
    weight: float = 1.0

    def weighted_score(self) -> float:
        if not 1 <= self.severity <= 5:
            raise ValueError("Severity must be between 1 and 5.")
        return self.severity * self.weight


def aggregate_regulatory_score(factors: list[RegulatoryFactor]) -> float:
    """Compute weighted average regulatory-friction score."""
    if not factors:
        return 0.0
    total_weight = sum(f.weight for f in factors)
    if total_weight <= 0:
        raise ValueError("Total weight must be positive.")
    return sum(f.weighted_score() for f in factors) / total_weight
