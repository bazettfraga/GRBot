import discord
import asyncio
import random
import time

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def attack(a,b):
    if a<11:
        return 0
    if a<16:
        return 2
    if a<20:
        return 3
    if a==20 and b == "mod":
        return 3
    if a==20 and b == "nat":
        return 4
    
@client.event
async def on_message(message):
    if message.content.startswith('$attack'):
        args = message.content.lstrip('$attack')
        try:
            if not args:
                pass
            else:
               val = list(map(arg.split(' ')))
        except ValueError:
            pass
        
        embed = discord.Embed(description=f'{message.author.mention} your attack minimum is:', color=0x00e6b8)     
            minimum = attack(val[0],val[1]) 
            descString = f"**{minimum}**"
            embed.add_field(name=f"Result", value=descString, inline=True)
        #embed.add_field(name="Field1", value="Test", inline=False)
        await client.send_message(message.channel, embed=embed)

#client.run('MjE5NjEwNDc3MTA4NTI3MTI1.DppR9Q.nW-jCuD-6ruwF1Qlb2KeJNi_h-Q')
while True:
    try:
        client.loop.run_until_complete(client.start('MjE2OTg1NzAxNTk2NjU5NzEz.DyvFaw.Brz52sjdPt147gIftoe6rNhILis'))
    except BaseException:
        time.sleep(5)