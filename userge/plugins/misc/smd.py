"""Find Songs Fast"""
# Made by- @DeletedUser420 idea- @AnInnocentboy
 
 
from pyrogram.errors import BadRequest
from userge import Message, userge
from userge.utils import get_file_id_of_media
 
 
@userge.on_cmd(
    "smd",
    about={
        "header": "Search from already uploaded 1M Songs",
        "usage": ".smd lady gaga - poker face",
    },
)
async def song_search(message: Message):
    """get songs from channel"""
    song = message.input_str
    if not song:
        await message.err("Provide a song name or artist name to search", del_in=10)
        return
    search = await message.edit("🔍 __Searching For__ **{}**".format(song))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in userge.search_messages(
            -1001271479322, query=song, limit=1, filter="audio"
        ):
            f_id = get_file_id_of_media(msg)
    except BadRequest:
        await search.edit(
            "Join [THIS](https://t.me/joinchat/DdR2SUvJPBouSW4QlbJU4g) channel first"
        )
        return
    if not f_id:
        await search.edit("⚠️ Song Not Found !", del_in=5)
        return
    await userge.send_audio(chat_id, f_id)
    await search.delete()
 
    
@userge.on_cmd(
    "idez",
    about={
        "header": "Deezer but yeah inline :)",
        "usage": "{tr}idez [text]",
    },
)
async def ideez_(message: Message):
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if message.input_str:
        input_query = message.input_str
    elif reply:
        if reply.text:
            input_query = reply.text
        elif reply.caption:
            input_query = reply.caption
    if not input_query:
        return await message.err("Input Not Found", del_in=5)

    x = await userge.get_inline_bot_results(
            "@DeezerMusicBot", input_query
    )
    try:
        await message.delete()
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=x.query_id,
            result_id=x.results[0].id,
            reply_to_message_id=reply_id
        )
    except (IndexError, BadRequest):
        await message.err("song not found", del_in=5)    