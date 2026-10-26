# Source code is private. This file shows only its classes and function signatures.

"""
data_fetcher.py
===============
Embedded Numbeo city rankings (April 2026) + live refresh functions.
Provides build_comparison() for the World Comparison tab.
"""
from __future__ import annotations
import datetime
import math
from typing import Optional
import pandas as pd
import numbeo_client
_FX_FALLBACK: dict[str, float]
_fx_cache: Optional[dict]
_fx_fetched_at: Optional[datetime.datetime]


def get_fx_rates() -> dict[str, float]:
    """Return FX rates to USD. Tries live API; falls back to embedded."""
    ...
_CITIES_RAW = ...
_CONTINENT_MAP = ...
CITY_DETAIL = ...
_COLS = ...
_BASE_DF: Optional[pd.DataFrame]
_BASE_LOADED_AT: Optional[datetime.datetime]
_BASE_DATA_TIME: str
_BASE_SOURCE: str
_RANKINGS_URL = ...


def _build_base_df() -> pd.DataFrame:
    ...


def parse_rankings_html(html: str) -> Optional[pd.DataFrame]:
    """Parse Numbeo's 'Cost of Living Index by City' table (id="t2")."""
    ...


def fetch_rankings_live() -> Optional[pd.DataFrame]:
    """Scrape Numbeo rankings. Returns DataFrame or None on failure."""
    ...


def get_rankings_df(force_refresh: bool=False) -> pd.DataFrame:
    """
    Return city rankings DataFrame.
    Reuses a copy saved in the last 24 hours, else tries a live fetch, then
    falls back to the newest saved copy and finally to the embedded April 2026 data.
    """
    ...


def last_updated() -> str:
    """When the city rankings in use were fetched from Numbeo."""
    ...


def rankings_source() -> str:
    """'live' (fetched just now), 'cache' / 'snapshot' (saved copy) or 'embedded' (April 2026)."""
    ...


def _amortize(principal: float, annual_rate: float, years: int) -> float:
    """Monthly payment for a fixed-rate amortizing loan."""
    ...


def build_comparison(my_city: str, my_country: str, my_income_usd: float, bedrooms: int=1, area_type: str='center', household_size: int=1) -> dict:
    """
    Build a full cost-of-living comparison for a user's profile.

    Parameters
    ----------
    my_city        : user's current city (matched against rankings)
    my_country     : user's current country
    my_income_usd  : monthly net income in USD
    bedrooms       : 1 or 3 (for rent estimation)
    area_type      : 'center' or 'outside'
    household_size : number of people

    Returns
    -------
    dict with keys: my_profile, rankings_df, top10_*, country_summary, recommendation
    """
    ...
