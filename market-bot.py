import discord
import asyncio
import random

client = discord.Client() 

bannedWords = ["trade", "exchange", "tradeogre", "sell turtlecoin", "buy turtlecoin", "sell trtl", "buy trtl", "tradesatoshi", "trde", "trae", "tradesat", 
				"wen lambo", "wen moon", "trade-", "when moon", "when lambo", "price", "fiat", "pr1ce", "usd", "euro", "inr", "binance", "altcoin", "sats", 
				"ts", "to down", "ts down", "tradesatoshi down", "tradeogre down", "ogre down", "sat down", "sats down", "exhcnage", "pump and dump", "dump", 
				"eur", "gbp", "ruble", "rub", "but turtlecoin", "but trtl", "mcap", "market cap", "hodl", "moons", "hitbtc", "trtl be worth", "trtl worth", 
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
				"1sat", "1 sat"]

wordlist = ["Go the server linked in #market-talk, not in this server", 
			"Rock's gonna git you boi, better move to the server linked in #market-talk NOW", 
			"u. move to server linked in #market-talk now. otherwise u ban.",
			":rotating_light: MARKET TALK DETECTED :rotating_light: :rotating_light: Move to the server linked in #market-talk to save yourself :rotating_light:"]

@client.event 
async def on_ready():
	print("With me around, ain't gonna be no market talk!") 

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if any(word.lower() in message.content.lower() for word in bannedWords):
		await client.send_message(message.channel, message.author.mention + " " + random.choice(wordlist))


client.run("token")
