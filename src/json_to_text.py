from youtube_api import request1
from dateutil import parser

test = {
    "items":[
            {
            "id":{
                "videoId":"JWZPRAGhCfs"
                },
            "snippet":{
                "publishedAt":"2026-03-15T17:00:06Z",
                "channelId":"UCdPhEv5wiw2uK6J0_wkc-RA",
                "title":"🚧PE**FIL⚡️ÁLLATKÍNZÓ rém 🚧",
                "description":"Egy eszelős pe**fil állatkínzóóhoz kopogtatott be a Bűnvadászok Állatvédelmi akciócsapata, aki ellen a hatóságok tehetetlenek.",
                "channelTitle":"BŰNVADÁSZOK"
                }
            }
        ]
    }

def normalizator():
    nyers_json = request1()

    csatorna_neve = nyers_json["items"][0]["snippet"]["channelTitle"]
    video_neve = nyers_json["items"][0]["snippet"]["title"]
    leiras = nyers_json["items"][0]["snippet"]["description"]
    feltoltes_datum_ido_z = nyers_json["items"][0]["snippet"]["publishedAt"]
    normalizalt_datum = parser.parse(feltoltes_datum_ido_z)

    return f"{csatorna_neve}\n{video_neve}\n{leiras}\n{normalizalt_datum}"
