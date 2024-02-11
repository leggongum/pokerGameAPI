from pydantic import BaseModel, Field



class password(BaseModel):
    password: str | None = Field(max_length=64, min_length=3, default=None)

class LobbyBase(BaseModel):
    title: str = Field(max_length=64)
    users: list | None = Field(default=None)


class LobbyCreate(LobbyBase):
    password: str | None = Field(max_length=64, min_length=3, default=None)


class LobbyUpdate(BaseModel):
    password: str | None = Field(max_length=64, min_length=3, default=None)






