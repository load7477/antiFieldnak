import discord
import warnings, random, asyncio
from discord.ui import InputText, Modal
from discord.commands import Option
from discord.ui import Button, View, Select
import re
import db as anti
warnings.filterwarnings("ignore", category=DeprecationWarning)
intents = discord.Intents.all()
client = discord.Bot(intents=intents)


@client.event
async def on_member_join(member):
    userinfo = anti.getuserinfo(member.id)
    count = 3
    try:
        if userinfo['count'] >= int(count):
            print('1', userinfo['count'])
            await member.send("들낙 3번 누적. 서버 접속 불가")
            await member.kick(reason="들낙 3번 ")
        else: 
            print('2', userinfo['count'])
    except:
        print("DB 생성작업 으로 인해 패스")
        pass

@client.event
async def on_member_remove(member):
    userinfo = anti.getuserinfo(member.id)
    anti.addcount(userinfo, member.id)
    

client.run("")