import discord
from bot_log import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command
async def hello(ctx):
    await ctx.send("hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("🙂‍↕️")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

client.run("MTI5Njk4MzcwMDI4OTg4MDE1Nw.GB4kX2.J9V6GNBV1EwEZBbFJwJvSCktxn9qgwnGQzhuK4")
