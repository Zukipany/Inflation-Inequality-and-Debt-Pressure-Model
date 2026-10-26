# Source code is private. This file shows only its classes and function signatures.

"""
numbeo_client.py
================
One place for every request to numbeo.com.

Numbeo gives free users a monthly page budget per page type. Once it is spent
it answers with an "Access Restricted" page (HTTP 429 with a Retry-After date).
This module:

  • stops requesting a page type until its Retry-After date once Numbeo says so
    (remembered on disk, so restarting the app does not hammer Numbeo again),
  • keeps every successful result in .cache/numbeo_cache.json and reuses it for
    24 hours instead of downloading the same tables on every page load,
  • falls back to the committed snapshot in data/numbeo_snapshot.json.
"""
from __future__ import annotations
import datetime as dt
import json
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse
import requests
USER_AGENT = ...
MAX_AGE_SECONDS = ...
_ROOT = ...
_CACHE_FILE = ...
_SNAPSHOT_FILE = ...
_state: Optional[dict]
_snapshot: Optional[dict]


class NumbeoRestricted(Exception):
    """Numbeo refused the page (free monthly limit reached for this page type)."""


def _now() -> dt.datetime:
    ...


def _read_json(path: Path) -> dict:
    ...


def _cache_state() -> dict:
    ...


def _snapshot_entries() -> dict:
    ...


def _save() -> None:
    ...


def _page_type(url: str) -> str:
    """'/cost-of-living/in/Berlin' and '/cost-of-living/in/Sofia' share one budget."""
    ...


def blocked_until(url: Optional[str]=None) -> Optional[dt.datetime]:
    """When Numbeo will serve this page type again (or the latest block of any type)."""
    ...


def get_html(url: str, timeout: int=12) -> str:
    ...


def put(key: str, value: Any) -> None:
    ...


def cached(key: str) -> Optional[dict]:
    """
    The newest stored copy of `key`:
    {"value": ..., "fetched_at": datetime, "age_seconds": float, "origin": "cache" | "snapshot"}
    """
    ...


def is_fresh(entry: Optional[dict]) -> bool:
    ...


def describe(entry_or_time: Any) -> str:
    """'21 Oct 2026 23:31' in local time, for the UI."""
    ...
