import asyncio
import json
import os
import random
import time
import urllib.request
import wikipediaapi as wi
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('KEY_YOUTUBE')

bot = commands.Bot(command_prefix='>')
bot.message_counter = 0

client = discord.Client()

@bot.event
async def on_ready():
    print ('Run')
    await bot.change_presence(activity=discord.Streaming(name="Nani?", url="https://www.twitch.tv/fisicaendirecto"))

# Youtube Twice
@bot.command(name='twice')
# @commands.cooldown(1, 30, commands.BucketType.user)
async def subscriptores(ctx,username):
    data = urllib.request.urlopen("https://youtube.googleapis.com/youtube/v3/search?part=id&part=snippet&channelId=UCzgxx_DM2Dcb9Y1spb9mUJA&maxResults=2&order=relevance&q=" + username + "&key=" + KEY).read()
    nombre = json.loads(data)["items"][0]["snippet"]["title"]
    subs = json.loads(data)["items"][0]["id"]["videoId"]

    response = "Resultados para " + username + ":\n" + nombre.replace('&quot;', '"') + ": https://www.youtube.com/watch?v=" + subs
    await ctx.send(response)

# Youtube fromis
@bot.command(name='fromis')
# @commands.cooldown(1, 30, commands.BucketType.user)
async def subscriptorez(ctx,username):
    data = urllib.request.urlopen("https://youtube.googleapis.com/youtube/v3/search?part=id&part=snippet&channelId=UC8qO5racajmy4YgPgNJkVXg&maxResults=2&order=relevance&q=" + username + "&key=" + KEY).read()
    nombre = json.loads(data)["items"][0]["snippet"]["title"]
    subs = json.loads(data)["items"][0]["id"]["videoId"]

    response = "Resultados para " + username + ":\n" + nombre.replace('&quot;', '"') + ": https://www.youtube.com/watch?v=" + subs
    await ctx.send(response)

# Wikipedia
@bot.command(name='w')
# @commands.cooldown(1, 30, commands.BucketType.user)
async def w(ctx, *args):

    args = list(args)
    if args[0][0] == '-':
        language = args[0][1:]
        args.pop(0)
    else:
        language = 'es'

    wikipedia = wi.Wikipedia(language)
    term = ' '.join(args).title()
    page = wikipedia.page(term)

    if page.exists():
        end = page.summary.find('\n')
        await ctx.send(page.summary[:end])
        await ctx.send('Puedes leer más en: ' + page.fullurl)
    else:
        await ctx.send(f"No encontramos resultados. Pi, pi, pi.")

####################

last_used = 0
cooldown = 10

tuais = ['🤖 ```1, 3, 2:``` https://youtu.be/xGFEC0hUlnM```', '🤖 ```Last Waltz:``` https://youtu.be/sb27EfioKKw ', '🤖 ```Mooonlight```: https://youtu.be/Q8nCjQCvWD4', '🤖 ```Queen```: https://youtu.be/21BJa_LA9W4 👑', '🤖 ```Like OOH-AHH:``` https://youtu.be/0rtV5esQT6I', '🤖 ```Yes or Yes:``` https://youtu.be/mAKsZ26SabQ', '🤖 ```Baby Blue Love:``` https://youtu.be/KRE5FpVxZVQ', '🤖 ```La que le gusta a Jihyo:``` https://youtu.be/Fm5iP0S1z9w', '🤖 ```Is Sana gay?:``` https://youtu.be/rRzxEiBLQCA', '🤖 ```The Feels:``` https://youtu.be/f5_wn8mexmM', '🤖 ```Scientist:``` https://youtu.be/vPwaXytZcgI', '🍩: https://youtu.be/VcOSUOpACq0', '🤖 ```I\'ll show you:``` https://youtu.be/WW1BpABbzHs', '```🤖 A ti no.```', '```🤖 La tuya, por si acaso.```']
richi = ['Also... Tzuyu > fromis_9', 'Also... Tuais >> fromis_9', 'Also... MinaGOD', 'Also... Seulgi > Sae-rom']
numero = ['1', '2', '3', '4', '5', '6']

