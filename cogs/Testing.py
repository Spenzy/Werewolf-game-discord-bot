import discord
from discord.ext import commands

client = discord.Client()


class Testing(commands.Cog):

    def _init_(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Testing Cog Active !')


def setup(client):
    client.add_cog(Testing(client))