import asyncio
import os

import aiohttp


async def send_notification(channel: str, data: str):
    # Your target URL
    url = f"https://ntfy.tsims.lol/{channel}"
    # The data to send
    data = data
    # Headers with additional information
    headers = {
        "Title": "Changes on TSIMS detected!",
        "Tags": "loudspeaker",
        "Authorization": f"Basic {os.environ['NTFY_SECRET']}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            response.raise_for_status()
