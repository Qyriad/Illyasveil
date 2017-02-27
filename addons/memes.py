# Some code borrowed from Kurisu by 916253 & ihaveamac
# license: Apache License 2.0
# https://github.com/916253/Kurisu

import discord
from discord.ext import commands
from sys import argv

class Memes:
    """
    Meme commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        author = ctx.message.author
        await self.bot.say(msg)

    # list memes
    @commands.command(name="listmemes", pass_context=True)
    async def _listmemes(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._meme(ctx, msg)

    # memes
    @commands.command(pass_context=True, hidden=True)
    async def screams2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/bh45fyL.png")

    @commands.command(pass_context=True, hidden=True)
    async def screams(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/j0Dkv2Z.png")

    @commands.command(pass_context=True, hidden=True)
    async def ehh(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/2SBC1Qo.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def wat(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/bp2YRAf.png")
        
    @commands.command(pass_context=True, hidden=True, name="no!!")
    async def nope(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/OcDrUYO.png")

    @commands.command(pass_context=True, hidden=True)
    async def illyacup(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/GMRp1dj.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def quivers(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/Aq5VISF.gifv")

    @commands.command(pass_context=True, hidden=True)
    async def nya(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/WKB08Iq.png")

    @commands.command(pass_context=True, hidden=True, name="916253")
    async def numbers(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/NukslEg.png")

    @commands.command(pass_context=True, hidden=True)
    async def thump(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/LZhDBkH.gifv")

    @commands.command(pass_context=True, hidden=True)
    async def rikkaeh(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/3Lg5jlA.png")

    @commands.command(pass_context=True, hidden=True)
    async def orz(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/LEey0Cd.png")

    @commands.command(pass_context=True, hidden=True)
    async def shotsfired(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/zf2XrNk.gifv")

    @commands.command(pass_context=True, hidden=True)
    async def thumbsup(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/2dll9My.png")

    @commands.command(pass_context=True, hidden=True)
    async def lenny(self, ctx):
        """Memes."""
        await self._meme(ctx, "( ͡° ͜ʖ ͡°)")

    @commands.command(pass_context=True, hidden=True)
    async def rip(self, ctx):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(pass_context=True, hidden=True)
    async def permabrocked(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/ARsOh3p.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def lucina(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/tnWSXf7.png")

    @commands.command(pass_context=True, hidden=True)
    async def lucina2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/ZPMveve.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def thumbsup2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/hki1IIs.gifv")

    # Cute commands :3
    @commands.command(pass_context=True, hidden=True)
    async def headpat(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/7V6gIIW.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def headpat2(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/djhHX0n.gifv")

    @commands.command(pass_context=True, hidden=True)
    async def sudoku(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/VHlIZRC.png") 
        
    @commands.command(pass_context=True, hidden=True)
    async def rawr(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/Bqw4OwQ.png")

    @commands.command(pass_context=True, hidden=True)
    async def baka(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/OyjCHNe.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def pantsu(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/BoRZLTU.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def luff(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/8TKIixk.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def fug(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/ZhTZtDa.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def fug2(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/9LvnrBB.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def walksin(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/xMfzlnU.jpg")
        
    @commands.command(pass_context=True, hidden=True)
    async def walksout(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/wIRkdud.jpg")
        
    @commands.command(pass_context=True, hidden=True)
    async def period(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/IGu4zGZ.jpg")
        
    @commands.command(pass_context=True, hidden=True)
    async def sadness(self, ctx):
        """:c"""
        await self._meme(ctx, "http://i.imgur.com/maRp8nB.png")
        
    @commands.command(pass_context=True, hidden=True)
    async def negativity(self, ctx):
        """:c"""
        await self._meme(ctx, "hhttp://i.imgur.com/1D5vHSk.png")

# Load the extension
def setup(bot):
    bot.add_cog(Memes(bot))
