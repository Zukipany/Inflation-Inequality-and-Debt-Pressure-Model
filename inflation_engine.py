# Source code is private. This file shows only its classes and function signatures.

"""
Layer 2: Inflation Exposure Engine
Computes household-specific effective inflation rates using
category spending weights × category inflation rates.
"""
import pandas as pd
from typing import Optional
from config import BASELINE_INFLATION, SPENDING_CATEGORIES


def compute_effective_inflation(households: pd.DataFrame, inflation_rates: Optional[dict]=None, baseline_inflation: Optional[dict]=None) -> pd.DataFrame:
    """
    π_h = Σ_i  w_{h,i} · π_i

    Adds columns:
      - effective_inflation: household-specific weighted inflation
      - inflation_contribution_{cat}: how much each category contributes
    """
    ...


def national_cpi(inflation_rates: Optional[dict]=None, baseline_inflation: Optional[dict]=None) -> float:
    """Simple unweighted average CPI for reference."""
    ...
