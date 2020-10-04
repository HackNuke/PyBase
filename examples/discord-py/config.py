# PyBase Team | PyBase v0.5.0
# Usage example file (for PyBase v0.5.0 and Discord.py v1.5.0).
# ---------------------------------------------------------------
# NOTE: This example code of a basic discord.py bot was extracted
# from https://discordpy.readthedocs.io/en/latest/quickstart.html

import discord # Lets import discord.py
from pybase_db import PyBase # Lets import the PyBase main class

# ---------- DataBase Declaration -------------------------------
db = PyBase(
    database = "config",
    db_type = "json",
    db_path = "./res/"
)

# ---------- Discord.py Code Starts Here ------------------------
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(db.get("token"))
