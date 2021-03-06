import os

from anekos import NekosLifeClient, NSFWImageTags, SFWImageTags
from pyrogram.errors import MediaEmpty, WebpageCurlFailed
from wget import download
from userge import Message, userge

client = NekosLifeClient()

NSFW = [x for x in dir(NSFWImageTags) if not x.startswith("__")]
SFW = [z for z in dir(SFWImageTags) if not z.startswith("__")]


neko_help = "<b>NSFW</b> :  "
for i in NSFW:
    neko_help += f"<code>{i.lower()}</code>   "
neko_help += "\n\n<b>SFW</b> :  "
for m in SFW:
    neko_help += f"<code>{m.lower()}</code>   "


@userge.on_cmd(
    "ne",
    about={
        "header": "Get NSFW / SFW stuff from nekos.life",
        "flags": {"ne": "For random NSFW"},
        "usage": "{tr}ne\n{tr}ne -nsfw\n{tr}ne [Choice]",
        "Choice": neko_help,
    },
)
async def neko_life(message: Message):
    choice = message.input_str
    if "-nsfw" in message.flags:
    	link = (await client.random_image(nsfw=True)).url
    elif choice:
        input_choice = (choice.strip()).upper()
        if input_choice in SFW:
            link = (await client.image(SFWImageTags[input_choice])).url
        elif input_choice in NSFW:
            link = (await client.image(NSFWImageTags[input_choice])).url
        else:
            await message.err(
                "Choose a valid Input !, See Help for more info.", del_in=5
            )
            return
    else:
        link = (await client.random_image()).url

    await message.delete()

    try:
        await send_nekos(message, link)
    except (MediaEmpty, WebpageCurlFailed):
        link = download(link)
        await send_nekos(message, link)
        os.remove(link)


async def send_nekos(message: Message, link: str):
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if link.endswith(".gif"):
        #  Bots can't use "unsave=True"
        bool_unsave = not message.client.is_bot
        await message.client.send_animation(
            chat_id=message.chat.id,
            animation=link,
            unsave=bool_unsave,
            reply_to_message_id=reply_id,
        )
    else:
        await message.client.send_photo(
            chat_id=message.chat.id, photo=link, reply_to_message_id=reply_id
        )

        