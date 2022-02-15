from distutils import command
from http import client
import math
import re
from nextcord.ext import commands
import nextcord
import random

client = commands.Bot(command_prefix="!", help_command=None)

def sub(x: float, y: float):
    return x - y

def add(x: float, y: float):
    return x + y

def div(x: float, y: float):
    return x / y

def mult(x: float, y: float):
    return x * y

def rando(x: int, y: int):
    return random.randint


@client.command()
async def madd(ctx, x:float, y:float):
    res = add(x,y)
    await ctx.send(res)
@client.command()
async def msub(ctx, x:float, y:float):
    res = sub(x,y)
    await ctx.send(res)
@client.command()
async def mdiv(ctx, x:float, y:float):
    res = div(x, y)
    await ctx.send(res)
@client.command()
async def mmult(ctx, x:float, y:float):
    res = mult(x, y)
    await ctx.send(res)


@client.event
async def on_ready():
    print(f"{client.user.name} is online")

client.run("NzQ3NTg3Nzk4OTY1NTUxMTY2.X0RDZA.tPf3FfORzkrkU13dANN78ssKOFo")