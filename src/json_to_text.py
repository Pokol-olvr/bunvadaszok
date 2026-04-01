from dateutil import parser

def normalizator(nyers_json: dict) -> str:

    csatorna_neve = nyers_json["items"][0]["snippet"]["channelTitle"]
    video_neve = nyers_json["items"][0]["snippet"]["title"]
    leiras = nyers_json["items"][0]["snippet"]["description"]
    feltoltes_datum_ido_z = nyers_json["items"][0]["snippet"]["publishedAt"]
    normalizalt_datum = parser.parse(feltoltes_datum_ido_z)

    return f"{csatorna_neve}\n{video_neve}\n{leiras}\n{normalizalt_datum}"
