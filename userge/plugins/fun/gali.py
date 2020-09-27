# by @krishna_singhal

import asyncio
from random import choice
from userge import userge, Message


async def check_and_send(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(
            message.delete(),
            replied.reply(*args, **kwargs)
        )
    else:
        await message.edit(*args, **kwargs)


@userge.on_cmd("gali$", about={'header': "slang to a bitch with power of bot"})

async def gali_func(message):
	gali = choice(gaali)
	stickers = choice(stickers_ids)
	await check_and_send(message, "<code>{}</code>".format(gali), parse_mode='html')
	await message.reply_sticker(sticker="".join(stickers))



gaali = (
    "Abey Ja Na Randi",
    "Abey Ja Na Madarchod",
    "Tu mach gey",
    "You gey gey gey gey gey gey gey gey",
    "Chut mai talwar ghusauga bc chut fat jaegi aur usme se itna khoon niklega ki maza hi ajaega deklena sale sasti jhat",
    "Loda lasun madrchod teri maa ki chut gasti ama ka chutia bacha teri maa ko chod chod k pagal kar dunga maa k lody kisi sastiii randii k bachy teri maa ki choot main teer maarun gandu harami",
    "Maa ke bhosde se bahr aja fir baap se zuban da teri maa ki chut chod chod ke bhosdabnadu madarchod aur uske upar cement lagadu ki tere jesa gandu insaan kabhi bahr na a ske esi gandi chut mai se",
    "Teri college jati baji ka road pey rape karongandu ki olaad haram ki nasal papa hun tera bhen pesh kar ab papa ko teri maa kkale kuss main kisi!",
    "Maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI",
    "Tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike",
    "maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha",
    "Drugs tere gand Me dalunga ki tatti nahi nikle maadarchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi.",
    "Sale tere gand ke balo pe tel laga ke jala du me teko",
    "Tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga",
    "Tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode",
    "Tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu",
    "Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe")
stickers_ids = (
    "CAADBQADlgADje9BLb-DhGHGfbx6FgQ",
    "CAADBQADBgAD-xNYN79jb8hXjxhyFgQ",
    "CAADBQADIwAD-xNYN_ZX0TUQ33b5FgQ",
    "CAADBQADtQADje9BLVtdHXr6pvQfFgQ",
    "CAADBQADzwADje9BLT69DmYKUwd_FgQ",
    "CAADBQADAQADh68vOP4aZy5tiSXlFgQ",
    "CAADBQADKAADh68vOAABLBgqCrYYFRYE",
    "CAADBQADLgADh68vODlskrbAM9dEFgQ")