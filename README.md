# OPCVM_risk_indicators
Le but de ce projet est de récupérer l'historique de prix d'un OPCVM (IE0002XZSH01) sur une source publique et de calculer pour différence periodes différents indicateurs (Performance, Volatilité, Rendement espéré, Max Drawdown) et les exporter en sous forme structurée.

## Table des matières
- Requirements
- Installation
- Struture du projet
- Usage

## Requirements
Python 3.8.8

Please find below the justification for some requirements:
dotenv to call the API key for scrapping from .env file
python-dateutil for delta on dates
requests for API


## Installation


```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```
- Créer fichier .env 
- Créer un compte dans https://marketstack.com/dashboard et récupérer le Your API Access Key
- Ajouter l'API Access Key dans .env

## Struture du projet

.
├── main.py                  # Script principal pour lancer le pipeline d'analyse
├── src/
│   ├── data_scrapper.py     # Module de collecte des données financières (web scraping ou API)
│   └── risk_indicators.py              # Fonctions de calcul des indicateurs de risque (volatilité, drawdown, etc.)
├── data/                    # Dossier de stockage des données brutes et des résultats générés (CSV, etc.)
├── notebooks/               # Pour hébérger les notebook de tests
├── tests/                   # Pour les tests unitaires
└── README.md                # Documentation du projet



## Usage
ce script va te générer les indicateurs de risque  (Performance, Volatilité, Rendement espéré, Max Drawdown) dans un csv dans le dossier data

```bash
python main.py
```

If futur modifications, ensure to have full coverage of the tests by 

```bash
pytest tests\risk_tests.py
```
