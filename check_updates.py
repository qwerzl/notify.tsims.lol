import api
import hashlib
import ntfy
from schemas import User, UserPatchSchema

async def check_updates(user: User):
    _session = await api.login(user.username, user.password)
    _year_id = await api.get_current_year(_session)
    _patch = dict()
    _patch['timetable'] = hashlib.sha256(
                            (await api.get_timetable(_session, _year_id)).encode()
                        ).hexdigest()
    _patch['score'] = hashlib.sha256(
                            (await api.get_score(_session, _year_id)).encode()
                        ).hexdigest()
    _patch['report'] = hashlib.sha256(
                            (await api.get_report(_session, _year_id)).encode()
                        ).hexdigest()

    if user.data is not None:
        for i in ['timetable', 'report', 'score']:
            if user.data[i] is not None:
                if user.data[i] != _patch[i]:
                    await ntfy.send_notification(user.ntfy_channel, f"{i} has changed.")
    else:
        await ntfy.send_notification(user.ntfy_channel, "Your account is configured!")

    return _patch
