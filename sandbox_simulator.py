# Source code is private. This file shows only its classes and function signatures.

"""
sandbox_simulator.py
====================
Custom Risk Sandbox — lets users dial in arbitrary economic shocks and
immediately see what would happen to the simulated population and to
their own personal financial position specifically.

Public API
----------
run_custom_scenario(households, shock_params, profile=None)
    → annotated DataFrame identical to run_scenario() output

compute_user_impact(user_monthly_income_usd, spending_shares, housing_usd,
                    total_debt_payment_usd, debt_variable_fraction,
                    shock_params, baseline_inflation)
    → dict: personal metrics before and after shock

build_sandbox_summary(baseline_df, sandbox_df, user_impact)
    → dict ready for Streamlit rendering
"""
from __future__ import annotations
import math
from typing import Optional
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from config import BASELINE_INFLATION, STRESS_THRESHOLDS, SPENDING_CATEGORIES
DEFAULT_SHOCK: dict[str, float]
SHOCK_LABELS = ...


def run_custom_scenario(households: pd.DataFrame, shock_params: dict[str, float], profile: Optional[dict]=None) -> pd.DataFrame:
    """
    Run a fully custom scenario through the standard 6-stage pipeline.
    shock_params keys follow DEFAULT_SHOCK schema.
    Returns a fully annotated DataFrame.
    """
    ...


def compute_user_impact(user_monthly_income_usd: float, spending_shares: dict[str, float], housing_usd: float, total_debt_payment_usd: float, debt_variable_fraction: float, shock_params: dict[str, float], baseline_inflation: Optional[dict]=None) -> dict:
    """
    Compute before/after financial metrics for a real user given shock_params.

    Returns a dict with keys:
      before / after — each containing:
        monthly_income, effective_inflation, essential_cost,
        debt_payment, dsr, ebr, rdi, stress_tier
      delta — change in each metric
      narrative — plain-English sentences about the impact
    """
    ...


def _classify_tier(dsr: float, ebr: float, rdi: float) -> str:
    ...


def _build_narrative(inc_before, inc_after, inf_before, inf_after, rdi_before, rdi_after, tier_before, tier_after, ess_before, ess_after, debt_before, debt_after) -> list[str]:
    ...


def build_sandbox_summary(baseline_df: pd.DataFrame, sandbox_df: pd.DataFrame, user_impact: Optional[dict]) -> dict:
    """
    Compare baseline vs sandbox simulation and package results for display.
    """
    ...
TIER_COLORS = ...
GROUP_COLORS = ...


def plot_sandbox_stress_comparison(base_summary, sandbox_summary) -> plt.Figure:
    """Side-by-side stress tier bars: baseline vs sandbox."""
    ...


def plot_sandbox_rdi_shift(base_summary, sandbox_summary) -> plt.Figure:
    """Real Disposable Income shift by group, baseline vs sandbox."""
    ...


def plot_sandbox_inflation_breakdown(shock_params: dict, spending_shares_by_group: dict) -> plt.Figure:
    """Show how the shock translates into effective inflation per group."""
    ...


def plot_user_before_after(user_impact: dict) -> plt.Figure:
    """Visual before/after for a single user."""
    ...


def plot_population_percentile_marker(scenario_df: pd.DataFrame, user_rdi: float) -> plt.Figure:
    """Show where the user's RDI sits in the full population distribution."""
    ...
