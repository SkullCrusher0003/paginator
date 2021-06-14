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
1. create your python file
2. type `pip install dcord` in the terminal
3. put the following snippet into your code `import dcord`
4. **button paginate**: 
	```python
	embeds = [] # list of embeds
	dcord.btn.msc.paginate(bot,ctx,embeds)
	```
5. **reaction paginate**: 
	```python
	embeds = [] # list of embeds
	dcord.msc.paginate(bot,ctx,embeds)
	```
6. Replace `<TOKEN>` with your bot's token
7. Edit the embeds as necessary / add more
8. Run it!

## More To Know
- Adding checks to the `wait_for` statement will allow you to restrict buttons usage for a single user
- If you're gonna be using this in a case where multiple people might be using it at the same time, consider putting a check to get the `message id == mainMessage.id`
- reactions can also be checked for using `wait_for`

### About Us
I'm Skull, `Skull Crusher#9515` on Discord. I am a high schooler who likes coding :D

I'm Kaneki `Kaneki#9876` on Discord. I'm a freelacner who gets bored easily, hit me up if you're bored too.

- YouTube: [AV Creators Coding](https://www.youtube.com/channel/UCcWfrKzR9cm-QKUZKAcxLXQ)
- Y4D Discord Bot: [Y4D](https://dsc.gg/y4d)
- Programming Server: [The Coders Arena](https://dsc.gg/codersarena)
