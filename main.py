import os

from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi_restful.tasks import repeat_every
from fastapi.staticfiles import StaticFiles
from odmantic import AIOEngine
import random
import nltk

from nltk.corpus import words
from api import login
from check_updates import check_updates
from schemas import User, UserPatchSchema

nltk.download('words')
word_bank = [word.lower() for word in words.words() if len(word) <= 6]

app = FastAPI()

client = AsyncIOMotorClient(os.environ["DATABASE_URL"])
engine = AIOEngine(client=client, database="tsims-notify")


@app.post("/submit", response_model=User)
async def submit(username: str, password: str) -> User:
    await engine.configure_database([User])
    await login(username, password)

    # Generate ntfy channel name
    selected_words = random.sample(word_bank, k=3)
    ntfy_channel = '-'.join(selected_words)

    user = User(username=username, password=password, ntfy_channel=ntfy_channel)

    # Check if user with same username exists
    existing_user = await engine.find_one(User, User.username == username)
    if existing_user is None:
        await engine.save(user)
        return user
    else:
        existing_user.model_update(UserPatchSchema(password=password, ntfy_channel=ntfy_channel))
        await engine.save(existing_user)
        return existing_user


@app.delete("/submit", response_model=User)
async def delete(username: str, password: str) -> User:
    await engine.configure_database([User])
    await login(username, password)

    # Check if user with same username exists
    existing_user = await engine.find_one(User, User.username == username)
    if existing_user is None:
        raise HTTPException(404)
    await engine.delete(existing_user)
    return existing_user


app.mount("/", StaticFiles(directory="frontend/.output/public", html=True), name="static")


@app.on_event("startup")
@repeat_every(seconds=60 * 5)  # 5mins
async def cron_job():
    users = await engine.find(User)
    for i in users:
        _data = await check_updates(i)
        # Save patch to database
        i.model_update(UserPatchSchema(data=_data))
        await engine.save(i)
