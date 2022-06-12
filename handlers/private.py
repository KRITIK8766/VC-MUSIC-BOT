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
                            text="❰❰ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❱❱",
                            url=f"https://t.me/Broken_Heart_72"),
                            
                    InlineKeyboardButton(
                            text="❰❰ 𝗚𝗥𝗢𝗨𝗣 ❱❱",
                            url=f"https://t.me/HEPPYLIFI")
                 ],
                  [
                    InlineKeyboardButton(
                        "❰❰ ❰❰ 𝗢𝗪𝗡𝗘𝗥 ❱❱ ❱❱", url=f"https://t.me/{master_user}")
                ],
                 [
                    InlineKeyboardButton(
                        "❰❰ 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 ❱❱", url=f"t.me/HKRMUSICBOT?startgroup=new")
                ]
                            
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3bbbd1b63621c01731ed3.jpg",
        caption=f"""**HA TU BHI AAJA BOSRI KE LUND LE LE MERA**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰❰ ❰❰ 𝗢𝗪𝗡𝗘𝗥 ❱❱ ❱❱", url=f"https://t.me/OFFICIALHACKERERA")
                ]
            ]
        ),
    )



