# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

bot = db_x["BOT_USERS"]


async def add_user(user_id):
    await bot.insert_one({"user_id": user_id})


async def check_user(user_id):
    Lol = await bot.find_one({"user_id": user_id})
    if Lol:
        return True
    else:
        return False


async def get_all_users():
    Lol = [s async for s in bot.find()]
    return Lol
