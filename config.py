# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24692763"))
API_HASH = getenv("API_HASH", "8e3840420e9d0895db3231d87c6d21a5")
BOT_TOKEN = getenv("BOT_TOKEN", "8005393579:AAES8sv0C5NMw_vDJSTHSicCfFvdlqjRCmA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8171835867").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jihehod332:OM69Q4epgIEcN3xk@cluster0.qzw02.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002340534679")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002486629939"))
