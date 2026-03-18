import requests

def post_uzenet(payload): 

    import_file = r"C:\pityon100\valami\src\slack_token.txt"
    with open(import_file,"r") as file:
        webhook_url = file.read()
    
    try:
        print("Üzenet küldése...")
        response = requests.post(
            webhook_url,
            json=payload,
            headers={'Content-type': 'appliaction/json'}
        )
        print(f"Sikeres üzenetküldés!\n{response}")
    except requests.ConnectionError as e:
        print(f"Sikertelen üzenetküldés: {e}")
