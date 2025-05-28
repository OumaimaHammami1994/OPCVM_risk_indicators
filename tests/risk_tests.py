# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:19:14 2025

@author: Oumaima
"""

import pandas as pd
import numpy as np
from datetime import datetime
from src.risk_indicators import get_risk_stats  

# Génération d'un DataFrame de test
def create_test_df():
    dates = pd.date_range(start="2020-01-01", periods=5)
    prices = [100, 105, 110, 108, 107]
    return pd.DataFrame({'date': dates, 'close': prices})

def test_performance():
    df = create_test_df()
    min_date = datetime(2019, 12, 31).date()
    max_date = datetime(2021, 1, 1).date()

    result = get_risk_stats(df, 'performance', min_date, max_date)
    expected = (107 / 100) - 1  # = 0.07

    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"


def test_volatility():
    df = create_test_df()
    min_date = datetime(2019, 12, 31).date()
    max_date = datetime(2021, 1, 1).date()

    result = get_risk_stats(df, 'vol', min_date, max_date)
    expected = np.std([100, 105, 110, 108, 107], ddof=1)

    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"
