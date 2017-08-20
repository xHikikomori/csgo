import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from datetime import date
from datetime import datetime

Client = discord.Client() #so the word client is able to be used instead of writing the whole thing
bot_prefix= "/" #set the bots prefix, what ever symbol is used here will need to be put in front of commands
client = commands.Bot(command_prefix=bot_prefix) #so the word client is able to be used instead of writing the whole thing

@client.event #As soon as the bot comes online all this will be ran
async def on_ready():
    csgo = True
    while csgo == True:
        dateSTR = datetime.now().strftime("%H:%M:%S" )
        dateSTR = str(dateSTR)
        for j in range(1,25):
            for i in range(0, 60, 5):
                if j < 10:
                    hour = ("0") + str(j)
                else:
                    hour = str(j)
                if i < 10:
                    minutes = ("0")+str(i)
                else:
                    minutes= str(i)

                time = (hour)+(":")+(minutes)+(":00")
                if dateSTR == time:
                        serverID = discord.utils.get(client.servers, id="192570059447730176")
                        channel = discord.utils.get(serverID.channels, name="CSGO")
                        for i in range(len(channel.voice_members)):
                            if str(channel.voice_members[i].game) != "Counter-Strike Global Offensive":
                                member = channel.voice_members[i]
                                newChannel = discord.utils.get(serverID.channels, name="Naughty Corner")
                                try:
                                    await client.move_member(member, newChannel)
                    
                    
                                except discord.DiscordException:
                                       channelType = channel.type
                                       await client.create_channel(serverID, name="Naughty Corner", type=channelType)

                                newChannel = discord.utils.get(serverID.channels, name="Naughty Corner")
                                await client.move_member(member, newChannel)
                                message = ("<@") + str(member.id)+(">")+(" You have been removed from the CSGO voice channel becuase you aren't playing CSGO, so piss off mate!")
                                textchannel = discord.utils.get(serverID.channels, name="voicechannel")
                                await client.send_message(textchannel, message)

client.run("MzM2NDMxMjU3NTgxOTEyMDY0.DE82AA.PZeFLPjS1nhzZYvGjCCs9eidrGU")        
