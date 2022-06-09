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
        photo=f"https://telegra.ph/file/72158285463afef8d1044.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞  𝐕𝐩𝐬  𝐒𝐞𝐫𝐯𝐞𝐫  𝐅𝐞𝐞𝐥 ️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜  𝐈𝐧 𝐕𝐜**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Owner ", url=f"https://t.me/{master_user}")
               ],
                [
                    InlineKeyboardButton(
                        " ✚ Add me to your Group ✚", url=f"t.me/HKRMUSICBOT?startgroup=new")
               ], 
                [
                    InlineKeyboardButton(
                        " ", url=f"https://t.me/LegendBot_AI")
               ],
                [
                    InlineKeyboardButton(
                        " ", url=f"https://t.me/LegendBot_OP")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/72158285463afef8d1044.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Repo ", url=f"https://github.com/LEGENDARY-OS/MUSIC-BOT")
                ]
            ]
        ),
    )
