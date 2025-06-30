import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7705600136:AAFjdIL8loK0FoefwJ8bHbZUJ3C1gzw5BbE")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25570420"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6591643fa39b5b9d0eb78cb24db17f69")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7552584508"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://right90:XPiKRe1KVae8sO0z@cluster0.hzctsrh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
