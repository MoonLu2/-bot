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

# Команды бота
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('+commands'):
        await message.channel.send('''
        
        +hello - say Hi!        
        +bye - say goodbye
        +rsymbols - pick a symbol randomly
        +password - shhhhh! never say the password...
        
        ''')


    if message.content.startswith('+hello'):
            await message.channel.send("Hi!")
    elif message.content.startswith('+bye'):
        await message.channel.send("\\-_-\\")
        exit(0)
    elif message.content.startswith('+rsymbols'):
        await message.channel.send(symbol_gen())
    elif message.content.startswith('+password'):
        await message.channel.send('''
        Password here...
        ''')
        await message.channel.send(generate(15))

   # Урок 6: Советы о том как избежать загрязнения в природе
    if message.content.startswith('+saveplanet'):
        tips_list =  ['Save plastic. It will be useful to make many things.', 'Every thing like plastic trash into correct bin.', 'Almost everything can be reused.']

        await message.channel.send('Tips for saving planet:')
        for i in tips_list:
            await message.channel.send(f'- {i}')
    await message.channel.send('type +commands if you forgot possible commands.')

client.run("TOKEN")
