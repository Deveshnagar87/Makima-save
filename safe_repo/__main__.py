#safe_repo

import asyncio
import importlib
import pyrogram.utils
from pyrogram import idle
from safe_repo.modules import ALL_MODULES
from aiojobs import create_scheduler
pyrogram.utils.MIN_CHANNEL_ID = -1002486629939
from safe_repo.core.mongo.plans_db import check_and_remove_expired_users

loop = asyncio.get_event_loop()

async def schedule_expiry_check():
    scheduler = await create_scheduler()
    while True:
        await scheduler.spawn(check_and_remove_expired_users())
        await asyncio.sleep(3600)  # Check every hour

async def safe_repo_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("safe_repo.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")

    # Start the background task for checking expired users
    asyncio.create_task(schedule_expiry_check())

    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop.run_until_complete(safe_repo_boot())
