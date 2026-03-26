import requests

try:
    import_file = r"/home/runner/work/bunvadaszok/bunvadaszok/src/slack_token.txt"
    with open(import_file,"r") as file:
        webhook_url = file.read()    
    print("Üzenet küldése...")
except FileExistsError as e:
    print(f"Nem létezik megnyitni kívánt file: {e}")
except FileNotFoundError as e:
    print(f"Nem található meg a megnyitni kívánt file: {e}")

def post_uzenet(adat): 
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
    
