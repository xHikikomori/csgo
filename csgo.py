#loads discord and other assets
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from random import randint
import os
import random, os
import subprocess
import time

#/vote stuff
vote = False
voteUser = "blank"
voteUserID = 0
numberOfVotes = 0
voters = []


Client = discord.Client() #so the word client is able to be used instead of writing the whole thing
bot_prefix= "/" #set the bots prefix, what ever symbol is used here will need to be put in front of commands
client = commands.Bot(command_prefix=bot_prefix) #so the word client is able to be used instead of writing the whole thing
cool = True
@client.event #As soon as the bot comes online all this will be ran
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    while cool == True:
        time.sleep(300)
        serverID = discord.utils.get(client.servers, id="337028246413639685")
        textchannel = discord.utils.get(serverID.channels, name="bot-testing")
        try: 
            await client.send_message(textchannel, "/csgo")
        except discord.DiscordException:
            print("Channel permissions disabled")

    
client.run("MzM3MDI4MDIwODAxODk2NDU4.DHrLVA.py6eMf1ySsJktwORRsdYupu2hAE")
