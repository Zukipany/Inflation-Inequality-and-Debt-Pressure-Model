# Source code is private. This file shows only its classes and function signatures.

"""
Location-calibrated simulation profile builder.

This module turns the saved local baseline into a simulation profile that can
drive the synthetic household generator with place-specific income bands,
population weights, spending shares, debt assumptions, and "you vs local"
comparison metadata.
"""
from __future__ import annotations
import copy
import datetime as dt
import math
import re
import unicodedata
from statistics import NormalDist
from typing import Optional
import pandas as pd
import requests
from config import BASELINE_INFLATION, DEBT_PROFILES, DEBT_TERM_YEARS, HOUSEHOLD_SIZE, INCOME_GROUPS, SAVINGS_BUFFER_MONTHS, SPENDING_CATEGORIES, SPENDING_SHARES, STRESS_THRESHOLDS
from data_fetcher import get_fx_rates
from inflation_fetcher import get_inflation_rates
_USER_AGENT = ...
_TIMEOUT = ...
_NORMAL = ...
_EUROSTAT_BASE = ...
_CENSUS_BASE = ...
_EUROSTAT_COUNTRY_CODES = ...
_US_ALIASES = ...
_US_INCOME_BINS = ...
_REQUEST_CACHE: dict[str, dict]


def _norm(text: str) -> str:
    ...


def _clamp(value: float, low: float, high: float) -> float:
    ...


def _equivalence_scale(adults: int, children: int) -> float:
    ...


def _size_equivalence_map() -> dict[int, float]:
    ...


def _normalise_weights(weights: dict[str, float]) -> dict[str, float]:
    ...


def _safe_float(value, default: float=0.0) -> float:
    ...


def _session() -> requests.Session:
    ...


def _json_get(url: str, params: Optional[dict]=None) -> Optional[dict]:
    ...


def _eurostat_value(payload: dict, selections: dict[str, str]) -> Optional[float]:
    ...


def _latest_years() -> list[int]:
    ...


def _fetch_eurostat_series(dataset: str, geo: str, selection: dict[str, str]) -> tuple[Optional[float], Optional[int]]:
    ...


def _fetch_us_census_income_distribution() -> tuple[Optional[dict], Optional[int]]:
    ...


def _cumulative_weight_to_threshold(bins: list[float], target_weight: float) -> float:
    ...


def _weight_below_threshold(bins: list[float], threshold: float) -> float:
    ...


def _eur_to_usd(value_eur: float) -> float:
    ...


def _build_eurostat_distribution(country: str, adults: int, children: int) -> Optional[dict]:
    ...


def _build_us_distribution() -> Optional[dict]:
    ...


def _build_fallback_distribution(world_result: dict) -> dict:
    ...


def _pick_distribution_provider(country: str, world_result: dict) -> dict:
    ...


def _match_local_row(world_result: dict) -> Optional[pd.Series]:
    ...


def _build_anchor_costs(world_result: dict) -> dict[str, float]:
    ...


def _blend_spending_shares(anchor_costs: dict[str, float], provider_level: str) -> dict[str, dict[str, float]]:
    ...


def _bias_household_sizes(world_result: dict) -> dict[str, dict[int, float]]:
    ...


def _derive_savings_buffer(world_result: dict) -> dict[str, dict[str, tuple[float, float]]]:
    ...


def _group_mid_annual_income(income_groups: dict[str, dict]) -> dict[str, float]:
    ...


def _expected_scale_for_group(size_dist: dict[int, float]) -> float:
    ...


def _derive_debt_profiles(world_result: dict, income_groups: dict[str, dict], household_sizes: dict[str, dict[int, float]]) -> dict[str, dict]:
    ...


def _derive_stress_thresholds(world_result: dict) -> dict:
    ...


def _build_group_benchmarks(world_result: dict, income_groups: dict[str, dict], spending_shares: dict[str, dict[str, float]], household_sizes: dict[str, dict[int, float]]) -> pd.DataFrame:
    ...


def _user_income_band(income_groups: dict[str, dict], user_equiv_annual_income: float) -> str:
    ...


def build_location_simulation_profile(world_result: Optional[dict]) -> Optional[dict]:
    ...
