import os

from aiohttp import ClientSession
from . import tTypes


async def get_timetable(session: tTypes.tSession, year: int):
    url = f'{os.environ["TSIMS_URL"]}/php/school_student_timetable.php'
    data = {
        'timetableType': 'teachertb',
        'yearID': year  # Replace with the actual value
    }

    async with ClientSession(cookie_jar=session.cookies) as _session:
        async with _session.post(url, data=data) as response:
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            # Parse the JSON response
            data = await response.text()
            return data
