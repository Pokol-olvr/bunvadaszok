from dateutil import parser
from pathlib import Path
import json

main = Path(__file__) 
src = main.parent
json_utvonal = src / "video.json"

def json_olvaso():
    try:
        print("File megnyitása...")
        with open(json_utvonal, "r", encoding="utf-8") as file: 
            data = json.load(file)
        print("Sikeres megnyitás!")
        return data
    except FileNotFoundError as e:
        print(f"Nem találom a filet te bolond: {e}")
    except TypeError as e:
        print(f"Nem megfelelő file-t akarsz megynitni öcskös: {e}")

def json_atiro(aktualis_json):
    try:
        print("File átírása...")
        with open(json_utvonal, "w", encoding="utf-8") as file: 
            file.write(json.dumps(aktualis_json, indent=4,separators=(", ", ": "),ensure_ascii=False))
        print("Sikeres átírás!")
    except FileNotFoundError as e:
        print(f"Nem találom a filet te bolond: {e}")
    except TypeError as e:
        print(f"Nem megfelelő file-t akarsz megynitni öcskös: {e}")

def date_parse(nyers_json):
    ido_z = nyers_json["items"][0]["snippet"]["publishedAt"]
    ido = parser.parse(ido_z)
    return ido

def osszehasonlito(tarolt_ido, aktualis_ido):
    if tarolt_ido < aktualis_ido:
        return True
    else:
        return False
