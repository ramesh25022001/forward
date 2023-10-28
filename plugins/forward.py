from pyrogram import filters
from pyrogram import Client as bot
from pyrogram.types import Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import time
import os
import sys

@bot.on_message(filters.command("forward", prefixes=prefixes) & filters.me)
async def forward(bot: bot, m: Message):
    find = m.command
    if find and len(find) >= 4:
        t_chat = int(find[1])
        i_chat = int(find[2])
        s_msg = int(find[3])
        f_msg = int(find[4])
        f_msg += 1

        await m.reply_text('**Forwarding Started**\n\nPress /restart to Stop')
        try:
            for i in range(s_msg, f_msg):
                try:
                    await bot.copy_message(
                        chat_id= t_chat,
                        from_chat_id= i_chat,
                        message_id= i
                    )
                    time.sleep(1.5)
                except Exception:
                    continue
        except Exception as e:
            await m.reply_text(str(e))
        await m.reply_text("Done Forwarding")

    else:
        await m.reply_text("Invalid command. Usage: /forward <targetchannel> <source_channel> <start message id> <end message id>")


@bot.on_message(filters.command("stop") & filters.me)
async def me(client, message):
    await message.reply_text("Stopped", quote=True)
    sys.exit()
