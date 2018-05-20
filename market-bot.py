import discord
import asyncio
import random
import time
import json
import yaml

client = discord.Client() 

def loadwordlist(wordlistfile):
    wordlist = []
    for line in wordlistfile:
        wordlist.append(line)
    return wordlist

#load config.yaml
config = yaml.load(open("./config.yaml"))["config"]
wordList = config["wordList"]
help = config["help"]
git = config["git"]
todo = config["todo"]
super = config["super"]
manres = config["manres"] 
tip = config["tip"]
token=open(config["tokenfile"]).read()

#load banned words list file
bannedWords = loadwordlist(config["bannedWordsfile"])

# Only owner has access to certain commands
ownerID = config["ownerID"]

@client.event 
async def on_ready():
    print(config["banner"]) 

maxResponses = config["maxResponses"]
timeFrameWindow = config["timeFrameWindow"]
lastMessageTimes = []

def shouldPrint():
    currentTime = time.time()

    global lastMessageTimes
    # remove any messages that haven't occured in the last timeFrameWindow seconds
    lastMessageTimes = [x for x in lastMessageTimes if not currentTime - x > timeFrameWindow]

    # check if we've had over maxResponses in the last timeFrameWindow
    return not len(lastMessageTimes) >= maxResponses

@client.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return

    if not shouldPrint():
        print("Ignoring messages, have responded too many times in timeframe")
        return
    
    # convert it to lower
    msg = message.content.lower()

    # check if message incl. banned words. if so, spit a response
    if any(word.lower() in msg for word in bannedWords):
        await client.send_message(message.channel, message.author.mention + " " + random.choice(wordList))
    elif msg == "^help":
        await client.send_message(message.channel, message.author.mention + " " + help)
    elif msg == "^git":
        await client.send_message(message.channel, message.author.mention + " " + git)
    elif msg == "^todo":
        await client.send_message(message.channel, message.author.mention + " " + todo)
    #commmand which can only be run by person whose user id matches this one here
    elif msg == "^super" and message.author.id == ownerID:
        await client.send_message(message.channel, message.author.mention + " " + super)
    # command to manually warn person
    elif msg.startswith("^warn") and message.author.id == ownerID:
        await client.send_message(message.channel, message.mentions[0].mention + " " + manres)
    elif msg == "^tip":
        await client.send_message(message.channel, message.author.mention + " " + tip)
    else:
        return

    # Add current message time (if we actually sent a message)
    lastMessageTimes.append(time.time())

client.run(token)
