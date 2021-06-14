# Paginator - discord_components
This repository is just an example code for how to carry out pagination using the discord_components library for python. Its fairly easy, and once you get the hang of it you can modify it as per your choice :D
The code contains an in-built timeout feature, where after 10 seconds of inactivity, the buttons are disabled automatically!

![git.gif](https://github.com/SkullCrusher0003/paginator/blob/main/git.gif)

## Pre Requisites
- Basic knowledge of Python
- Python 3.7+ installed on your computer
- Discord Account

## Libraries
Simply install these by running `pip install <library name>` in your terminal
- discord.py
- asyncio
- discord_components

## Usage
1. Download the pagination.py file
2. Replace `<TOKEN>` with your bot's token
3. Edit the embeds as necessary / add more
4. Edit button styles if necessary
5. Run it!

## More To Know
- Adding checks to the `wait_for` statement will allow you to restrict buttons usage for a single user
- If you're gonna be using this in a case where multiple people might be using it at the same time, consider putting a check to get the `message id == mainMessage.id`

### About Me
I'm Skull, Skull Crusher#9515 on Discord. I am a high schooler who likes coding :D

YouTube: [AV Creators Coding](https://www.youtube.com/channel/UCcWfrKzR9cm-QKUZKAcxLXQ)
Y4D Discord Bot: [Y4D](https://dsc.gg/y4d)
