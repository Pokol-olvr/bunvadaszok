import googleapiclient.discovery

api_service_name = "youtube"
api_version = "v3"

DEVELOPER_KEY = "AIzaSyBgcbvO3WjGStGAofh-rAXlTVOKKQcFs9k"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.search().list(
    part="id",
    type="video",
    q="Bűnvadászok",
    maxResults=1
)

response = request.execute()

print(response)