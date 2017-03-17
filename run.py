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
import datetime, re
import json
import discord
import asyncio
import configparser

# sets working directory to bot's folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# read config for token
config = configparser.ConfigParser()
config.read("config.ini")

prefix = [',']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None, self_bot=True)

@bot.event
async def on_ready():
    for server in bot.servers:
        print("{} has started! {} has {:,} members!".format(bot.user.name, server.name, server.member_count))
    await bot.change_presence(status=discord.Status.offline)

# loads extensions
addons = [
    'addons.memes',
    'addons.load',
    'addons.playing',
]

for extension in addons:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(extension, type(e).__name__, e))

# Execute
print('Bot directory: ', dir_path)
bot.run(config['Main']['token'], bot=False)
