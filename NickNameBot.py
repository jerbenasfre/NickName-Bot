# 10/31/18
# nicknamebot.py
import discord
from discord.ext.commands import Bot
from discord.ext import commands

import asyncio
import time
import random
import re

client = discord.Client()
cprefix = 'n.'
bot = commands.Bot(command_prefix = 'n.')

Embed = discord.Embed()

@bot.command(name = 'prefix', description= cprefix + 'prefix new_prefix')
async def prefix(ctx):
    '''Changes the prefix command bot responds to'''
    global cprefix

    cprefix = ctx.message.content.split()[1]
    Bot.command_prefix = cprefix
    
    await ctx.send('The new prefix is: ' + cprefix)
    await ctx.send(activity=discord.Game(name= cprefix+"help for commands."))

    
@bot.command(name = 'change',
             description= cprefix + 'change user_name | nickname(2-32 char in length)\n' +
                               cprefix + 'change @user nickname(2-32 char in length)\n' +
                               cprefix + 'change user_name(only) to reset\n' +
                               cprefix + 'change @user(only) to reset\n' 
                                       + 'prefix.[ways to use command]',
             aliases=['change_nick','nick','nickname','nick_name'])
async def change(ctx):
    '''Changes the name of a Discord Member(Role of member has to be lower than NickName Bot's Role)'''
    command = re.compile(r"(?P<prefix>[\S]*)(?P<prefix2>[.?!@#$%^&*-+=])(?P<command>[\S]+)")
    command_index = re.search(command,ctx.message.content)

    text = ctx.message.content[command_index.end():].strip()
    mentions =  ctx.message.mentions
    await change_helper(ctx, text, mentions)
    

@bot.command(name = 'schange',
             description= 'Similar to ' + cprefix + 'change except it erases your message for anonymity. This is for you stealthy trolls ;)',
             aliases=['stealth_change','snick','snickname','snick_name'])
async def schange(ctx):
    command = re.compile(r"(?P<prefix>[\S]*)(?P<prefix2>[.?!@#$%^&*-+=])(?P<command>[\S]+)")
    command_index = re.search(command,ctx.message.content)
    
    text = ctx.message.content[command_index.end():].strip()
    await ctx.message.delete()
    await change_helper(ctx, text)


@bot.command(name = 'rchange',
             description= 'Randomly selects a user to change nick of.',
             aliases=['rnick'])
async def rchange(ctx):
    command = re.compile(r"(?P<prefix>[\S]*)(?P<prefix2>[.?!@#$%^&*-+=])(?P<command>[\S]+)")
    command_index = re.search(command,ctx.message.content)
    
    text = ctx.message.content[command_index.end():].strip()
    member = random.choice(ctx.message.channel.guild.members)
    await ctx.send('Attempting to change ' + member.name + "'s nick.", delete_after = 2)
    text = member.name + ' | ' + text
    print(text)
    await ctx.message.delete()
    await change_helper(ctx, text)


@bot.command(name= 'achange',
             description= 'Mass changes nicknames with given nick.',
             aliases=['anick','all'])
async def achange(ctx):
    await ctx.send('Attempting to do mass nick change!', delete_after = 3)
    
    command = re.compile(r"(?P<prefix>[\S]*)(?P<prefix2>[.?!@#$%^&*-+=])(?P<command>[\S]+)")
    command_index = re.search(command,ctx.message.content)
    text = ctx.message.content[command_index.end():].strip()
    for member in ctx.guild.members:
        if ctx.guild.get_member(507343818404659202).top_role > member.top_role:
            try:
                await member.edit(nick = text)
            except Exception as e:
                print(f'**`ERROR:`** {type(e).__name__} - {e}')
    

async def change_helper(ctx, text = '', mentions = []):
    '''Handles the parsing of a message'''
    if len(mentions) != 0:
        member = mentions[0]
        text = text.split()
        nickname = ' '.join(text[1:]) if len(text) > 1 else ""
    else:
        if ' | ' not in text:
            nickname = ''
            name = ' '.join(text.split())
        else:
            text = text.split(' | ')
            name = text[0]
            nickname = text[1]

        member = discord.utils.find(lambda m: (m.name == name or m.nick == name), ctx.message.channel.guild.members)

        if member == None:
            await ctx.send('Could not find a user by the name/nick of ' + name + '. Mention user when using the .nick/change command.', delete_after = 3)
            return
    try:
        if len(nickname) == 0:
            await member.edit(nick = None)
            await ctx.send('The nick has been reset!', delete_after = 3)
        else:
            await member.edit(nick = nickname)
            await ctx.send('The nick has been changed!', delete_after = 3)
    except Exception as e:
        print(f'**`ERROR:`** {type(e).__name__} - {e}')
        await ctx.send('Something went wrong!', delete_after = 3)

        
@bot.command(name='self_reset',description= "Reset your nick with " + cprefix + "self_reset")
async def reset(ctx):
    try:
        await ctx.message.author.edit(nick = None)
        await ctx.send('The nick has been reset!', delete_after = 3)
    except:
        await ctx.send('Something went wrong! Creator is a bad creator D:<', delete_after = 3)

        
@bot.event#Event handler.
async def on_ready():
    print('NickNameBot is at your service.')
    await bot.change_presence(activity=discord.Game(name= cprefix + "help for commands."))            

        
bot.run('TOKEN HERE')
