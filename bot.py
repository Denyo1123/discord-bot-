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
forum_words = ["forum", "Форум", "foruma"]
biip_words = ["help", "pomosht", "помощ", "помогне", "pomognetemi", "iskam pomosht", "помогнетеми" ]
help_1 = [
  "използвайте тикети",
  "отвори тикет за помощ"
]

client = discord.Client()

@client.event
async def  on_ready():
  print('we have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content 

  if message.content.startswith('$beep'):
    await message.channel.send('Boop!')  

  if any(word in msg for word in site_words):
    await message.channel.send('https://hytale-bg.com/') 
  
  if any(word in msg for word in forum_words):
    await message.channel.send('https://hytale-bg.com/community/index.php')

  if any(word in msg for word in biip_words):
    await message.channel.send(random.choice(help_1))

  if any(word in msg for word in fb_words):
    await message.channel.send('https://www.facebook.com/HytaleBulgaria')



client.run(os.getenv('TOKEN'))