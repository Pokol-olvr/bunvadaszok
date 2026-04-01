from dateutil import parser
import json

def json_olvaso():
    try:
        print("File megnyitása...")
        with open(r"/home/runner/work/bunvadaszok/bunvadaszok/src/video.json", "r", encoding="utf-8") as file: 
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
        with open(r"/home/runner/work/bunvadaszok/bunvadaszok/src/video.json", "w", encoding="utf-8") as file: 
            file.write(aktualis_json)
        print("Sikeres átírás!")
    except FileNotFoundError as e:
        print(f"Nem találom a filet te bolond: {e}")
    except TypeError as e:
        print(f"Nem megfelelő file-t akarsz megynitni öcskös: {e}")

def date_parse(json):
    json = json_olvaso()
    ido_z = json["items"][0]["snippet"]["publishedAt"]
    ido = parser.parse(ido_z)
    return ido

def osszehasonlito(tarolt_ido, aktualis_ido):
    if tarolt_ido < aktualis_ido:
        True
    else:
        False

