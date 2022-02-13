import discord
from discord.ext import commands, tasks
import random


print("Hello")


client = commands.Bot(command_prefix='.')


@tasks.loop(seconds=5)
async def my_loop(ctx):
    await print('Hello World')

my_loop.start()


@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(
        "Don't Invite me unless u like a server full of nothing but 'hahas'"))
    print("I'm awake boss")

@client.command()
async def c(ctx):
    await ctx.send(f"```__COMMAND LIST__\n1- **.morty**: to get a reply (ping test)\n2- **.clear[amt]** to clear ["
                   f"amt] messages, "
                   f"default [amt]value is = 3\n3- **[DANGEROUS COMMAND]**: **.p** to fill a channel with an endless "
                   f"loop "
                   f"of 'haha's\n4- **.8ball [question]** to ask an 8ball question```")

@client.command()
async def morty(ctx):
    await ctx.send(f"Ayy {client.latency * 1000}ms")


@client.command()
async def p(ctx):
    h = 'haha\nhaha\nhaha\nhaha' * 50
    for i in range(0, 9000000000000000000000000000000000000000000000):
        await ctx.send(h)


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes – definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        "Don't count on it",
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.event
async def on_member_join(member):
    print(f"A new {member} has joined a server")


@client.event
async def on_member_remove(member):
    print(member + "has left a server")


client.run('NzIwNzc5NzExNTU4NTgyMjcy.XuK8ag.QBi70-2l4isHpTYhnRF5P1mT8xQ')
