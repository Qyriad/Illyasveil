import discord
from discord.ext import commands
from sys import argv

class Playing:
    """
    Sets playing message.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

        
    @commands.command(pass_context=True)
    async def playing(self, ctx, *gamename):
        """Sets playing message."""
        await self.bot.change_presence(game=discord.Game(name='{}'.format(" ".join(gamename))))


def setup(bot):
    bot.add_cog(Playing(bot))
