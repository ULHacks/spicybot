import os

import dotenv
import discord

dotenv.load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user.name}")

@client.event
async def on_message(message):
    await message.channel.send("Got a message!")

client.run(os.environ["BOT_TOKEN"])
