import discord
import asyncio
from discord.ext import commands

client = discord.Client()


class Basics(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Basics Cog Active !')

    # Commands
    @commands.command()
    async def status(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}, i am online ! :D')

    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    async def help(self, ctx):
        # Declaration
        basicF = discord.Embed(color=discord.Color.purple())
        betaF = discord.Embed(color=discord.Color.dark_magenta())
        inProg = discord.Embed(color=discord.Color.dark_gold())
        # Setting author/title
        basicF.set_author(name="Help: Basic Functions!")
        betaF.set_author(name="Help: Beta Functions!")
        inProg.set_author(name="Help: In Progress Functions!")
        # Adding fields/commands
        basicF.add_field(name=':clear x', value='Clear x messages', inline=False)
        basicF.add_field(name=':help', value='Shows the help menu', inline=False)
        betaF.add_field(name=':participate', value='Participate in the current game', inline=False)
        betaF.add_field(name=':plist', value='Show the current list of participants', inline=False)
        betaF.add_field(name=':start', value='Starts the game and sends roles', inline=False)
        inProg.add_field(name=':shield', value='used by doctors to shield allies', inline=True)
        inProg.add_field(name=':kill', value='used by wolves to kill', inline=True)
        inProg.add_field(name=':cycle', value='cycles the day/night rotation', inline=False)

        await ctx.send(embed=basicF)
        await ctx.send(embed=betaF)
        await ctx.send(embed=inProg)


def setup(client):
    client.add_cog(Basics(client))