@bot.event
async def on_message(message):
    global last_used
    if message.author.bot:
        return
    if any(x in message.content for x in ["cerjio", "Cerjio"]):
      if time.time() > last_used+cooldown:
          msg = f'🤖 ```kyc, ctmr. Es Sergio, no \'cerjio\'.```'
          await message.channel.send(msg)
          last_used = time.time()
      else:
          return
    if any(x in message.content for x in ["sexo", "Sexo", "SEXO"]):
      if time.time() > last_used+cooldown:
          msg = f'🤖 ```Calla, virgen.```'
          await message.channel.send(msg)
          last_used = time.time() + 30
      else:
          return
    if any(x in message.content for x in ["virgen", "Virgen", "VIRGEN"]):
      if time.time() > last_used+cooldown:
          msg = f'🤖 ```No mientas.```'
          await message.channel.send(msg)
          last_used = time.time() + 30
      else:
          return
    if message.content.startswith('>tuais'):
      if time.time() > last_used+cooldown:
          await message.channel.send(random.choice(tuais))
          last_used = time.time()
      else:
          return
    if message.content.startswith('>random'):
      if time.time() > last_used+cooldown:
        await message.channel.send(random.choice(numero))
        last_used = time.time()
      else:
          return
    if message.content.startswith('>CAE'):
      if time.time() > last_used+cooldown:
          msg2 = '🤖 linktr.ee/caefisica'
          msgcal = '🤖 1: https://caefis.netlify.app/guias/pregrado/1/cbo104/\n2: https://caefis.netlify.app/guias/pregrado/2/cbo204/'
          msgfg= '🤖 1: https://caefis.netlify.app/guias/pregrado/1/cbe013/\n2: https://caefis.netlify.app/guias/pregrado/2/cbo207/'
          if 'calculo' in message.content:
            await message.channel.send(msgcal)
            last_used = time.time()
          if 'fg' in message.content:
            await message.channel.send(msgfg)
            last_used = time.time()
          if 'links' in message.content:
            await message.channel.send(msg2)
            last_used = time.time()
      else:
          return
    if any(x in message.content for x in ["matricula", "matrícula", "Matricula", "Matrícula", "MATRICULA", "MATRÍCULA"]):
      bot.message_counter += 1
      if time.time() > last_used+cooldown:
          msg = f'🤖 AAAAAAAAHHHH.'
          await message.channel.send(msg)
          last_used = time.time() + 30
      else:
          return
    if any(x in message.content for x in ["chinitas", "Chinitas", "CHINITAS", "kpop", "Kpop", "KPOP", "k-pop", "K-pop", "K-POP"]):
      if time.time() > last_used+cooldown:
          msg = f'🤖 Ya, pero...\nhttps://www.youtube.com/playlist?list=PLCzBTA_MIpqLDTKH9x14OtwJP7IMqi8AX'
          await message.channel.send(msg)
          last_used = time.time()
      else:
          return
    if any(x in message.content for x in ["david", "don"]) and any(x in message.content for x in ["bot", "davidbot"]):
      if time.time() > last_used+cooldown:
          msg = f'🤖 ```Bip, bop, kyc.\nApagando...```'
          await message.channel.send(msg)
          last_used = time.time() + 30
      else:
          return
    if message.content.startswith('>info'):
      if time.time() > last_used+cooldown:
          msg = '🤖\n```>twice [término]``` busca videos de Twice.\n```>w [término]``` busca info en Wikipedia.\n```>tuais``` muestra una canción random.\n```>random``` muestra un número al azar del 1 al 6.\n```>CAE [término]``` acepta valores como ```calculo```, ```fg``` y ```links```.\n```>forms``` muestra el formulario de Nelson.\n```>mat``` muestra cuántas veces se ha mencionado matrícula.\n\n```NOTA: El bot no contesta si alguien envía un comando múltiples veces.```'
          await message.channel.send(msg)
          last_used = time.time()
      else:
          return
    #if message.content.startswith('@22 Ariana'):
    #  if time.time() > last_used+cooldown:
    #    msg = f'🤖 No.'
    #    await message.channel.send(msg)
    #    last_used = time.time() + 30
    #  else:
    #      return
    #if message.content.startswith('>forms'):
    #  if time.time() > last_used+cooldown:
    #    msg = f'🤖 Acá está, Nelson, mi kong: https://docs.google.com/forms/d/1qZOvwIguWCKw31dzyrFRu21X54d4QYrrbsiQK60qwJQ/\n```Este mensaje es automático.```'
    #    await message.channel.send(msg)
    #    last_used = time.time() + 30
    #  else:
    #      return
    await bot.process_commands(message)

@bot.command()
async def mat(ctx):
    response = "Cantidad de veces que alguien ha dicho \"matrícula\": {}".format(ctx.bot.message_counter)
    await ctx.send(response)

SECRET_KEY = os.getenv("TOKEN")

bot.run(SECRET_KEY)