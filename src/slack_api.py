import os
import requests

try:
    webhook_url = os.environ.get("SLACK_WEBHOOK")
except OSError as e:
    print(f"Nem találom a kulcsot: {e}")

def post_uzenet(adat): 
    print("Üzenet küldése...")

    payload = {
        'text':adat
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(
            webhook_url,
            json=payload,
            headers = headers
        )
        response.raise_for_status()
        print(f"Sikeres üzenetküldés!\n{response}")
    except requests.ConnectionError as e:
        print(f"Sikertelen üzenetküldés: {e}")
    
