# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

bsdb = db_x["bot_sdb"]

default_text = """<b>Hello, {user_firstname}!
This is A UserBot Of {boss_firstname}.</b>
<i>My Boss is Busy As For Now, You Can Wait For Sometime
If S/he Needs To Talk To You, S/he Will Approve You!</i>

<b><u>You Have {warns} Of Warns.</b></u>
"""

default_thumb = "https://telegra.ph/file/5e2c600d79c7f9a005776.jpg"


async def add_pm_text(text=default_text):
    ujwal = await bsdb.find_one({"_id": "PM_START_MSG"})
    if ujwal:
        await bsdb.update_one({"_id": "PM_START_MSG"}, {"$set": {"pm_msg": text}})
    else:
        await bsdb.insert_one({"_id": "PM_START_MSG", "pm_msg": text})


async def add_pm_thumb(thumb=default_thumb):
    ujwal = await bsdb.find_one({"_id": "PM_START_THUMB"})
    if ujwal:
        await bsdb.update_one({"_id": "PM_START_THUMB"}, {"$set": {"pm_img": thumb}})
    else:
        await bsdb.insert_one({"_id": "PM_START_THUMB", "pm_img": thumb})


async def get_thumb():
    ujwal = await bsdb.find_one({"_id": "PM_START_THUMB"})
    if ujwal:
        return ujwal["pm_img"]
    else:
        return None 


async def get_pm_text():
    ujwal = await bsdb.find_one({"_id": "PM_START_MSG"})
    if ujwal:
        return ujwal["pm_msg"]
    else:
        return default_text


async def set_pm_spam_limit(psl=3):
    stark = await bsdb.find_one({"_id": "LIMIT_PM"})
    if stark:
        await bsdb.update_one({"_id": "LIMIT_PM"}, {"$set": {"psl": int(psl)}})
    else:
        await bsdb.insert_one({"_id": "LIMIT_PM", "psl": int(psl)})


async def get_pm_spam_limit():
    meisnub = await bsdb.find_one({"_id": "LIMIT_PM"})
    if meisnub:
        return int(meisnub["psl"])
    else:
        return 3
