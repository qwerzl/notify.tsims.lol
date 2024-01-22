import os

from aiohttp import ClientSession, FormData, CookieJar
from fastapi import HTTPException

from . import tTypes


async def login(username: str, password: str) -> tTypes.tSession:
    url = f'{os.environ["TSIMS_URL"]}/php/login.php'
    _cookies = CookieJar(unsafe=True)  # `Unsafe=True` is for IP addresses.
    data = FormData()
    data.add_field('username', username)
    data.add_field('password', password)
    async with ClientSession(cookie_jar=_cookies) as session:
        # Send the POST request
        async with session.post(url, data=data) as response:
            response.raise_for_status()  # Raise for non-2xx errors.
            if (await response.json(content_type='text/html'))['status'] != "ok":
                raise HTTPException(status_code=403, detail="Username/Password Incorrect")
            return tTypes.tSession(cookies=_cookies)
