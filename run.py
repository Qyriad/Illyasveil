#!/usr/bin/env python3

# Illyasveil by 916253
# Based off of Kurisu by 916253 & ihaveamac
# license: Apache License 2.0
# https://github.com/916253/Illyasveil
# https://github.com/916253/Kurisu

description = """
Illyasveil, the basic selfbot that doesn't do much yet.
"""

# import dependencies
import os
from discord.ext import commands
import discord
import datetime, re
import json, asyncio
import copy
import configparser
import traceback
import sys
import os

# sets working directory to bot's folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# read config for token
config = configparser.ConfigParser()
config.read("config.ini")



prefix = [',']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None, self_bot=True)



# http://stackoverflow.com/questions/3411771/multiple-character-replace-with-python
chars = "\\`*_<>#@:"
def escape_name(name):
    name = str(name)
    for c in chars:
        if c in name:
            name = name.replace(c, "\\" + c)
    return name.replace("@", "@\u200b")  # prevent mentions
bot.escape_name = escape_name

bot.pruning = False 

@bot.event
async def on_ready():
    for server in bot.servers:
        print("{} has started! {} has {:,} members!".format(bot.user.name, server.name, server.member_count))
        bot.server = server


# loads extensions
addons = [
    'addons.memes',
    'addons.load',
]

failed_addons = []

for extension in addons:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(extension, type(e).__name__, e))
        failed_addons.append([extension, type(e).__name__, e])

# Execute
print('Bot directory: ', dir_path)
bot.run(config['Main']['token'], bot=False)
