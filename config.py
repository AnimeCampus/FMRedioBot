import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "6198858059")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 16743442))
    CHAT = int(os.environ.get("CHAT", "-1001905486162"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001905486162")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6377102011:AAE3ltg7QR20ChoH1HaBl6GCbig8xi7yjGc") 
    SESSION = os.environ.get("SESSION_STRING", "")

