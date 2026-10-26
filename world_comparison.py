# Source code is private. This file shows only its classes and function signatures.

"""
world_comparison.py
===================
Live-friendly global city and country comparison helpers for the Streamlit app.
Uses Numbeo public tables and falls back to embedded data where live fetches fail.
"""
from __future__ import annotations
import datetime as dt
import re
import unicodedata
from typing import Optional
import pandas as pd
from bs4 import BeautifulSoup
import numbeo_client
from data_fetcher import CITY_DETAIL, get_fx_rates, get_rankings_df, last_updated, rankings_source
from numbeo_client import NumbeoRestricted
_TTL_SECONDS = ...
_CACHE: dict[str, tuple[dt.datetime, pd.DataFrame]]
_CITY_PAGE_CACHE: dict[str, tuple[dt.datetime, Optional[dict]]]
_FRAME_ORIGIN: dict[str, tuple[str, str]]
_CITY_QUALITY_URL = ...
_COUNTRY_COST_URL = ...
_COUNTRY_QUALITY_URL = ...
_PRICE_ITEMS = ...
_NYC_BASE = ...
_COUNTRY_COLUMNS = ...
_COUNTRY_QUALITY_COLUMNS = ...
_SOURCES = ...


def _norm(text: str) -> str:
    ...


def _city_key(city: str, country: str) -> str:
    ...


def _country_key(country: str) -> str:
    ...


def _extract_number(text: str) -> Optional[float]:
    ...


def _get_html(url: str) -> str:
    ...


def _largest_table_rows(html: str) -> list[list[str]]:
    ...


def _split_city_country(label: str) -> tuple[str, str]:
    ...


def _fetch_cached_frame(cache_key: str, builder, force_refresh: bool=False) -> pd.DataFrame:
    """
    In-process cache → saved copy younger than 24h → live fetch → any saved copy.
    Every live result is saved to disk so the next start does not download it again.
    """
    ...


def _parse_rankings_rows(rows: list[list[str]], level: str, kind: str) -> pd.DataFrame:
    ...


def _fetch_city_quality_df(force_refresh: bool=False) -> pd.DataFrame:
    ...


def _fetch_country_cost_df(force_refresh: bool=False) -> pd.DataFrame:
    ...


def _fetch_country_quality_df(force_refresh: bool=False) -> pd.DataFrame:
    ...


def _fetch_price_df(level: str, force_refresh: bool=False) -> pd.DataFrame:
    ...
_CITY_PAGE_ITEMS = ...


def _city_page_slugs(city: str, country: str) -> list[str]:
    """Numbeo URL slugs to try: 'Berlin', then 'Portland-OR' / 'Valencia-Spain' style."""
    ...


def _parse_city_page(html: str, country: str) -> Optional[dict]:
    ...


def fetch_city_prices(city: str, country: str, force_refresh: bool=False) -> Optional[dict]:
    """
    Real prices for one city from its public Numbeo page, in USD.
    Returns {column: value, "_last_update": "20 October 2026", "_url": ...} or None.
    """
    ...


def _nyc_base(force_refresh: bool=False) -> tuple[dict, Optional[dict]]:
    """
    Numbeo indices are relative to New York City (= 100). Anchor every index-based
    estimate on NYC's real prices when its page (or a saved copy) is available,
    else on the embedded April 2026 values. Returns (base, NYC page data or None).
    """
    ...


def _anchor_on_city(base: dict, prices: dict, row: pd.Series) -> dict:
    """
    Turn one city's real prices into New-York-equivalent values, so that the
    usual "NYC price × index / 100" reproduces that city exactly and scales every
    other city relative to it. Anchoring on your own city keeps the comparison
    consistent with the place everything is compared against, and avoids leaning
    on New York prices that may be months old.
    """
    ...


def _overlay_city_prices(df: pd.DataFrame, city: str, country: str, prices: dict) -> pd.DataFrame:
    """Write a city's real Numbeo prices over its index-based estimates."""
    ...


def _monthly_school_cost(children: int, private_school: bool, row: pd.Series) -> float:
    ...


def _household_grocery_base(adults: int, children: int) -> float:
    ...


def _household_discretionary_base(adults: int, children: int) -> float:
    ...


def _housing_size_sqm(bedrooms: int, housing_type: str) -> float:
    ...


def _pick_rent(row: pd.Series, bedrooms: int, area_type: str) -> float:
    ...


def _amortize(principal: float, annual_rate_pct: float, years: int) -> float:
    ...


def _affordability_label(burden_pct: float) -> str:
    ...


def _apply_city_fallbacks(df: pd.DataFrame, nyc: dict) -> pd.DataFrame:
    ...


def _build_city_df(force_refresh: bool=False, nyc: Optional[dict]=None) -> pd.DataFrame:
    ...


def _build_country_df(force_refresh: bool=False, city_df: Optional[pd.DataFrame]=None, nyc: Optional[dict]=None) -> pd.DataFrame:
    ...


def _match_city_row(df: pd.DataFrame, city: str, country: str, allow_country_fallback: bool=True) -> Optional[pd.Series]:
    ...


def _match_country_row(df: pd.DataFrame, country: str) -> Optional[pd.Series]:
    ...


def _compute_metrics(df: pd.DataFrame, my_income_usd: float, adults: int, children: int, bedrooms: int, area_type: str, housing_mode: str, housing_type: str, private_school: bool) -> pd.DataFrame:
    ...


def _apply_livability_filter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove cities/countries that fall below minimum livability thresholds.
    A place is excluded from rankings if:
      - safety_index is known AND < 40 (active conflict, extreme crime), OR
      - quality_of_life_index is known AND < 35, OR
      - col_index < 20 AND safety_index is NA (likely missing data for a fragile state)
    Cities that fail the filter are kept in the full table but flagged so the user
    can see them — they are just not allowed into the Top 10 / ranked lists.
    """
    ...


def _scored(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute a composite 'overall_score' anchored on livability first, then
    financial metrics.  Safety and quality-of-life are first-class components.

    Weights:
      Quality of life  25%  — overall wellbeing, healthcare, climate, traffic
      Safety           20%  — crime, conflict, personal security
      Purchasing power 20%  — how far money goes locally (real wages vs costs)
      Essential cost   15%  — raw affordability of housing + groceries + utilities
      Salary/rent      10%  — local labour market strength vs housing costs
      Mortgage burden  10%  — path to home ownership

    Cities filtered out by _apply_livability_filter() receive a 0.0 score
    regardless of their financial metrics, so they never appear in top-10 lists.
    """
    ...


def _reason(row: pd.Series, current: pd.Series) -> str:
    ...


def _prepare_top10(df: pd.DataFrame, current: pd.Series, level_name: str) -> pd.DataFrame:
    ...


def build_world_comparison(my_city: str, my_country: str, income_amount: float, income_currency: str='USD', income_period: str='monthly', job_title: str='', adults: int=1, children: int=0, housing_mode: str='rent', housing_type: str='apartment', bedrooms: int=1, area_type: str='city center', private_school: bool=False, force_refresh: bool=False, income_mode: str='remote') -> dict:
    ...


def _data_status(city_df: pd.DataFrame, country_df: pd.DataFrame, my_city_overlaid: bool, my_city_prices: Optional[dict], anchor: dict) -> dict:
    """Where every table in this comparison came from, for the UI."""
    ...
