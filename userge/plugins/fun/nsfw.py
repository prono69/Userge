import os
import urllib
import requests
import asyncio
from userge import userge , Message, Config
from userge.plugins.fun.nekos import send_nekos

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"


@userge.on_cmd("boobs", about={
    'header': "Find some Boob",
    'usage': "{tr}boobs"})
async def boobs(message: Message):
    if not os.path.isdir(Config.DOWN_PATH):
        os.makedirs(Config.DOWN_PATH)
    pic_loc = os.path.join(Config.DOWN_PATH, "bobs.jpg")
    await message.edit("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await message.edit("`Sending some big bobs 🌚...`")
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await message.client.send_photo(message.chat.id, photo=pic_loc)
    os.remove(pic_loc)
    await message.delete()

@userge.on_cmd("butts", about={
    'header': "Find some Butts",
    'usage': "{tr}butts"})
async def butts(message: Message):
    if not os.path.isdir(Config.DOWN_PATH):
        os.makedirs(Config.DOWN_PATH)
    pic_loc = os.path.join(Config.DOWN_PATH, "bobs.jpg")
    await message.edit("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await message.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await message.client.send_photo(message.chat.id, photo=pic_loc)
    os.remove(pic_loc)
    await message.delete()
    
@userge.on_cmd("hentai", about={
    'header': "Random hentai pics",
    'usage': "{tr}hentai"})
async def butts(message: Message):
    nsfw = requests.get("https://api.computerfreaker.cf/v1/hentai", headers={"User-Agent": user_agent}).json()
    link = nsfw.get("url")
    await send_nekos(message, link)
    await message.delete()
    
@userge.on_cmd("lewdn", about={
    'header': "Random lewd neko pics",
    'usage': "{tr}lewdn"})
async def dva(message: Message):
    nsfw = requests.get("https://nekos.life/api/lewd/neko").json()
    link = nsfw.get("neko")
    if not url:
        await message.edit("`No lewd neko found. U stay horni now :)`", del_in=4)
        return
    await send_nekos(message, link)
    await event.delete()    