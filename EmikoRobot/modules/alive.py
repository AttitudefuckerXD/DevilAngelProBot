import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/a01ef91bd802109bbcbc1.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ๐ณแดแด ษชสโ๐ฐษณษ ษฦ.** \n\n"
  TEXT += "โช **I'm Working Properly** \n\n"
  TEXT += f"โช **My Master : [ ออออโณโฅ๐ฆ๐๐๐๐๐๐๐ ๐ฐ๐๐๐เฟ](https://t.me/Attitude_king_vj)** \n\n"
  TEXT += f"โช **Library Version :** `{telever}` \n\n"
  TEXT += f"โช **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"โช **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here โค๏ธ**"
  BUTTON = [[Button.url("Help", "https://t.me/DevilxAngeLBot?start=help"), Button.url("Support", "https://t.me/PyTgMusicSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
