import googleapiclient.discovery
from googleapiclient.errors import HttpError


import_file = r"C:\pityon100\valami\src\key.txt"
with open(import_file,"r") as api_key:
    secret = api_key.read()
    print(secret)

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = secret

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

request1()
