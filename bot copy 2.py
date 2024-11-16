import discord
from bot_log  import flip_coin, gen_pass
from discord.ext import commands
import os
import random
import requests

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command
async def hi(ctx):
    await ctx.send("hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("🙂‍↕️")

@bot.command()
async def elementos(ctx):
    await ctx.send("rollos de papel, cajas de carton, botellas de plastico")

@bot.command()
async def reducir(ctx):
    await ctx.send("cajas de carton pequenñas, para elementos fragles que requieran envoltorios de plasticos recuerda reciclarlos en casa o derigirte a un lugar especialzado en reciclar")



@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


 
@bot.command()
async def motivaciones(ctx):
    motivacion = random.choice(os.listdir("image"))
    with open(f'image/{motivacion}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


bot.run("token")