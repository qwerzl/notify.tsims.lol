import os

from aiohttp import ClientSession
from . import tTypes


async def get_score(session: tTypes.tSession, year: int):
    url = f'{os.environ["TSIMS_URL"]}/php/search_student_score.php'
    data = {
        'yearID': year
    }

    async with ClientSession(cookie_jar=session.cookies) as _session:
        async with _session.post(url, data=data) as response:
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            # Parse the JSON response
            data = await response.text()
            return data
