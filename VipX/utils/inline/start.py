from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" 《ʜᴇʟᴘ》 ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ ꜱᴇᴛᴛɪɴɢꜱ ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" ᴏᴡɴᴇʀ ", url=f"https://t.me/cosmic_god",
            ),
            InlineKeyboardButton(
                text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=" ꜱᴜᴘᴘᴏʀᴛ ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text=" ᴜᴘᴅᴀᴛᴇꜱ ", url=f"https://t.me/thejudicialNetwork",
            )
        ],
        [
            InlineKeyboardButton(
                text=" ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ",
                url=f"https://github.com/Cosmicgodalpha/Alphamusic",
            )
        ],
     ]
    return buttons
