#MTE5ODA2MjkxNjc4MDQzNzU5NA.GJ5UO_.W3HspdpqanbGrHIiq09eoQEB2u6tjEZ3Yc1va0
import discord
from main import gen_pass
from discord.ext import commands
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx, count_heh = 5):
    await ctx.send("bye" * count_heh)
    
@bot.command()
async def password(ctx, pass_length = 10):
    await ctx.send(gen_pass(pass_length))


bot.run("MTE5ODA2MjkxNjc4MDQzNzU5NA.GJ5UO_.W3HspdpqanbGrHIiq09eoQEB2u6tjEZ3Yc1va0")