# Ported from PepeBot for Userge by [NIKITA] @kirito6969
# Don't remove credits plox

from userge import userge, Message
from userge.plugins.fun.gali import check_and_send as lol

PENIS_TEMPLATE = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""


@userge.on_cmd("dick", about={
    'header': "Di*k Plugin",
    'description': "Dickifying everything :)"})
async def emoji_penis(e: Message):
    emoji = e.input_str
    message = PENIS_TEMPLATE
    if emoji:
        message = message.replace("🍆", emoji)

    await lol(e, message)
