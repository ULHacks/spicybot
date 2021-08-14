import os

import dotenv
import discord
import discord.ext.commands as commands

dotenv.load_dotenv()

client = commands.Bot(command_prefix="!")

@client.listen()
async def on_ready():
    print(f"Bot logged in as {client.user.name}")

@client.listen()
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("Got a message!")

@client.command(name="12345", help="Continues the nursery rhyme")
async def nursery_rhyme(ctx):
    await ctx.message.channel.send("Once I caught a fish alive!")

client.run(os.environ["BOT_TOKEN"])
