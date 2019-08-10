# -*- coding: utf-8 -*-
import discord, asyncio
import random
from random import randint
import os
import pip
import time
from discord.ext import commands
from discord import utils
client = commands.Bot(command_prefix='#')

client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="(>_):#help", type=discord.ActivityType.playing))
    print("ok")












@client.event
async def on_member_join(member):
    roles = discord.Guild.get_role(role_id=609013471845023785, self = member.guild)
    await client.get_channel(609358360277549059).send(f"Приветствую тебя на сервере {member.guild.name}, {member.mention}, зайди в канал получения ролей(вход-на-сервер)")


@client.event
async def on_member_remove(member):
    await client.get_channel(609358360277549059).send(f"{member.mention} покидает наш сервер...")


@client.command(brief = 'Отослать сообщение от имени бота(Администрация)')
@commands.has_permissions(administrator = True) # Могут использовать лишь пользователи с правами Администратора
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() # Удаляет написанное вами сообщение
   embed = discord.Embed(description = cnt, colour = 0xffff00) # Генерация красивого сообщения
   await channel.send(embed=embed) # Отправка сообщения в указанный Вами канал
@client.command(brief = 'Информация о пользователе')
@commands.cooldown(1, 5, commands.BucketType.user)
async def info(ctx, member: discord.Member = None):
    user = ctx.message.author if (member == None) else member
    if (user == client.user):
        return
    else:
        mobile = user.is_on_mobile()
        gameuser = user.activity
        name = user.display_name
        role = user.top_role


    if mobile == True:
        rly = "Да"
    else: rly = "Нет"
    if(gameuser == None):
        embed = discord.Embed(title=f'Пользователь {user}', description= f'Пользователь ни во что не играет\nС телефона?: {rly}\n Отображаемое имя: {name}\n Самая высокая роль: {role.mention}', color=0xffff00)
        embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=str(ctx.message.author.avatar_url))
    else:
        embed = discord.Embed(title=f'Пользователь {user}', description= f'Играет в {gameuser} \nС телефона?: {rly}\nОтображаемое имя: {name}\n Самая высокая роль: {role.mention}', color=0xffff00)
        embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=str(ctx.message.author.avatar_url))

    await ctx.send(embed=embed)
varable = ["Да", "Нет"]
@client.command(brief = 'Рандом(2 сек)')
@commands.cooldown(1, 2, commands.BucketType.user)
async def random(ctx):
    res = randint(1,2)
    if res == 1:
        await ctx.send("Да")
    else:
        await ctx.send("Нет")
@client.command(brief = 'Аватар пользователя(5 сек)')
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, member: discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=0xffff00)
    embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
@client.command(brief = 'Перевести текст(5 сек)')
@commands.cooldown(1, 5, commands.BucketType.user)
async def trans(ctx, *args):

    my_args =' '.join(args)
    rueng = [
        ['а', 'a'], ['б', 'b'], ['в', 'v'], ['г', 'g'], ['д', 'd'], ['е', 'e'], ['ё', 'e'], ['ж', 'j'], ['з', 'z'],
        ['и', 'i'], ['й', 'i'], ['к', 'k'], ['л', 'l'], ['м', 'm'], ['н', 'n'], ['о', 'o'], ['п', 'p'], ['р', 'r'],
        ['с', 's'], ['т', 't'], ['у', 'u'], ['ф', 'f'], ['х', 'h'], ['ц', 'c'], ['ч', 'ch'], ['ш', 'sh'], ['щ', 'sh'],
        ['ъ', ''], ['ы', ''], ['ь', ''], ['э', ''], ['ю', 'yu'], ['я', 'ya']
    ]
    for i in rueng:
        if i[0] in my_args:
            my_args = my_args.replace(i[0], i[1])


    embed = discord.Embed(colour = ctx.message.author.color, description = f'{my_args}')

    await ctx.send(embed = embed)
