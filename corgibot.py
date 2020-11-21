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

hoes = ["<:woodhoe:779730777112838154>",
        "<:stonehoe:779730777024888873>",
        "<:ironhoe:779730777206161429>",
        "<:goldhoe:779730777200918528>",
        "<:diamondhoe:779730777126076446>",
        "<:netheritehoe:779730776920293407>"]

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

        if (msg.find("hoerate") != -1):
            if(len(message.mentions) == 1):
                name = message.mentions[0].nick
                hoe = random.choice(hoes)
                number = hoes.index(hoe) + 1
                finalhoe = ""
                for i in range (number):
                    finalhoe = finalhoe+hoe+" "
                hoeembed = discord.Embed(
                    title = "Hoe Rater",
                    color = discord.Color(0x7289DA)
                )
                hoeembed.add_field(
                    name = name,
                    value = finalhoe,
                    inline = False
                )
                await message.channel.send(embed = hoeembed)
                return
            else:
                await message.channel.send("Just one person can be hoed at a time!")
                return

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

    elif msg.lower() == "who is the best":
        arr = ["Anveshak", "Maitreyi"]
        name = random.choice(arr)
        await message.channel.send((name+" is the best!"))

    else:
        pass

client.run(TOKEN)
