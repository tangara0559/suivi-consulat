name: Surveillance Consulat

on:
  schedule:
    # S'exécute automatiquement tous les jours à 8h00 UTC (10h00 heure de Paris en été)
    - cron: '0 8 * * *'
  workflow_dispatch: # Permet de lancer le script manuellement depuis GitHub

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Récupérer le code du dépôt
        uses: actions/checkout@v4

      - name: Configurer Python
        uses: actions/setup-python@v5
        with:
          python-python-version: '3.10'

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install requests beautifulsoup4

      - name: Exécuter le script de surveillance
        env:
          EMAIL_EMETTEUR: ${{ secrets.EMAIL_EMETTEUR }}
          EMAIL_MOT_DE_PASSE: ${{ secrets.EMAIL_MOT_DE_PASSE }}
          EMAIL_RECEPTEUR: ${{ secrets.EMAIL_RECEPTEUR }}
        run: python script_surveillance.py
