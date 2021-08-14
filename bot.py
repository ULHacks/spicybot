import os

import dotenv
import discord

dotenv.load_dotenv()

client = discord.Client()

client.run(os.environ["BOT_TOKEN"])
