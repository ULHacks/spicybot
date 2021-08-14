import os
import random
import asyncio

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

@client.command(help="Gives a random number")
async def rng(ctx, a: int, b: int):
    number = random.randint(a, b)
    await ctx.send(number)

@client.command(help="Pings a user multiple times with the given message")
async def chant(ctx, member: discord.Member, *, text):
    for _ in range(3):
        await ctx.send(f"{member.mention}: {text}")
        await asyncio.sleep(3)

client.run(os.environ["BOT_TOKEN"])
