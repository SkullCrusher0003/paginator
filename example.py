#Importing libraries, these are all we need
import discord, asyncio, dcord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

#Using commands.Bot, you can use discord.Client also
bot = commands.Bot(
    command_prefix = "sc." #Put your prefix in place of "sc."
)
#Components init
DiscordComponents(bot)

#On ready event
@bot.event
async def on_ready():
    print(f"{bot.user} Online")

@bot.command()
async def buttonpagainate(ctx):
  embed1 = discord.Embed(title="Paginate Example",description="Paginate example page 1",color=ctx.author.color)
  embed1.add_field(name="button paginate",value="A stylish modern paginator")
  embed2 = discord.Embed(title="Paginate Example",description="Paginate example page 2",color=ctx.author.color)
  embed2.add_field(name="reaction paginate",value="A fun easy to access way of pagination")
  embeds = [embed1,embed2] # list of embeds
  dcord.btn.msc.paginate(bot,ctx,embeds)
    
@bot.command()
async def reactpaginate(ctx):
  embed1 = discord.Embed(title="Paginate Example",description="Paginate example page 1",color=ctx.author.color)
  embed1.add_field(name="button paginate",value="A stylish modern paginator")
  embed2 = discord.Embed(title="Paginate Example",description="Paginate example page 2",color=ctx.author.color)
  embed2.add_field(name="reaction paginate",value="A fun easy to access way of pagination")
  embeds = [embed1,embed2] # list of embeds
  dcord.msc.paginate(bot,ctx,embeds)
    
bot.run("<TOKEN>")
