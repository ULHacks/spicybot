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
    if message.author == client.user:
        return
    await message.channel.send("Got a message!")
    if message.content == "12345!":
        await message.channel.send("Once I caught a fish alive!")

client.run(os.environ["BOT_TOKEN"])
