#Discord Bot
#Made By 'Wolf'1K89

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from discord.voice_client import VoiceClient
import datetime

startup_extensions = ["Music"]

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Ready when you are")
    print("I am unning on: ", bot.user.name)
    print("With the ID: ", bot.user.id)
    print(datetime.datetime.now())

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed=discord.Embed(title="{}'s".format(user.name), Description="User Name", color=0x00ff00)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="Id", value=user.id, inline=True)
	embed.add_field(name="Status: ", value=user.status, inline=True)
	embed.add_field(name="Highest Role", value=user.top_role)
	embed.add_field(name="User Joined At", value=user.joined_at)
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
	await bot.say(":boot: byby {}".format(user.name))
	await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
	await bot.say(":no_entry_sign: And Don't Come Back!")
	await bot.ban(user)

@bot.command(pass_context=True)
async def sinfo(ctx):
	embed=discord.Embed(name="{}'s".format(ctx.message.server.name), description="Server Info", color=0x00ff00)
	embed.add_field(name="Owner", value=ctx.message.server.owner)
	embed.add_field(name="Server Name", value=ctx.message.server.name)
	embed.add_field(name="Server ID", value=ctx.message.server.id)
	embed.add_field(name="Roles", value=len(ctx.message.server.roles))
	embed.add_field(name="members", value=len(ctx.message.server.members))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.add_field(name="Created At", value=ctx.message.server.created_at)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def purge(context, number : int):
	deleted = await bot.purge_from(context.message.channel, limit=number)

class Main_Commands():
	def __init__(self, bot):
		self.bot = bot

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))



bot.run("NDc5MzI2OTYxODQwMjkxODUw.DlZbGQ.1J-321_CHIrW7ZKB0sF0o5OmM5U")

