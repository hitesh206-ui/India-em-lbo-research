from india_em_lbo.regulatory_scoring import RegulatoryFactor, aggregate_regulatory_score


def test_regulatory_score():
    factors = [
        RegulatoryFactor("financial assistance", 4, 0.4),
        RegulatoryFactor("foreign borrowing restrictions", 3, 0.3),
        RegulatoryFactor("exit uncertainty", 2, 0.3),
    ]
    score = aggregate_regulatory_score(factors)
    assert round(score, 2) == 3.1
