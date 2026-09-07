import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

# Configuration
URL = "https://france.diplomatie.belgium.be/fr/services-consulaires/services-consulaires-marseille/missions-flying-kit-marseille"
MOT_CLE = "Montpellier"

# Configuration Email (via variables d'environnement pour la sécurité)
EMAIL_EMETTEUR = os.environ.get("EMAIL_EMETTEUR")
EMAIL_MOT_DE_PASSE = os.environ.get("EMAIL_MOT_DE_PASSE") # Mot de passe d'application Gmail
EMAIL_RECEPTEUR = os.environ.get("EMAIL_RECEPTEUR")

def verifier_site():
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        reponse = requests.get(URL, headers=headers, timeout=15)
        reponse.raise_for_status()
        
        soup = BeautifulSoup(reponse.text, 'html.parser')
        texte_page = soup.get_text()
        
        if MOT_CLE.lower() in texte_page.lower():
            print(f"[{MOT_CLE}] trouvé sur la page ! Envoi de l'alerte...")
            envoyer_email()
        else:
            print(f"[{MOT_CLE}] non détecté pour le moment.")
            
    except Exception as e:
        print(f"Erreur lors de la vérification : {e}")

def envoyer_email():
    if not all([EMAIL_EMETTEUR, EMAIL_MOT_DE_PASSE, EMAIL_RECEPTEUR]):
        print("Erreur : Les variables d'environnement e-mail ne sont pas configurées.")
        return

    sujet = "⚠️ Alerte Consulat : Nouvelles dates Flying Kit Montpellier !"
    corps = f"Le mot-clé '{MOT_CLE}' a été détecté sur la page du consulat.\n\nVérifiez les dates ici : {URL}"
    
    msg = MIMEText(corps)
    msg['Subject'] = sujet
    msg['From'] = EMAIL_EMETTEUR
    msg['To'] = EMAIL_RECEPTEUR

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as serveur:
            serveur.login(EMAIL_EMETTEUR, EMAIL_MOT_DE_PASSE)
            serveur.send_message(msg)
        print("E-mail d'alerte envoyé avec succès !")
    except Exception as e:
        print(f"Erreur d'envoi de l'e-mail : {e}")

if __name__ == "__main__":
    verifier_site()
