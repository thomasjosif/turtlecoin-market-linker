# turtlecoin-market-linker

A simple bot to look for any market talk-related keywords, after which it chooses randomly from and prints a pre-set message.

## Usage

``` py
py market-bot.py
```

## Connecting it to Discord

* Go [here](https://discordapp.com/developers/applications/me#top) to make a bot.
* Give your bot a name, and then click `Create App`.
* Scroll down to `Create a Bot User` and click that.
* Click `Yes, do it!`
* Copy your  bot token by clicking `click to reveal` in the `APP BOT USER`section.
* Enter this token in the last line in `market-bot.py`, replacing `token`(keep the `"`).
* **Don't reveal this token to anyone!**
* Next you need to get the Channel ID you want the bot to run in.
* In Discord, follow these steps-

   1. Click on `User Settings`(small gear icon to right of name in the bottom left) 

   2. Click on `Appearance` 

   3. Enable `Developer Mode`.
* Right click on the Discord channel you want the bot to work in, and press `Copy ID`.
* Open up `market-bot.py`, and replace the value of `message.channel.id` with the ID you just copied(again, keep the `"`).
* Scroll up and click `Generate OAuth2 URL`
* Choose `bot` under `SCOPES`
* Select the permissions you want the bot to have under `Bot Permissions`
* When done, click `COPY` next to the link generated
* Open said link and choose the server you wish to add the bot to. You must have `Manage Server` permissions.

## Deploying on Heroku

I use it personally and recommend as on signing up you get free "Dynos"(credits) worth ~$40 for free, with the only verification being a valid e-mail address, which renews monthly. Setting it up is relatively easy-

* open Command Prompts/terminal and type `pip freeze`
  * then copy/paste everything shown into a file called `requirements.txt`, like in my repo
* in a file `runtime.txt` specify the python version to use. Assuming you used the latest version, check and enter the value after making sure it is supported by Heroku [here](https://devcenter.heroku.com/articles/python-runtimes). See my file for the format
* then make a file `Procfile`(no extension, check for caps) and specify how to run the program, like `python market-bot.py`. Check mine if you're unsure
* Once done, make an account in Heroku(screw the get started guide) and make a new application
* Go to `Deploy` and scroll down
  * Download [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
  * If you don't have Git installed yet, then do so(through the Heroku installer.)
    * For the rest of the tutorial, enter all commands through the terminal/command prompts
    * If you do then cancel the installation of Git and run `Git CLI` when the CLI installs
  * Login to your Heroku account using `heroku login`
  * Clone and cd to your repository using the commands given
  * Make any changes you want to locally, then run the commands given to push them to Heroku and deploy them
* If it deploys successfully, then it should-
  * work in your server without having to run the script locally, and
  * show the message you defined to print on startup in the logs section of Heroku (`More` -> `View Logs`)

## Thanks

Big thanks to [@ZedPea](https://github.com/zedpea), he helped a lot with the bot.
