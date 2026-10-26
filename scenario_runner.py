# Source code is private. This file shows only its classes and function signatures.

"""
Layer 6: Scenario Pipeline Orchestrator
For each scenario: apply income delta → compute inflation → apply rate shock
→ compute debt metrics → compute purchasing power → classify stress.
"""
from typing import List, Optional
import pandas as pd
from config import SCENARIOS
from inflation_engine import compute_effective_inflation
from debt_engine import apply_rate_shock, compute_debt_metrics
from purchasing_power import compute_purchasing_power
from metrics import classify_stress, purchasing_power_loss, summary_by_group


def run_scenario(households: pd.DataFrame, scenario_key: str, profile: dict | None=None) -> pd.DataFrame:
    """
    Run a single scenario through the full pipeline.
    Returns a fully annotated DataFrame.
    """
    ...


def compare_scenarios(households: pd.DataFrame, scenario_keys: Optional[List[str]]=None, profile: dict | None=None) -> dict:
    """
    Run all (or a subset of) scenarios.
    Always includes 'baseline' as the reference.
    Returns a dict keyed by scenario_key with:
      - label: human-readable name
      - detail: per-household DataFrame (with pp_loss vs baseline)
      - summary: group-level aggregated stats
    """
    ...
