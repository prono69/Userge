# Rewrote poto by code-rgb

import asyncio
import os
from pyrogram.types import InputMediaPhoto
from userge import Config, Message, userge

CHANNEL = userge.getCLogger(__name__)

# photo stealer :)

@userge.on_cmd(
    "poto",
    about={
        "header": "use this plugin to get photos of user or chat",
        "description": "fetches upto 100 photos of a user or chat",
        "flags": {"-l": "limit, max. 100", "-p": "for photo at particular postion"},
        "examples": [
            "{tr}poto",
            "{tr}poto [reply to chat message]",
            "{tr}poto @midnightmadwalk -p5\n    (i.e sends photo at position 5)",
            "{tr}poto @midnightmadwalk -l5\n    (i.e sends an album of first 5 photos)",
        ],
    },
)
async def poto_x(message: Message):
    chat_id = message.chat.id
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    await message.edit("`Fetching photos ...`")
    if reply:
        input_ = reply.from_user.id
    elif message.filtered_input_str:
        input_ = message.filtered_input_str.strip()
        if len(input_.split()) != 1:
            await message.err("<b>Provide a valid ID or username</b>", del_in=5)
            return
    else:
        input_ = chat_id
    type_, peer_id, f_id = await chat_type_(message, input_)
    if peer_id == 0:
        await message.err(type_, del_in=7)
        return
    if type_ in ("group", "supergroup", "channel") and message.client.is_bot:
        photo_ = await userge.bot.download_media(f_id)
        await userge.bot.send_photo(chat_id, photo_, reply_to_message_id=reply_id)
        os.remove(photo_)
        await message.delete()
        return
    flags_ = message.flags
    if "-p" in flags_:
        pos_ = flags_.get("-p", 0)
        if not str(pos_).isdigit():
            await message.err('"-p" Flag only takes integers', del_in=5)
            return
        await send_single(message, peer_id=peer_id, pos=int(pos_), reply_id=reply_id)
    elif "-l" in flags_:
        get_l = flags_.get("-l", 0)
        if not str(get_l).isdigit():
            await message.err('"-l" Flag only takes integers', del_in=5)
            return
        media, media_group = [], []
        async for photo_ in message.client.iter_profile_photos(
            peer_id, limit=min(int(get_l), 100)
        ):
            media.append(InputMediaPhoto(photo_.file_id))
            if len(media) == 10:
                media_group.append(media)
                media = []
        if len(media) != 0:
            media_group.append(media)
        if len(media_group) == 0:
            # Happens if bot doesn't know the user
            await message.delete()
            return
        try:
            for poto_ in media_group:
                await userge.send_media_group(chat_id, media=poto_)
                await asyncio.sleep(2)
        except FloodWait as e:
            await asyncio.sleep(e.x + 3)
        except Exception as err:
            await CHANNEL.log(f"**ERROR:** `{str(err)}`")
    else:
        await send_single(message, peer_id=peer_id, pos=1, reply_id=reply_id)
    await message.delete()
