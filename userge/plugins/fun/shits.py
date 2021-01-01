# Original Author @DneZyeK
# Ported by @kirito6969 :) Thanks for the help @DeletedUser420

"""Image to dot
	   .doti <count> + reply to img for COLOUR dot
	   .doty <count> + reply to img for BW dot
	   the bigger, the slower and bugger
	   recommended not more 1000"""

import os
import logging

from re import sub
from requests import get
from PIL import Image, ImageDraw
import io
import asyncio
from userge import userge, Message
from userge.utils import runcmd

logger = logging.getLogger(__name__)


@userge.on_cmd("tgs", about={
    'header': "Destroy Sticker",
    'description': "Destroy your sticker"})
async def lmao(message: Message):
	reply = message.reply_to_message
	if not reply.sticker:
		await message.edit("`Reply to a animated sticker`", del_in=3)
		return
	stkr = await reply.download("tgs.tgs")
	await message.edit("`Fixing this sticker...`")
	await runcmd(f"lottie_convert.py {stkr} json.json")
	os.remove(stkr)
	with open("json.json","r") as json:
		jsn = json.read()
		jsn = jsn.replace('[1]','[20]').replace('[2]','[30]').replace('[3]','[40]').replace('[4]','[50]').replace('[5]','[60]')
	
	with open("json.json","w") as outfile:
		outfile.write(jsn)
	await runcmd("lottie_convert.py json.json tgs.tgs")
	await message.client.send_sticker(message.chat.id, "tgs.tgs")
	os.remove("json.json")
	os.remove("tgs.tgs")
	await message.delete()


@userge.on_cmd("ip", about={
  'description': "Find information about an ip address"})
async def ipcmd(message: Message):
        """Use as .ip <ip> (optional)"""
        ip = message.input_str
        if not ip:
        	await message.edit("`Give me ip address :(`", del_in=3)

        lookup = get(f"http://ip-api.com/json/{ip}").json()
        fixed_lookup = {}

        for key, value in lookup.items():
            special = {"lat": "Latitude", "lon": "Longitude", "isp": "ISP", "as": "AS", "asname": "AS name"}
            if key in special:
                fixed_lookup[special[key]] = str(value)
                continue

            key = sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", key)
            key = key.capitalize()

            if not value:
                value = "None"

            fixed_lookup[key] = str(value)

        text = ""

        for key, value in fixed_lookup.items():
            text = text + f"<b>{key}:</b> <code>{value}</code>\n"

        await message.edit(f"<b><i><u>IP Information for PepeBot</u></i></b>\n\n{text}")



	   
@userge.on_cmd("doti", about={
  'header': "Dotify images",
  'description': "this is for colour dot"})
async def dotifycmd(message: Message):
		"""Image to RGB dots"""
		mode = False
		reply, pix = await parse(message)
		if reply:
			await dotify(message, reply, pix, mode)

@userge.on_cmd("doty", about={
  'description': "This is for black & white dots"})
async def dotificmd(message: Message):
		"""Image to BW dots """
		mode = True
		reply, pix = await parse(message)
		if reply:
			await dotify(message, reply, pix, mode)			
			
	
	
async def parse(message: Message):
	reply = message.reply_to_message
	if not reply:
		await message.edit("<b>Reply to Image!</b>", del_in=3)
		return None, None
	args = message.input_str.split(" ", 1)
	pix = 100
	if args:
		args=args[0]
		if args.isdigit():
			pix = int(args) if int(args) > 0 else 100
	return reply, pix

async def dotify(message: Message, reply, pix, mode):
	await message.edit("<b>Putting dots...</b>", del_in=2)
	count = 24
	im_ = Image.open(await reply.download("bytes.png"))
	if im_.mode == "RGBA":
		temp = Image.new("RGB", im_.size, "#000")
		temp.paste(im_, (0, 0), im_)
		im_ = temp
		
	im = im_.convert("L")
	im_ = im if mode else im_
	[_.thumbnail((pix, pix)) for _ in[im, im_]]
	w, h = im.size
	img = Image.new(im_.mode, (w*count+(count//2), h*count+(count//2)), 0)
	draw = ImageDraw.Draw(img)
	
	def cirsle(im, x, y, r, fill):
		x += r//2
		y += r//2
		draw = ImageDraw.Draw(im)
		draw.ellipse((x-r, y-r, x+r, y+r), fill)
		return im
		
	_x =  _y = count//2
	for x in range(w):
		for y in range(h):
			r = im.getpixel((x, y))
			fill = im_.getpixel((x, y))
			cirsle(img, _x, _y, r//count, fill)
			_y += count
		_x += count
		_y = count//2
	 
	out = io.BytesIO()
	out.name = "out.png"
	img.save(out)
	out.seek(0)
	await message.client.send_photo(message.chat.id, photo=out)
	await message.delete()
