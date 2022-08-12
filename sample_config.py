import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1996499923:AAGVCjT4msY1AOHb-qtalwMsrwu0dD65k7g")

    APP_ID = int(os.environ.get("APP_ID", "3335796"))
    
    API_HASH = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600
    
    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://abirhasan2005:abirhasan@cluster0.lb2tp.mongodb.net/cluster0?retryWrites=true&w=majority")

    UPDATE_GROUP = os.environ.get("UPDATE_GROUP", "dlchinhub")
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "irbotz")

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "128"))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "763990585").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
