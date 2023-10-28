
import os

class Config(object):
    # get a token from @BotFather
    USER_SESSION = os.environ.get("USER_SESSION", "")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    AUTH_USERS = os.environ.get("OWNER", "")

