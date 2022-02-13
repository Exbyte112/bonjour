from email import message
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Yo!')
    
@client.event
async def on_member_join(member):
    await member.send('Welcome{member}')

client.run('NzIwNzc5NzExNTU4NTgyMjcy.XuK8ag.2_ITvGN5HU2Xn7vPI4vAdNfZA38')
