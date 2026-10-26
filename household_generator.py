# Source code is private. This file shows only its classes and function signatures.

"""
Layer 1: Synthetic Household Generator
Produces a DataFrame of N households with realistic income, spending,
debt, and savings profiles drawn from configured distributions.
"""
import numpy as np
import pandas as pd
from config import INCOME_GROUPS, SPENDING_SHARES, DEBT_PROFILES, DEBT_TERM_YEARS, HOUSEHOLD_SIZE, SAVINGS_BUFFER_MONTHS, N_HOUSEHOLDS, RANDOM_SEED


def _pick_weighted(options: dict, rng: np.random.Generator, size: int) -> np.ndarray:
    ...


def _monthly_payment(balance: float, annual_rate: float, term_years: int) -> float:
    ...


def _equivalence_scale_from_size(size: int, scale_map: dict[int, float] | None=None) -> float:
    ...


def generate_households(n: int=N_HOUSEHOLDS, seed: int=RANDOM_SEED, profile: dict | None=None) -> pd.DataFrame:
    ...


if __name__ == '__main__':
    ...
