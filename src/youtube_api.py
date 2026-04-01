import os 
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

try:
    secret = os.environ.get("YOUTUBE_API_KEY")
except OSError as e:
    print(f"Nem találom a kulcsot: {e}")
    
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
        response = request.execute()
        print("A hívás sikeres volt!")
        return response
    except HttpError as e:
        print(f"Nem sikerült a hívás: {e}")

uzenet = request1()

print(uzenet)