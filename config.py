#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "26069929")
API_HASH = os.environ.get("API_HASH", "b0551dd4dd9e81b47fe6aa92173aff24")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7914035563:AAFEXPFGBPfkJlu-7TMj5_i258zlXLoolKA")
ADMIN = int(os.environ.get("ADMIN", '6586630448'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "PythonBotz")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "offchats")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://UPLOADXPRO24BOT:UPLOADXPRO24BOT@cluster0.hjfk60f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "HAMZAX")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002154446015')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://telegra.ph/file/a8e6aef1e2e383e68e122-3f263288e18b91f679.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '6586630448'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002527850870)
