# PyBase Team | PyBase v1.0.0
# Usage example file (for PyBase v1.0.0 and Discord.py v1.5.0).
# ---------------------------------------------------------------
# NOTE: This is a modified example code of a basic discord.py bot
# that was extracted from
# https://discordpy.readthedocs.io/en/latest/quickstart.html

import discord  # Lets import discord.py

from pybase_db import PyBase  # Lets import the PyBase main class

# ---------- DataBase Declaration -------------------------------
db = PyBase(database="config", db_type="yaml")

# ---------- Discord.py Code Starts Here ------------------------
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    prefix = db.get('prefix')

    if message.author == client.user:
        return
    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!')


client.run(db.get("token"))
