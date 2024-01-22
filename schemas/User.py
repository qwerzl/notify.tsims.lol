from typing import Optional

from odmantic import Model, Field
from pydantic import BaseModel


class User(Model):
    username: str = Field(unique=True)
    password: str
    ntfy_channel: str = Field(unique=True)
    data: Optional[dict] = None  # EmbeddedModel for odmantic doesn't allow optional types. See odmantic pull#344


class UserPatchSchema(BaseModel):
    password: str = None
    ntfy_channel: str = None
    data: dict = None
