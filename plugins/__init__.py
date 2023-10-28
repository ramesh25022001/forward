from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS, bot
from config import Config
import os
import sys


@bot.on_message(filters.me & filters.command("start", prefixes=prefixes))
async def Start_msg(bot: Client , m: Message):
    await m.reply_text(
    caption = f"Hello [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n" +
    f"\nI am Auto Forwarder bot." +
    f"\nPress /help for More Info.",
    )

@bot.on_message(filters.me & filters.command("restart", prefixes=prefixes))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
