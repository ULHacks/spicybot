import os

import dotenv
import discord

dotenv.load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user.name}")

client.run(os.environ["BOT_TOKEN"])
