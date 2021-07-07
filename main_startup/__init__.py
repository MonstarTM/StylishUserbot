# Copyright (C) 2020-2021 by MohsinHsn@Github, < https://github.com/MohsinHsn >.
#
# This file is part of < https://github.com/MohsinHsn/StylishUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MohsinHsn/blob/master/LICENSE >
#
# All rights reserved.

import logging
import os
import time

import motor.motor_asyncio
from pyrogram import Client

from .config_var import Config

# Note StartUp Time - To Capture Uptime.
start_time = time.time()
friday_version = "V9.0"

# Enable Logging For Pyrogram
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [FridayUB] - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)


mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_DB)

CMD_LIST = {}
XTRA_CMD_LIST = {}
sudo_id = Config.AFS

if not Config.STRINGSESSION:
    logging.error("No String Session Found! Stylish is Exiting!")
    quit(1)

if not Config.API_ID:
    logging.error("No Api-ID Found! Stylish is Exiting!")
    quit(1)

if not Config.API_HASH:
    logging.error("No Api-Hash Found! Stylish is Exiting!")
    quit(1)

if not Config.LOG_GRP:
    logging.error("No Log Group ID Found! Stylish is Exiting!")
    quit(1)


# Clients - Upto 4 Clients is Supported!
if Config.STRINGSESSION:
    Stylish = Client(
        Config.STRINGSESSION,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
if Config.STRINGSESSION_2:
    Stylish2 = Client(
        Config.STRINGSESSION_2,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Stylish2 = None
if Config.STRINGSESSION_3:
    Stylish3 = Client(
        Config.STRINGSESSION_3,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Stylish3 = None
if Config.STRINGSESSION_4:
    Stylish4 = Client(
        Config.STRINGSESSION_4,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Stylish4 = None

if Config.BOT_TOKEN:
    bot = Client(
        "MyAssistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        sleep_threshold=180,
    )
else:
    bot = None
