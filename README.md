# NickName-Bot
A simple bot made to circumvent one restriction of nickname changing on discord. In order to change someone's nickname, a discord member must have a higher role than the person they want to change the nickname of. They cannot change the nickname of someone of the same role level or higher. With this bot, they can change the nicknames of people with the same role level.

## Getting Started
1) Go to https://discordapp.com/developers/applications/ and create an application for the discord bot.
2) Get a token under the Bot tab and place in bot.run("token here") in main.py.
3) Invite the bot to your discord server by creating a link in OAuth2.
4) Create a role and give it nickname priviledge. Place above roles of members you wish to be effected.

## Prerequisites
Python 3.7+ 

Discord.py 1.3.0a

## Installing
Go to https://www.python.org/downloads/ to install Python.

Run py -3 -m pip install -U discord.py in command prompt for Windows to get/update Discord.py

## Commands

Commands for bot prefaced with "dj."

- n.help \- see commands list in discord.
- dj.prefix new_prefix\- change the prefix command for the bot.
- dj.change target | nickname \- changes the nickname of target.
- dj.schange target | nickname \- changes the nickname of target and deletes your text.
- dj.achange nickname \- changes the nicknames of everyone in the server(with role lower than NickName bot).
- dj.self_reset \- clears your nickname.