@client.command(brief = 'Помощь')
async def help(ctx, *args):
    await ctx.message.delete()
    embed = discord.Embed(title=f'Помощь по командам', description= f'#avatar - Аватар пользователя(5 сек)\n #help - Это сообщение \n #info - Информация о пользователе \n #random - Рандом(2 сек) \n #say - Отослать сообщение от имени бота(Администрация) \n #trans - Перевести текст(5 сек) \n #f - просто f.. \n#role - Выдача роли(Администратор)\n#call - звонок на сервере(Для включения демонстрации)\n#move (id канала откуда) (id канала куда) (ник игрока(если пусто переместит всех))', color=0xffff00)
    embed.set_footer(text=f'Вызвано: {ctx.message.author} \n Удалится через 30 секунд', icon_url=str(ctx.message.author.avatar_url),)
    embed.set_image(url='https://sun9-49.userapi.com/c849520/v849520051/1d8873/WD4UuGoTas8.jpg')
    msg = await ctx.send(embed = embed)
    await asyncio.sleep(30)  # sec
    await msg.delete()
@client.command(pass_context = True)
async def f(ctx, arg: discord.Member = None):
    if not arg:
        await ctx.message.delete()
        author = ctx.message.author
        emb = discord.Embed(title= f'{author.name} выражает уважение' , colour= 0xffff00)
        await ctx.send(embed= emb)
    else:
        await ctx.message.delete()
        author = ctx.message.author
        emb = discord.Embed(title= f'{author.name} выражает уважение'  +  f' {arg.name}', colour= 0xffff00)
        await ctx.send(embed= emb)
@client.command(brief = 'Выдача роли(Администрация)')
@commands.has_permissions(administrator = True)
@commands.cooldown(1, 2, commands.BucketType.user)
async def role(ctx, member: discord.Member = None, * , role: discord.Role = None):
    if role== None and member == None:
        await ctx.send("Укажите пользователя и id роли")
        return
    if member == None:
        await ctx.send("Укажите пользователя")
    else: user = member
    if role == None:
        await ctx.send("Укажите роль")
    else:
        await member.add_roles(role)
        embed = discord.Embed(title=f"Пользователю {member.nick} выдана роль {role}", color= 0xffff00)
        await ctx.send(embed=embed)
@client.command()
async def call(ctx):
    if not ctx.author.voice:
        await ctx.message.delete()
        await ctx.send("Нужно находиться в голосовом канале", delete_after = 10)
    else:
        user = ctx.message.author
        Guild = ctx.message.guild.id
        channel = ctx.message.author.voice.channel.id
        em = discord.Embed(title= 'Клик(для выхода нажать на текстовый канал)', colour = user.color, description = f'https://discordapp.com/channels/{Guild}/{channel}')

        await ctx.message.delete()
        await ctx.send(embed = em, delete_after = 300)

@client.command()
async def getrole(ctx):

    testrole = discord.utils.get(ctx.author.guild.roles, name="📗Все")
    em = discord.Embed(title =f"Поставь реакцию 📗(green_book), чтобы получить роль {testrole.name}", color=0xffff00)
    em.set_image(url="https://media.discordapp.net/attachments/520600831058509830/609817001455779850/unknown.png")
    em.set_image(url="https://cdn.discordapp.com/attachments/520600831058509830/609817290195861525/unknown.png")
    em.set_footer(text=f"Вызванно {ctx.author.mention}")
    msg = await ctx.send(embed=em)
    await ctx.message.delete()
    def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '📗'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await asyncio.sleep(1)
        await msg.delete()
    else:
        await ctx.author.add_roles(testrole)
        await asyncio.sleep(1)
        await msg.delete()
@client.command()
@commands.has_permissions(administrator = True)
async def move(ctx, channel: discord.VoiceChannel = None, channel2: discord.VoiceChannel = None, member: discord.Member = None):
    await ctx.message.delete()
    if channel == None:
        pass
    if channel2 == None:
        pass
    if member == None:
        x = channel.members
        for member in x:
            await member.edit(voice_channel=channel2)
    else: await member.edit(voice_channel=channel2)


token = os.environ.get('BOT_TOKEN_1')
client.run(token, bot=True)
