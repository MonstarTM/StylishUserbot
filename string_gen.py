import pyrogram
from pyrogram import Client

Stylish_ = """
STYLISH USERBOT
Copyright (C) 2020-2021 by mohsinhsn@Github, < https://github.com/mohsinhsn >.
This file is part of < https://github.com/mohsinhsn/StylishUserBot > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/mohsinhsn/blob/master/LICENSE >
All rights reserved.
"""

print(stylish_)

api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")
bot_token = input("Enter Your BOT TOKEN : \n")


with Client("StylishUB", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b><u>String Session For {first_name}</b></u> \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
