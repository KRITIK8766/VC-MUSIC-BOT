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
        photo=f"https://telegra.ph/file/ac2cbc52c602ed4dbc549.jpg",
        caption=f"""** ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ **""",
    reply_markup=InlineKeyboardMarkup(
            [
                  [
                    InlineKeyboardButton(
                            text="❰❰ OWNER ❱❱",
                            url=f"https://t.me/{master_user}"),
                            
                    InlineKeyboardButton(
                            text="❰❰ GROUP ❱❱",
                            url=f"https://t.me/HEPPYLIFI")
                 ],
                 [
                    InlineKeyboardButton(
                        "❰❰ ADD ME TO YOUR GROUP ❱❱", url=f"t.me/HKRMUSICBOT?startgroup=new")
                ]
                            
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ac2cbc52c602ed4dbc549.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰❰ OWNER ❱❱", url=f"https://t.me/OFFICIALHACKERERA")
                ]
            ]
        ),
    )



