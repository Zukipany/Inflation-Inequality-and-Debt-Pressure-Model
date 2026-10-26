# Source code is private. This file shows only its classes and function signatures.

"""
Inflation Inequality & Debt Pressure Model — Streamlit App
Run with:  streamlit run app.py
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time
from config import SCENARIOS, INCOME_GROUPS, SPENDING_SHARES, SPENDING_CATEGORIES, BASELINE_INFLATION, DEBT_PROFILES, DEBT_TERM_YEARS, STRESS_THRESHOLDS, SAVINGS_BUFFER_MONTHS
from household_generator import generate_households
from scenario_runner import run_scenario, compare_scenarios
import dashboard as dash
from world_comparison import build_world_comparison
from location_profile import build_location_simulation_profile
import sandbox_simulator as sbx
GRP_COLOR = ...
TIER_COLOR = ...


def _show_chart(fig):
    """Display a matplotlib figure in Streamlit then close it."""
    ...


def _simple_intro_card(title: str, body: str):
    ...
_ORIGIN_LABEL = ...


def _render_data_status(result: dict, expanded: bool=False):
    """Show where each Numbeo table in the comparison came from, and how old it is."""
    ...


def _render_formatted_table(df: pd.DataFrame, currency_cols=None, pct_cols=None, round_cols=None):
    ...


def _active_simulation_profile() -> dict | None:
    ...


def _profile_signature(profile: dict | None) -> str:
    ...


def _chart_story(title: str, body: str):
    ...


def _render_active_model_summary():
    ...


def _current_local_inputs() -> dict | None:
    ...


def _ensure_baseline_defaults():
    ...


def _run_local_baseline_analysis(force_refresh: bool=False):
    ...


def _closest_income_group(monthly_income_usd: float) -> str:
    ...


def _local_crisis_signal(profile: dict) -> tuple[str, str]:
    ...


def _compute_user_sim_metrics(scenario_df: pd.DataFrame, scenario_key: str | None=None) -> dict | None:
    """
    Compute where the logged-in user sits in a given scenario.
    scenario_key is used to apply the correct inflation / income deltas to
    the user's own numbers so the per-scenario table shows real changes.
    Returns None if no local baseline is set.
    """
    ...
_TIER_EMOJI = ...
_TIER_COLOR_CSS = ...


def _render_user_position_card(heading: str, u: dict, extra_lines: list[str] | None=None):
    """Show a clearly-formatted 'where you are' card using Streamlit-native components."""
    ...


def _render_local_crisis_snapshot(include_simulation_context: bool=False):
    ...


def _render_global_local_baseline():
    ...


def _render_world_comparison():
    ...


def _plain_language_intro():
    ...


def _explanation_subtabs():
    ...


def _run_simulation(n, seed, selected):
    """Run the full simulation pipeline and cache results in session_state."""
    ...
