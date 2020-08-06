from telethon import events
from userbot import ALIVE_NAME
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import admin_cmd
bot = javes = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
from telethon.events import ChatAction
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from uniborg.on.util import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

javes = bot

async def get_user_from_event(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.bot.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"`{DEFAULTUSER}`: ** Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.bot.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.bot.get_entity(user)
        except Exception as err:
            return await event.edit("Failed \n **Error**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.bot.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
   
from userbot import bot, bot

                    
                   

#command(admin_cmd(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
@borg.on(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def startgban(event):
        await event.edit("`In Process`")   
        await asyncio.sleep(0.5)
        await event.edit(f"`{DEFAULTUSER}:` **Requesting  to gban user! #GBAN**")
   if event.is_private::       
   	user = chat ; reason = pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await event.edit(f"`{DEFAULTUSER}:`**Error! Unknown user.**")
   if user:      
        if user.id == 709723121:     
    	             return await event.edit(f"`{DEFAULTUSER}:`**Error! cant gban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute            
        except:
   	     pass
        try:
          await bot(BlockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await bot.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await event.edit_permissions(i, user, view_messages=False)          
                 a += 1
                 await event.edit(f"`{DEFAULTUSER}:` **Requesting  to gban user!\nGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await event.edit(f"`{DEFAULTUSER}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await event.edit(f"`{DEFAULTUSER}:`**Error! User probably already gbanned.**")
   except:
    	pass
   return await event.edit(f"`{DEFAULTUSER}:` **Gbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , Blocked user and added to Gban watch **") 
        



#@command(admin_cmd(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
@borg.on(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def regressgban(event):
    	await event.edit("`processing...`")   
        await asyncio.sleep(0.5)
        await event.edit(f"`{DEFAULTUSER}:` **Requesting  to ungban user!**")
   if event.is_private::       
   	user = chat ; reason = pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await event.edit(f"`{DEFAULTUSER}:`**Error! Unknown user.**")
   if user:      
        if user.id == 709723121:     
    	             return await event.edit(f"`{DEFAULTUSER}:`**Error! cant ungban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
   	     pass
        try:
          await bot(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await bot.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await event.edit_permissions(i, user, send_messages=True)          
                 a += 1
                 await event.edit(f"`{DEFAULTUSER}:` **Requesting  to ungban user!\nunGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await event.edit(f"`{DEFAULTUSER}:` **Reply to a user !! **")        
   try:
     if ungmute(user.id) is False:
            return await event.edit(f"`{DEFAULTUSER}:`**Error! User probably already ungbanned.**")
   except:
    	pass
   return await event.edit(f"`{DEFAULTUSER}:` **UnGbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , UnBlocked and removed user from Gban watch **") 
        
