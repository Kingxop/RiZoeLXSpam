from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC or "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  


rizoel = "✧ 𝑅𝐼𝑍𝑂𝐸𝐿 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n" + '┏━━━━━━━━━━━━━━━━━━━\n'            

rizoel += '┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n'

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"

rizoel += '┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/DNHxHELL)\n'

rizoel += '┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/RiZoeLX)\n'

rizoel += '┗━━━━━━━━━━━━━━━━━━━\n\n'

rizoel += '🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLXSpam) 🖤'            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
