# Source code is private. This file shows only its classes and function signatures.

"""
Inflation Inequality & Debt Pressure Model
===========================================
Main orchestrator — generates households, runs all scenarios,
prints summary tables, model explanation, and produces 15 charts.

Usage:
    python main.py
    python main.py --report-only
    python main.py --n 50000
    python main.py --scenarios food_shock rate_hike
    python main.py --no-explain     (skip the long explanation block)
"""
import argparse
import os
import subprocess
import sys
import time
import webbrowser
from config import INCOME_GROUPS, SPENDING_SHARES, SPENDING_CATEGORIES, BASELINE_INFLATION, DEBT_PROFILES, DEBT_TERM_YEARS, HOUSEHOLD_SIZE, SAVINGS_BUFFER_MONTHS, STRESS_THRESHOLDS, SCENARIOS, N_HOUSEHOLDS
from household_generator import generate_households
from scenario_runner import run_scenario, compare_scenarios
from metrics import summary_by_group
from dashboard import generate_all_charts


def _hr(char='─', width=80):
    ...


def _section(title):
    ...


def print_summary_table(label: str, summary):
    ...


def print_model_explanation():
    ...


def main():
    ...


def launch_dashboard(host: str, port: int, open_browser: bool=True):
    ...


if __name__ == '__main__':
    ...
