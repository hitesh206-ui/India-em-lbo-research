"""Visualization helpers."""

from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def save_sector_count_chart(df: pd.DataFrame, output_path: str | Path) -> None:
    """Save a simple sector count chart."""
    counts = df["sector"].value_counts().sort_values(ascending=True)
    ax = counts.plot(kind="barh")
    ax.set_xlabel("Number of deals")
    ax.set_ylabel("Sector")
    ax.set_title("Buyout / Control Transactions by Sector")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
