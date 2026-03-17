import googleapiclient.discovery

api_service_name = "youtube"
api_version = "v3"

DEVELOPER_KEY = "AIzaSyBgcbvO3WjGStGAofh-rAXlTVOKKQcFs9k"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.search().list(
    part="id, snippet",
    type="video",
    order="date",
    channelId="UCdPhEv5wiw2uK6J0_wkc-RA",
    maxResults=1,
    fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
)

response = request.execute()

print(response)