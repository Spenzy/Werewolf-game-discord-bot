import traceback
import sys
import os
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=':')
client.remove_command('help')


def pExist(user, plist):
    for l in plist:
        if user.id == l[0]:
            return False
    return True


def roleList(n: int, rl):
    r = []
    if 7 <= n <= 12:
        if n < 11:
            if n == 7 or n == 8:
                for i in range(2):
                    r.append(rl[0])
                nb = n - 2
            else:
                for i in range(3):
                    r.append(rl[0])
                nb = n - 3
            for i in range(3):
                r.append(rl[i + 1])
                nb = nb - 1
            for i in range(nb):
                r.append(rl[4])
        else:
            for i in range(3):
                r.append(rl[0])
            nb = n - 3
            for i in range(2):
                r.append(rl[1])
                nb = nb - 1
            for i in range(2):
                r.append(rl[i + 2])
                nb = nb - 1
            for i in range(nb):
                r.append(rl[4])
    else:
        print('invalid player count')
    return r


def assignRoles(pl):
    for p in pl:
        if p[1] == 'idle':
            role = random.choice(roleList(len(players), roles))
            p[1] = role
            roles.remove(role)
        else:
            print('already has a role')
    return pl


def Wolves(pl):
    wl = []
    for p in pl:
        if p[1] == 'wolf':
            wl.append(p)
    return wl


players = []
roles = ['wolf',
         'sorcerer',
         'detective',
         'doctor',
         'villager']


# events
@client.event  # bot's log in id , defines online status
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    gid = client.get_guild(397532070772998154)
    print(gid.name)


@client.event  # bot's dm interaction section
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)


@client.event  # bot's error handler
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please enter the required argument')
    error = getattr(error, 'original', error)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


# commands
@client.command()  # just a random command
async def bbyoda(ctx):
    gid = client.get_guild(397532070772998154)
    embed = discord.Embed(color=discord.Color.purple())
    embed.set_author(name='Baby Yoda ♥', icon_url=gid.icon_url())
    embed.set_image(url=gid.owner.avatar_url())
    await ctx.send(embed=embed)


@client.command()  # starts game by sending roles to players
async def start(ctx):
    #if len(players) > 6:
        for p in players:
            user = client.get_user(p[0])
            await user.send(f'Your role is : {p[1]}')
        await ctx.send('Game starting ! Good luck surviving!')
    #else:
    #    await ctx.send('You need at least 7 players to start a game!')


@client.command()  # assigns members who participated
async def participate(ctx):
    if len(players) < 12:
        player = [ctx.author.id, 'idle', False]
        if pExist(ctx.author, players):
            players.append(player)
            await ctx.send("Participation processed !")
        else:
            await ctx.send("You already participated !")
    else:
        await ctx.send("Sorry, maximum supported # of players reached !")


@client.command()  # lists all participating players
async def plist(ctx):
    for p in players:
        uid = p[0]
        user = client.get_user(uid)
        await ctx.send(f'{user.mention}')


# Cog management section
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')


cog_path = './cogs'
for filename in os.listdir(cog_path):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjA0MzE5OTY1NTg3MTc3NDcy.XhzLeA.J_FuSO8WtfbFrCuRrTXnmVoDPoU')