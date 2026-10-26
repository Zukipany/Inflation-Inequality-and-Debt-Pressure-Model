# Source code is private. This file shows only its classes and function signatures.

"""
Layer 5: Quantitative Metrics & Stress Classification
"""
import pandas as pd
from config import STRESS_THRESHOLDS


def classify_stress(households: pd.DataFrame, thresholds: dict | None=None) -> pd.DataFrame:
    ...


def purchasing_power_loss(baseline: pd.DataFrame, shocked: pd.DataFrame) -> pd.DataFrame:
    """PPL_h = (RDI_baseline - RDI_shock) / RDI_baseline"""
    ...


def summary_by_group(df: pd.DataFrame) -> pd.DataFrame:
    ...
