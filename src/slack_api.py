import requests


import_file = r"C:\pityon100\valami\src\slack_token.txt"

with open(import_file,"r") as file:
    webhook_url = file.read()

answer = "Titkosítás pipa!"

payload = {
    'text':answer
}

response = requests.post(
    webhook_url,
    json=payload,
    headers={'Content-type': 'appliaction/json'}
)

