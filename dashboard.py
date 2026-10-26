# Source code is private. This file shows only its classes and function signatures.

"""
Dashboard / Reporting Module
All chart functions return a matplotlib Figure so they can be
displayed in Streamlit (st.pyplot) or saved to disk.
generate_all_charts() handles the file-saving path.
"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from pathlib import Path
OUTPUT = ...
COLORS = ...
STRESS_COLORS = ...
CAT_PALETTE = ...


def _save(fig, name):
    ...


def plot_local_income_ladder(simulation_profile: dict):
    ...


def plot_local_budget_comparison(simulation_profile: dict):
    ...


def plot_inflation_distribution(df: pd.DataFrame):
    ...


def plot_pp_loss_heatmap(results: dict):
    ...


def plot_stress_bars(df: pd.DataFrame, label: str=''):
    ...


def plot_debt_vs_disposable(df: pd.DataFrame):
    ...


def plot_inflation_decomposition(df: pd.DataFrame):
    ...


def plot_scenario_comparison(results: dict):
    ...


def plot_spending_pies(households: pd.DataFrame):
    ...


def plot_debt_composition_pies(households: pd.DataFrame):
    ...


def _stress_pies_figure(df: pd.DataFrame, title: str):
    ...


def plot_stress_pies_baseline(df: pd.DataFrame):
    ...


def plot_stress_pies_worst(df: pd.DataFrame, label: str):
    ...


def plot_income_and_savings(households: pd.DataFrame):
    ...


def plot_burden_boxplots(df: pd.DataFrame):
    ...


def plot_rdi_across_scenarios(results: dict):
    ...


def plot_effective_inflation_heatmap(results: dict):
    ...


def plot_distress_by_scenario(results: dict):
    ...


def generate_all_charts(baseline_df: pd.DataFrame, results: dict, households_raw: pd.DataFrame=None):
    ...
