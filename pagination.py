#Importing libraries, these are all we need
import discord, asyncio
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
    print("Paginator Online")

#Pagination Embeds...
##Like usual, just type out embeds in the discord.Embed() format and be sure to keep the names different
embedOne = discord.Embed(
    title = "Page #1", #Any title will do
    description = "This is page one!" #Any description will be fine
)
embedTwo = discord.Embed(
    title = "Page #2",
    description = "This is page two!"
)
embedThree = discord.Embed(
    title = "Page #3",
    description = "This is page three!"
)
#I have not added fields / authors, you're free to do so and works fine anyways

#Get all embeds into a list
paginationList = [embedOne, embedTwo, embedThree] #Just append all embed names in here, in the right order ofcourse

#Main command
@bot.command(
    name = "pagination",
    aliases = ["pages"]
)
async def pagination(ctx):
    #Sets a default embed
    current = 0
    #Sending first message
    #I used ctx.reply, you can use simply send as well
    mainMessage = await ctx.reply(
        "**Pagination!**",
        embed = paginationList[current],
        components = [ #Use any button style you wish to :)
            [
                Button(
                    label = "Prev",
                    id = "back",
                    style = ButtonStyle.red
                ),
                Button(
                    label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                    id = "cur",
                    style = ButtonStyle.grey,
                    disabled = True
                ),
                Button(
                    label = "Next",
                    id = "front",
                    style = ButtonStyle.red
                )
            ]
        ]
    )
    #Infinite loop
    while True:
        #Try and except blocks to catch timeout and break
        try:
            interaction = await bot.wait_for(
                "button_click",
                check = lambda i: i.component.id in ["back", "front"], #You can add more
                timeout = 10.0 #10 seconds of inactivity
            )
            #Getting the right list index
            if interaction.component.id == "back":
                current -= 1
            elif interaction.component.id == "front":
                current += 1
            #If its out of index, go back to start / end
            if current == len(paginationList):
                current = 0
            elif current < 0:
                current = len(paginationList) - 1

            #Edit to new page + the center counter changes
            await interaction.respond(
                type = InteractionType.UpdateMessage,
                embed = paginationList[current],
                components = [ #Use any button style you wish to :)
                    [
                        Button(
                            label = "Prev",
                            id = "back",
                            style = ButtonStyle.red
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.red
                        )
                    ]
                ]
            )
        except asyncio.TimeoutError:
            #Disable and get outta here
            await mainMessage.edit(
                components = [
                    [
                        Button(
                            label = "Prev",
                            id = "back",
                            style = ButtonStyle.red,
                            disabled = True
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.red,
                            disabled = True
                        )
                    ]
                ]
            )
            break
#Run bot
bot.run("<TOKEN>")
