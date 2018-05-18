import discord
import asyncio
import random
import time
import json

client = discord.Client() 

# list of words which triggers it
bannedWords = ["exchanges", "tradeogre", "sell turtlecoin", "buy turtlecoin", "sell trtl", "buy trtl", "tradesatoshi", "tradesat", 
               "trade-", "pr1ce", "binance", "sats", "to down", "ts down", "tradesatoshi down", "tradeogre down", "ogre down", "sats down", "exhcnage", 
               "hitbtc", "trtl be worth", "trtl worth", "exhcnag,e", "buy wall", "sell wall", "buy order", "sell order", "buy trlt", "sell trlt", 
               "Bitfinex", "Kraken", "Coinbase", "coinone", "Bitstamp", "Bithumb", "Bittrex", "Quoine", "Gemini", "bitFlyer", "BTC-e", "Poloniex", 
               "exx ", "livecoin", "exmo", "korbit", "cex.io", "tidex", "vaultoro", "itbit", "cryptopia", "yobit", "lakebtc", "kucoin", "btc-alpha", 
               "quadrigacx", "localbitcoins", "coinfloor", "bitx", "coinexchange", "okcoin", "gatecoin", "coinmate", "bitso", "acx", "idex", "cryptobridge", 
               "btcc", "bitfex", "virwox", "bleutrade", "abucoins", "paymium",  "flowbtc", "gate.io", "bitkonan", "cryptox", "cryptonit", "go4cryptos", "c-cex",
               "novaexchange", "coincoz", "btctrade", "vircurex", "allcoin", "coinsecure",  "indacoin", "bitmarket", "braziliex", "coinnest", "dsx", 
               "localturtlecoin", "localmonero", "local bitcoin", "local bitcoins", "localbitcoin", "stocks.exchange", "indacion", "indaocin", "satoshis", 
               "trtl sell", "tlt sell", "turtlecoin sell", "trtl buy", "trlt buy", "turtlecoin buy", "1sat", "1 sat", "buy turtle", "sell turtle", "crypto exchange", 
               "cryptocurrency exchange", "crypto currency exchange", "sellin", "buyin", "selin", "sellwall", "buywall", "selwall", " ts", "s@t", "0 sat", "0sat", "0stas", 
               "stas", "st@s", "btc volume", "pr!ce", "binnance", "buy btc", "buy bct", "buy bticoin", "buy bitcion", "buy btiocin", "buy bitocin", "xchange", "exchnage", "xchnage", "bitfenix", "ccex", 
               "exchamge", "bynance", "turtle cost", "cost turtle", "cost of turtle", "trtl price", "price of trtl", "price trtl", "price of turtle", "turtle price",
               "price turtle", "price of rtrl", "coin price", "price of coin", "price coin", "2 sats", "2 sat", "3 sat", "3 sats", "4 sat", "4 sats", "2sat", "3sat", 
               "4sat", "5sat", "5 sat", "6sat", "6 sat", "7sat", "7 sat", "8sat", "8 sat", "9sat", "9 sat", "price of the coin", "price of the trtl", 
               "price of the turtle", "pricce for the coin", "price for the trtl", "price for the turtle", "price for coin", "price for trtl", "price for turtle", 
               "gamble turtle", "gamble trtl", "gamble rtrl", "trtl gamble", "turtle gamble"]

# list of responses
wordlist = ["Heyo, please move to the server linked in <https://tinyurl.com/ybas4twh>, we don't like market talk here.", 
            "If you could move to the server linked in <https://tinyurl.com/ybas4twh>, that'd be great! We don't enjoy market talk here.", 
            "Please move this discussion to the server linked in <https://tinyurl.com/ybas4twh>, we like to keep this server focused on support and development. Thank you! <:t_smile:405478442599972874>",
            ":rotating_light: MARKET TALK DETECTED :rotating_light: Please move to the server linked in <https://tinyurl.com/ybas4twh>, we don't like market talk here. :rotating_light:"]

#help reply
help = "Available commands - `^git` and `^todo`"

# github repo
git = "https://github.com/Sajo811/turtlecoin-market-linker"

# todo list
todo = "https://github.com/Sajo811/turtlecoin-market-linker/projects/1"

# supreme power
super = "WHEN WEB WALLET"

# manual warn's response
manres = "Hey, we don't like market-related talk in here. Join the server linked in <https://tinyurl.com/ybas4twh> to discuss about it."

# tip me repsonse
tip = "Hey, thanks for the thought! If you tip me, it all goes to RainBorg. If you want to tip my creator, tip `@Sajo8#2953`. Once again, thank you! <:t_smile:405478442599972874>"

# Only owner has access to certain commands
ownerID = "235707623985512451"

@client.event 
async def on_ready():
    print("With me around, ain't gonna be no market talk!") 

lastMessageTimes = []
maxResponses = 4
timeFrameWindow = 15

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
        await client.send_message(message.channel, message.author.mention + " " + random.choice(wordlist))
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

config = json.load(open('config.json'))
client.run(config['token'])
