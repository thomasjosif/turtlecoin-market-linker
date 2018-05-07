import discord
import asyncio
import random

client = discord.Client() 

# list of words which triggers it
bannedWords = ["trade", "exchange", "tradeogre", "sell turtlecoin", "buy turtlecoin", "sell trtl", "buy trtl", "tradesatoshi", "trde", "trae", "tradesat", 
				"wen lambo", "wen moon", "trade-", "when moon", "when lambo", "price", "fiat", "pr1ce", "usd", "euro", "inr", "binance", "altcoin", "sats", 
				"to down", "ts down", "tradesatoshi down", "tradeogre down", "ogre down", "sats down", "exhcnage", "pump and dump", "dump", 
				"eur", "gbp", "ruble", "but turtlecoin", "but trtl", "moons", "hitbtc", "trtl be worth", "trtl worth", "exhcnag,e"
				"airdrop", "shitcoin", "shitcion", "shitconi", "gewi", "gwei", "mine and sell", "down trend", "resistance line", "bearish", "bullish",
				"to da moon", "pump and dump", "pump & dump", "pumped and dumped", "pumped & dumped", "pump n dump", "pumped n dumped" , "cmc", "coin market cap",
				"ico", "ipo", "stop loss", "mkid", "tether", "trading", "trend line", "buy wall", "sell wall", "buy order", "sell order", "buy trlt", "sell trlt", 
				"wtb", "wts", "Bitfinex", "Kraken", "Coinbase", "coinone", "Bitstamp", "Bithumb", "Bittrex", "Quoine", "Gemini", "bitFlyer", "BTC-e", "Poloniex", 
				"exx", "livecoin", "exmo", "korbit", "liqui", "cex.io", "tidex", "vaultoro", "itbit", "cryptopia", "yobit", "lakebtc", "kucoin", "btc-alpha", 
				"quadrigacx", "localbitcoins", "coinfloor", "bitx", "coinexchange", "okcoin", "gatecoin", "coinmate", "bitso", "acx", "idex", "cryptobridge", 
				"btcc", "bitfex", "virwox", "bleutrade", "abucoins", "paymium",  "flowbtc", "gate.io", "bitkonan", "cryptox", "cryptonit", "go4cryptos", "c-cex",
				"novaexchange", "coincoz", "btctrade", "vircurex", "allcoin", "coinsecure",  "indacoin", "bitmarket", "braziliex", "coinnest", "dsx", 
				"localturtlecoin", "localmonero", "local bitcoin", "local bitcoins", "localbitcoin", "stocks.exchange", "wen lamb0", "when lamb0", "wen l@mbo", 
				"when l@mbo", "wen l@mb0", "when l@mb0", "indacion", "indaocin", "satoshi", "ogre", "tr@de", "tr2de", "elliot wave", "when buy in", "mt. gox",
				" mt. gox", "mtgox", "mt gox", "pesos", "pesps", "trtl sell", "tlt sell", "turtlecoin sell", "trtl buy", "trlt buy", "turtlecoin buy",
				"1sat", "1 sat", "buy turtle", "sell turtle", "crypto exchange", "cryptocurrency exchange", "crypto currency exchange", "sellin", "buyin",
				"selin", "pumpin", "dumpin", "sellwall", "buywall", "selwall", " ts", "s@t", "0 sat", "0sat", "0stas", "stas", "st@s", "btc volume", 
				"btc volue", "btc volube", "wen buy in", "wen sell out", "wen but in", "when but in", "pr!ce", "binnance", "buy btc", "buy bct", "buy bticoin", 
				"buy bitcion", "buy btiocin", "buy bitocin", "coin offering", "inital coin offering", "crypto investing", "crypto invensting", "crypto investments",
				"investment", "investment", "investing", "invensting", "dividends", "dividens", "profit, dividends and gains", "profit dividens and gains",
				"mark3t", "xchange"]

# list of responses
wordlist = ["Heyo, please move to the server linked in #market-talk, we don't like it here.", 
			"If you could move to the server linked in #market-talk, that'd be great! We don't enjoy that here.", 
			"Please move this discussion to the server linked in #market-talk, we like to keep this server focused on support and development. Thank you! :t_smile:",
			":rotating_light: MARKET TALK DETECTED :rotating_light: :rotating_light: Move to the server linked in #market-talk, we don't like that here. :rotating_light:"]

#help reply
help = "Available commands - `^git` and `^todo`"

# github repo
git = "https://github.com/Sajo811/turtlecoin-market-linker"

# todo list
todo = "https://github.com/Sajo811/turtlecoin-market-linker/projects/1"

# supreme power
super = "WHEN WEB WALLET"

# no permission to run
perms = "Sorry, you don't have the privileges to run this command. It's like you're SuperMan, and this command is green kryptonite."

# manual warn's response
manres = "Hey, we don't like market-related talk in here. Join the server linked in #market-talk to discuss about it."
 

@client.event 
async def on_ready():
	print("With me around, ain't gonna be no market talk!") 

@client.event
async def on_message(message):

	# convert it to lower
	low = message.content.lower()

	#send only in general
	if message.channel.id != "440496273762549762":
		return

	# check if bot is author in which case doesnt do anything
	if message.author.bot:
		return

	# check if message incl. banned words. if so, spit a response
	if any(word.lower() in message.content.lower() for word in bannedWords):
		await client.send_message(message.channel, message.author.mention + " " + random.choice(wordlist))

	# command to see if message *is* something and then responds if true
	if message.content.lower() == "^help":
		await client.send_message(message.channel, message.author.mention + " " + help)
		return

	if message.content.lower() == "^git":
		await client.send_message(message.channel, message.author.mention + " " + git)
		return

	if message.content.lower() == "^todo":
		await client.send_message(message.channel, message.author.mention + " " + todo)
		return

	#commmand which can only be run by person whose user id matches this one here
	if message.content.lower() == "^super":
		if message.author.id != "235707623985512451":
			await client.send_message(message.channel, message.author.mention + " " + perms)
		else:
			await client.send_message(message.channel, message.author.mention + " " + super)
		return	
	
	# command to manually warn person
	if message.content.lower().startswith("^warn"):	
		if message.author.id == "235707623985512451":
			# get userid of person
			user = message.mentions[0]
			await client.send_message(message.channel, user.mention + " " + manres)
	else:
		return

client.run("token")
