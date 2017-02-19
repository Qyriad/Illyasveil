# Illyasveil by 916253
# license: Apache License 2.0
# https://github.com/916253/Illyasveil

import discord
from discord.ext import commands
from sys import argv

class Test:
    """
    Test addon.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def screams(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/j0Dkv2Z.png")
        
    @commands.command()
    async def screams2(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/bh45fyL.png")
        
    @commands.command()
    async def wat(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/bp2YRAf.png")
    
    @commands.command(pass_context=True, name="no!!")
    async def nope(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/OcDrUYO.png")
        
    @commands.command()
    async def rawr(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/Bqw4OwQ.png")
    
    @commands.command()
    async def sudoku(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/9AJeFFu.png")
        
    @commands.command()
    async def baka(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/OyjCHNe.png")
        
    @commands.command()
    async def quivers(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/Aq5VISF.gifv")
        
    @commands.command()
    async def nya(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/WKB08Iq.png")
        
    @commands.command(pass_context=True, name="916253")
    async def numbers(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/NukslEg.png")
        
    @commands.command()
    async def emojihax(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/6eVmvo3.png")
        
    @commands.command()
    async def thump(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/LZhDBkH.gifv")
        
    @commands.command()
    async def rikkaeh(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/3Lg5jlA.png")
        
    @commands.command()
    async def orz(self):
        """meme"""
        await self.bot.say("http://i.imgur.com/LEey0Cd.png")
        


def setup(bot):
    bot.add_cog(Test(bot))
