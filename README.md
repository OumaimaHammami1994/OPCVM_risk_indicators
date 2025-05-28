# OPCVM_risk_indicators
Le but de ce projet est de récupérer l'historique de prix d'un OPCVM (IE0002XZSH01) sur une source publique et de calculer pour différence periodes différents indicateurs (Performance, Volatilité, Rendement espéré, Max Drawdown) et les exporter en sous forme structurée.

## Table des matières

- Installation
- Usage

## Installation


```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Créer fichier .env 
- Créer un compte dans https://marketstack.com/dashboard et récupérer le Your API Access Key
- Ajouter l'API Access Key dans .env
## Usage


python main.py

