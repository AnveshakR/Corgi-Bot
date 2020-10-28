import os
import discord
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"}
url = ""

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg[0:4] == "gib ":
        if (msg.find("corgi") != -1):
            url = 'https://www.reddit.com/r/corgi/'

        if (msg.find("shibe") != -1):
            url = 'https://www.reddit.com/r/shibes/'
    
    page  = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll("img", {"class":"_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax"})
    choice = random.choice(links)
    src = choice['src']

    await message.channel.send(src)
    await message.channel.send("provided by MUSTANGBOSSBOSS <3")

client.run(TOKEN)