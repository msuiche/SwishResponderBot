# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import csv

from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='swish.export', help='Collect logs required for the investigation.')
@commands.has_role('responders')
async def export_logs(ctx, command):
    await ctx.author.send("Yo! Here is a copy of the logs.")
    await ctx.author.send("If you have any questions you can ping me @msuiche#1337 on Discord or @msuiche on Twitter.")
    # if command == "view":
    #    guild = ctx.message.guild
    #    async for entry in guild.audit_logs(limit=100):
    #        await ctx.author.send('{0.user} did {0.action} to {0.target}'.format(entry))
    if command == "logs":
        fieldnames = ['created_at', 'category', 'id', 'user', 'action', 'target', 
                    'before', 'after', 'reason', 'changes']
        now = datetime.now()
        date_time = now.strftime("%Y%m%d-%H%M%S")
        guild = ctx.message.guild
        filename = guild.name + '_' + date_time + '_auditlogs.csv'
        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            async for entry in guild.audit_logs():
                writer.writerow({
                    'created_at': entry.created_at,
                    'category': entry.category,
                    'id': entry.id,
                    'user': entry.user,
                    'action': entry.action,
                    'target': entry.target,
                    'before': entry.before,
                    'after': entry.after,
                    'reason': entry.reason,
                    # 'changes': entry.changes,
                    })
            f.close()
            await ctx.author.send(file=discord.File(filename))

        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        print('[%s] %s on %s requested audit logs.' % (timestamp, ctx.author.name, guild.name))

    elif command == "webhooks":
        fieldnames = ['created_at', 'avatar', 'avatar_url', 'channel', 'channel_id',
                    'guild', 'guild_id', 'id', 'name', 'token',
                    'type', 'url', 'user']
        now = datetime.now()
        date_time = now.strftime("%Y%m%d-%H%M%S")
        guild = ctx.message.guild
        filename = guild.name + '_' + date_time + '_webhooks.csv'

        webhooks = await guild.webhooks()
        await ctx.author.send("There are a total of %d webhooks in this guild." % (len(webhooks)))

        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in webhooks:
                writer.writerow({
                    'created_at': entry.created_at,
                    'avatar': entry.avatar,
                    'avatar_url': entry.avatar_url,
                    'channel': entry.channel,
                    'channel_id': entry.channel_id,
                    'guild': entry.guild,
                    'guild_id': entry.guild_id,
                    'id': entry.id,
                    'name': entry.name,
                    'token': entry.token,
                    'type': entry.type,
                    'url': entry.url,
                    'user': entry.user,
                    })
            f.close()
            await ctx.author.send(file=discord.File(filename))

        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        print('[%s] %s on %s requested webhooks lists.' % (timestamp, ctx.author.name, guild.name))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the "responders" role for this command.')

bot.run(TOKEN)