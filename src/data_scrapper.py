# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:19:14 2025

@author: Oumaima
"""

import requests
import pandas as pd

def get_hist_data_from_MarketStack(start_date_str: str, end_date_str: str, API_KEY: str, symbol : str) -> pd.DataFrame:
    
    """
    Fetches historical end-of-day stock data from the MarketStack API.

    Parameters:
    - start_date_str: str, the start date in 'YYYY-MM-DD' format.
    - end_date_str: str, the end date in 'YYYY-MM-DD' format.
    - API_KEY: str, your MarketStack API key.
    - symbol: str, the symbol of the instrument (https://marketstack.com/search to find the exact ticker)

    Returns:
    - pd.DataFrame: DataFrame containing the historical data.
    """
    
    url = f"https://api.marketstack.com/v1/eod?access_key={API_KEY}"
    # API parameters (max 1000 rows allowed per request)
    querystring = {

        "symbols": symbol,
        "date_from": end_date_str,
        "date_to": start_date_str,
        "limit": 1000
    }

    try:
        # Send GET request to the API
        print(f"Sending request to {url} with params: {querystring}")
        response = requests.get(url, params=querystring)
        response.raise_for_status()  # Raises an error for HTTP codes 4xx or 5xx

        json_response = response.json()

        # Ensure 'data' key exists in response
        if 'data' not in json_response:
            raise ValueError("Missing 'data' key in API response")

        # Convert to DataFrame
        return pd.DataFrame(json_response['data'])

    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

    # Return empty DataFrame in case of failure
    return pd.DataFrame()
