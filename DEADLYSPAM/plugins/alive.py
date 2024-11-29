import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://envs.sh/Ynn.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝐒𝐈𝐃𝐇𝐈 𝗫 𝐌𝐔𝐒𝐈𝐂 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴋɪɴɢ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/BRANDED_KHUSHI"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/SIDHI_SUPPORT")], [Button.url("• ʀᴇᴘᴏ •", "https://t.me/SIDHI_MUSIC/19")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ sɪᴅʜɪ x ᴍᴜsɪᴄ sɪᴅʜɪ-ꜱᴘᴀᴍʙᴏᴛ!**") 
