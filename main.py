import discord
from bot_logic import generate
from random_symbol import symbol_gen

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('+hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('+bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('+rsymbols'):
        await message.channel.send(symbol_gen())
    elif message.content.startswith('+password'):
        await message.channel.send('''
        Password here...
        ''')
        await message.channel.send(generate(15))
    else:
        await message.channel.send(message.content)

client.run("MTE5MzA5Mzg1ODAzMzE0Nzk5NA.GWZpYE.M7otn5DVbsqPdNUNbHWIXwGNPhnpMMMWKaUIRo")
