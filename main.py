import discord
import os
import random

fb_words = [
  "fb", 
  "stranica", 
  "face", 
  "feis",
  "фб",
  "фейс",
  "страница"

]
site_words = ["sait", "site", "сайт" ]
shop_words = ["vip", "mega", "shop", "вип"]
biip_words = ["help", "pomosht", "помощ", "помогне", "pomognetemi", "iskam pomosht", "помогнетеми" ]
ip_words = ["ip", "ип", "даийте ми ип" ]
vote_word = ["vote", "вот", ]

help_1 = [
  "използвайте тикети",
  "отвори тикет за помощ"
]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event

async def  on_ready():

  activity = discord.Game(name="ClassicCraft")
  print('we have logged in as {0.user}'
  .format(client))
  activity = discord.Game(name="ClassicCraft")

@client.event

async def on_message(message):

  if message.author == client.user:
    return

  msg = message.content 

  if message.content.startswith('motherfucker'):
    await message.channel.send('Не работи пробвай пак по късно')  

  if any(word in msg for word in site_words):
    await message.channel.send('https://hytale-bg.com/') 
  
  if any(word in msg for word in shop_words):
    await message.channel.send('https://hytale-bg.com/community/index.php')

  if any(word in msg for word in biip_words):
    await message.channel.send(random.choice(help_1))

  if any(word in msg for word in fb_words):
    await message.channel.send('https://www.facebook.com/HytaleBulgaria')

  if any(word in msg for word in ip_words):
    await message.channel.send('0.0.0.0:25565')

  if any(word in msg for word in vote_word):
    await message.channel.send('вот сайт')


     
client.run(os.getenv('TOKEN'))