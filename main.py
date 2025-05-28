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
from src.risks_indicators import get_risk_stats


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
    df_hist_data = get_hist_data_from_MarketStack(start_date_str=start_date_str,
                       end_date_str=end_date_str,
                       API_KEY=API_KEY,
                       symbol="WPEA.XPAR")
    
    #conversion de la colonne date en datetime
    df_hist_data.date=pd.to_datetime(df_hist_data.date)
    # Horizons à évaluer
    periods = {
        'YTD': date(date.today().year, 1, 1),
        '3M': date.today() - relativedelta(months=3),
        '6M': date.today() - relativedelta(months=6),
        '1Y': date.today() - relativedelta(years=1),
        '3Y': date.today() - relativedelta(years=3),
    }
    
    # Liste des indicateurs
    indicators = ['vol', 'performance', 'rendement espéré', 'max dropdown']
    
    # Initialiser une liste pour stocker les résultats
    results = []
    
    # Boucle sur chaque période et chaque indicateur
    for label, min_date in periods.items():
        for indicator in indicators:
            value = get_risk_stats(df_hist_data,indicator, min_date, date.today())
            results.append({
                'Période': label,
                'Indicateur': indicator,
                'Valeur': value
            })
    
    # Convertir les résultats en DataFrame
    df_results = pd.DataFrame(results)
    
    # Option : pivot pour avoir un tableau lisible
    df_pivot = df_results.pivot(index='Indicateur', columns='Période', values='Valeur')
    
    df_pivot.to_csv(r'data/IE0002XZSHO1_risk_indicators.csv')

if __name__ == "__main__":
    main()
