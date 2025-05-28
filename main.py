# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:19:14 2025

@author: Oumaima
"""

from datetime import date
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import os
import pandas as pd
from src.data_scrapper import get_hist_data_from_MarketStack  




def main():
    
    #read API key from .env file
    load_dotenv()
    API_KEY=os.getenv("API_key_market_stack")
    
    # Date d’aujourd’hui
    start = date.today()

    # Date il y a 3 ans
    three_years_ago = start - relativedelta(years=3)

    # Format des dates pour l’API
    start_date_str = start.strftime("%Y-%m-%d")
    end_date_str = three_years_ago.strftime("%Y-%m-%d")
    
    # dans https://www.justetf.com/en/etf-profile.html?isin=IE0002XZSHO1, I found ISIN IE0002XZSHO1   |  WKN A3E1JV   |  Ticker WPEA
    #use of https://marketstack.com/search to find the exact ticker to finc the exact ticker
    # Appel de l'API pour récupérer les données du ticker WPEA.XPAR, 
    df = get_hist_data_from_MarketStack(start_date_str=start_date_str,
                       end_date_str=end_date_str,
                       API_KEY=API_KEY,
                       symbol="WPEA.XPAR")

    # Afficher les 5 premières lignes (ou fais autre chose avec le DataFrame)
    print(df.head())

if __name__ == "__main__":
    main()
