import requests

def post_uzenet(adat): 
    payload = {
        'text':adat
    }
    headers = {'Content-Type': 'application/json'}

    try:
        import_file = r"C:\pityon100\valami\src\slack_token.txt"
        with open(import_file,"r") as file:
            webhook_url = file.read()    
        print("Üzenet küldése...")

        response = requests.post(
            webhook_url,
            json=payload,
            headers = headers
        )
        response.raise_for_status()
        print(f"Sikeres üzenetküldés!\n{response}")
    except requests.ConnectionError as e:
        print(f"Sikertelen üzenetküldés: {e}")
    
