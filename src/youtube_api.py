import googleapiclient.discovery
from googleapiclient.errors import HttpError

def file_olvaso():
    try:
        import_file = r"/src/google_api.txt"
        with open(import_file,"r") as api_key:
            secret = api_key.read()
            return secret
    except FileExistsError as e:
        print(f"Nem létezik megnyitni kívánt file: {e}")
    except FileNotFoundError as e:
        print(f"Nem található meg a megnyitni kívánt file: {e}")

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = file_olvaso()

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

def request1():
    try:
        print("Hívás indítása...")
        request = youtube.search().list(
            part="id, snippet",
            type="video",
            order="date",
            channelId="UCdPhEv5wiw2uK6J0_wkc-RA",
            maxResults=1,
            fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
        )
        print(f"A hívás sikeres volt!")
        response = request.execute()
        return response
    except HttpError as e:
        print(f"Nem sikerült a hívás: {e}")


