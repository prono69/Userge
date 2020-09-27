"""P*rnhub Comment"""
# @Mrconfused [catuserbot] for the idea of nekobot API
# BY code-rgb [https://github.com/code-rgb]


import os
import requests
import re
from validators.url import url
from html_telegraph_poster.upload_images import upload_image
from userge import userge, Message, Config

@userge.on_cmd("ph", about={
    'header': "P*rnhub Comment",
    'description': "Creates a P*rnhub Comment of Replied User With Custom Name",
    'usage': "{tr}ph Name , [reply or reply with text]",
    'examples': [
        "{tr}ph Did they ever get the pizza?",
        "{tr}ph David , Did they ever get the pizza?",
        "{tr}ph David , "]}, check_downpath=True)
async def ph_comment(message: Message):
    """ Create P*rnhub Comment for Replied User """
    replied = message.reply_to_message
    if replied:
        user = replied.forward_from if replied.forward_from else replied.from_user
        if "," in message.input_str:
            u_name, msg_text = message.input_str.split(',', 1)
            name = u_name.strip()
            comment = msg_text or replied.text
        else:
            if user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.first_name
            comment = message.input_str or replied.text
    else:
        await message.err("```Input not found!...```", del_in=3)
        return
    await message.delete()
    await message.edit("```Creating A PH Comment 😜```", del_in=1)
    comment = deEmojify(comment)


    if user.photo:
        pfp_photo = user.photo.small_file_id
        file_name = os.path.join(Config.DOWN_PATH, "profile_pic.jpg")
        picture = await message.client.download_media(
            pfp_photo,
            file_name=file_name
        )
        loc_f = upload_image(picture)
        os.remove(picture)
    else:
        loc_f = "https://telegra.ph/file/9844536dbba404c227181.jpg"
    path = await phcomment(loc_f, comment, name)
    if path == "ERROR":
        return await message.edit("😔 Something Wrong see Help!", del_in=2)
    chat_id = message.chat.id
    await message.delete()
    await message.client.send_photo(
        chat_id=chat_id,
        photo=path,
        reply_to_message_id=replied.message_id
    )


async def phcomment(text1, text2, text3):
    site = "https://nekobot.xyz/api/imagegen?type=phcomment&image="
    r = requests.get(f"{site}{text1}&text={text2}&username={text3}").json()
    urlx = r.get("message")
    ph_url = url(urlx)
    if not ph_url:
        return "ERROR"
    return urlx


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")
 
# RETURNS a "string" so don't use with await
def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)
 