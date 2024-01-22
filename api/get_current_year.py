import os
from aiohttp import ClientSession, CookieJar

from . import tTypes


async def get_current_year(_session: tTypes.tSession) -> int:
    url = f'{os.environ["TSIMS_URL"]}/php/init_term_dropdown.php'
    _cookies = CookieJar(unsafe=True)  # `Unsafe=True` is for IP addresses.
    async with ClientSession(cookie_jar=_session.cookies) as session:
        # Send the POST request
        async with session.post(url) as response:
            response.raise_for_status()  # Raise for non-2xx errors.
            return (await response.json(content_type='text/html'))[0]["W_YearID"]
