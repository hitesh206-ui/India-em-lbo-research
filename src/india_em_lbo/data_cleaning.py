"""Data cleaning utilities for hand-collected LBO datasets."""

from __future__ import annotations
import pandas as pd


REQUIRED_DEAL_COLUMNS = [
    "deal_id",
    "announcement_date",
    "target_name",
    "country",
    "sector",
    "sponsor",
    "deal_type",
]


def validate_deal_dataset(df: pd.DataFrame) -> None:
    """Validate required columns in the deal dataset."""
    missing = [col for col in REQUIRED_DEAL_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def clean_deal_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning for the hand-collected deal dataset."""
    validate_deal_dataset(df)
    out = df.copy()
    out["announcement_date"] = pd.to_datetime(out["announcement_date"], errors="coerce")
    for col in ["target_name", "country", "sector", "sponsor", "deal_type"]:
        out[col] = out[col].astype(str).str.strip()
    return out
