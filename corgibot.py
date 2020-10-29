import os
import discord
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import random
import praw
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
REDDIT_ID = os.getenv('CLIENT_ID')
REDDIT_SECRET = os.getenv('CLIENT_SECRET')

client = discord.Client()

reddit = praw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent='corgibot by u/mustangboss8055')

functions = ["corgi", "shibe"]

@client.event
async def on_ready():
    #activity = discord.Game(name = "gib", type = 2)
    #await client.change_presence(status=discord.Status.online, activity=activity)
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
    
        submissions = reddit.subreddit(rslash).new()
        sub_arr=[]
        for i in range(0, 10):
            submission = next(x for x in submissions if not x.stickied)
            if (submission.url.find("i.redd.it") != -1):
                sub_arr.append(submission.url)

        await message.channel.send(random.choice(sub_arr))
        await message.channel.send("provided by MUSTANGBOSSBOSS <3")

    elif msg.lower() == "who is the best":
        arr = ["Anveshak", "Maitreyi"]
        name = random.choice(arr)
        await message.channel.send((name+" is the best!"))
        #await message.channel.send(("Maitreyi is the best!"))

    else:
        pass

client.run(TOKEN)