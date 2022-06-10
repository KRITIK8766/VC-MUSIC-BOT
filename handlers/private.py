import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

master_user = os.environ.get("MASTER_USERNAME", None)

if "@" in master_user: 
    master_user.replace("@", "")

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3bbbd1b63621c01731ed3.jpg",
        caption=f"""** ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ 
        
    ØFFɪㄈɪΛŁ нΛㄈҚƐ尺 (https://t.me/OFFICIALHACKERERA) **""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝙊𝙒𝙉𝙀𝙍 ", url=f"https://t.me/{master_user}")
                    
               ],
                [
                    InlineKeyboardButton(
                        " ✚ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ✚ ", url=f"t.me/HKRMUSICBOT?startgroup=new")
               ]
                            
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3bbbd1b63621c01731ed3.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝗢𝘄𝗻𝗲𝗿 ", url=f"https://t.me/OFFICIALHACKERERA")
                ]
            ]
        ),
    )



