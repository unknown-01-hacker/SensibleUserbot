"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @MR_CE0
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/5e3a0b03f6f5af5b37490.jpg"
ALIVE_caption = "`Sensible Userbot IS:` **ONLINE**\n\n"
ALIVE_caption += "**SYSTEM STATUS**\n\n"
ALIVE_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n\n"
ALIVE_caption += "`DATABASE STATUS:` **Functional**\n\n"
ALIVE_caption += "**Current Branch** : `master`\n\n"
ALIVE_caption += "**Sensible  OS** : `3.14`\n\n"
ALIVE_caption += "**Current Sat** : `Sensible Userbot Sat-2.95`\n\n"
ALIVE_caption += f"**My master** : {DEFAULTUSER} \n\n"
ALIVE_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
ALIVE_caption += "**Alive now** \n\n"
ALIVE_caption += "Copyright By [CEOWHITEHATCRACKS](GitHub.com/spandey112)\n\n"
ALIVE_caption += "[Deploy SensibleUserbot](GitHub.com/)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def sensible(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)

@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def sensible(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
