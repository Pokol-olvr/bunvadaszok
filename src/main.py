import logging
import logging.handlers
import os

from slack_api import post_uzenet
from json_to_text import normalizator
from youtube_api import request1
from comparator import osszehasonlito, json_olvaso, json_atiro, date_parse

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    tarolt_json = json_olvaso()
    aktualis_json = request1()

    tarolt_ido = date_parse(tarolt_json)
    aktualis_ido = date_parse(request1)

    if osszehasonlito(tarolt_ido, aktualis_ido):
        json_atiro(aktualis_json)
        uzenet = json_olvaso()
    else:
        uzenet = "Nincs sajnos új videó :("
        
    uzenet = normalizator()
    
    post_uzenet(uzenet)




