import os
import discord
from dotenv import load_dotenv
import requests
import random
import praw
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
REDDIT_ID = os.getenv('CLIENT_ID')
REDDIT_SECRET = os.getenv('CLIENT_SECRET')

client = commands.Bot(command_prefix = "gib")

reddit = praw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent='corgibot by u/mustangboss8055')

functions = ["corgi", "shibe", "puggy", "cat"]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="gib"))


@client.event
async def on_message(message):

    rslash = ''
    if message.author == client.user:
        return

    msg = message.content
    if msg[0:4] == "gib ":

        if (msg.find("help") != -1):
            await message.channel.send("Use gib followed by: ")
            for i in functions:
                await message.channel.send(i)
            return

        if (msg.find("corgi") != -1):
            rslash = 'corgi'

        if (msg.find("shibe") != -1):
            rslash = 'shibes'

        if (msg.find("puggy") != -1):
            rslash = 'pugs'

        if (msg.find("cat") != -1):
            rslash = 'cat'

        submission = ''
        while(1):
            submission = reddit.subreddit(rslash).random()
            if (submission.url.find("i.redd.it") != -1):
                break

        embed = discord.Embed(
            title = "Here is your chonk!",
            color = discord.Colour(0x7289DA)
        )
        embed.set_image(url=submission.url)
        embed.set_footer(text="Provided by Anveshak <3")

        await message.channel.send(embed = embed)

        #await message.channel.send(submission.url)
        #wait message.channel.send("provided by MUSTANGBOSSBOSS <3")

    elif msg.lower() == "who is the best":
        arr = ["Anveshak", "Maitreyi"]
        name = random.choice(arr)
        await message.channel.send((name+" is the best!"))
        #await message.channel.send(("Maitreyi is the best!"))

    else:
        pass

client.run(TOKEN)
