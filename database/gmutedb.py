# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

gmuteh = db_x["GMUTE"]


async def is_gmuted(sender_id):
    kk = await gmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


async def gmute(sender_id, reason="#GMuted"):
    await gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


async def ungmute(sender_id):
    await gmuteh.delete_one({"sender_id": sender_id})
