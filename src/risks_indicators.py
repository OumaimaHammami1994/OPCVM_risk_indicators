# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:19:14 2025

@author: Oumaima
"""

import numpy as np

def get_risk_stats(df, indicator: str, min_date, max_date) -> float:
    """
    Calcule différents indicateurs financiers sur une période donnée à partir du DataFrame global `df`.

    Paramètres :
    - indicator : str, le nom de l'indicateur à calculer ('vol', 'performance', 'rendement espéré', 'max dropdown')
    - min_date : date de début de la période (exclue)
    - max_date : date de fin de la période (exclue)

    Retour :
    - float : la valeur de l'indicateur, ou None si l'indicateur est inconnu
    """
    
    # Filtrer les données entre min_date et max_date
    cond_inf = (df['date'].dt.date > min_date)
    cond_sup = (df['date'].dt.date < max_date)
    sub_df = df.loc[cond_inf & cond_sup, :]

    if indicator == 'vol':
        # Volatilité = écart-type des prix de clôture
        return sub_df['close'].std()

    elif indicator == 'performance':
        # Performance = variation relative entre le 1er et le dernier prix
        return (sub_df['close'].iloc[-1] / sub_df['close'].iloc[0]) - 1

    elif indicator == 'rendement espéré':
        # Calcul des rendements log
        log_returns = np.log(sub_df['close'] / sub_df['close'].shift(1))
        # Moyenne des rendements journaliers (supposés réguliers ici)
        mean_daily_return = log_returns.mean()
        # Annualisation : ici on multiplie par le nombre d'observations (≈ nombre de jours)
        expected_annual_return = mean_daily_return * log_returns.shape[0]
        return expected_annual_return

    elif indicator == 'max dropdown':
        # Série du maximum cumulé des prix
        running_max = sub_df['close'].cummax()
        # Drawdown = écart relatif entre le prix courant et le max précédent
        drawdown = (sub_df['close'] - running_max) / running_max
        # Max drawdown = drawdown le plus bas (plus forte perte)
        max_drawdown = drawdown.min()
        return max_drawdown

    else:
        print('Unknown indicator')
        return None
