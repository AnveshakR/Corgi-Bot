import os
import discord
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import random
import praw

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
REDDIT_ID = os.getenv('CLIENT_ID')
REDDIT_SECRET = os.getenv('CLIENT_SECRET')

client = discord.Client()

reddit = praw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent='corgibot by u/mustangboss8055')

@client.event
async def on_message(message):

    rslash = ''
    if message.author == client.user:
        return

    msg = message.content
    if msg[0:4] == "gib ":
        if (msg.find("corgi") != -1):
            rslash = 'corgi'

        if (msg.find("shibe") != -1):
            rslash = 'shibes'
    
        submissions = reddit.subreddit(rslash).hot()
        post_to_pick = random.randint(1,10)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await message.channel.send(submission.url)
        await message.channel.send("provided by MUSTANGBOSSBOSS <3")

    elif msg.lower() == "who is the best":
        await message.channel.send("Anveshak is the best!")
        
    else:
        pass

client.run(TOKEN)