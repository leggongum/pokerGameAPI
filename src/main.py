from fastapi import FastAPI, Request
from urllib.parse import urlencode

from lobby.router import router as lobby_router
from game.router import router as game_router
from fake_db import db
from utils import generate_name


app = FastAPI(title='pokerGameAPI')

app.include_router(lobby_router)
app.include_router(game_router)


@app.middleware("http")
async def add_user(request: Request, call_next):
    user_id = request.query_params.get('user') if request.query_params.get('user') else request.client.host
    if user_id not in db['users']:
        db['users'][user_id] = generate_name()
    q_params = dict(request.query_params)
    q_params['user'] = user_id
    request.scope['query_string'] = urlencode(q_params).encode('utf-8')
    return await call_next(request)

