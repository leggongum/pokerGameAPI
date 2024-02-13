from fastapi import APIRouter, HTTPException, Request, Response

from fake_db import db
from lobby.schemas import LobbyCreate, LobbyBase, password
from lobby.private_lobby_utils import get_password_hash, verify_password



router = APIRouter(
    prefix="/lobby",
    tags=["Lobbies"],
)


@router.get('/', response_model=list[LobbyBase])
def get_all_lobbies():
    res = []
    for lobby in db['lobbies'].values():
        users = []
        for user in lobby.users:
            users.append(db['users'][user])
        res.append(LobbyBase(title=lobby.title, users=users))

    return res


@router.post('/')
async def create_lobby(lobby: LobbyCreate, response: Response, user: str | None = None):
    if db['lobbies'].get(lobby.title):
        return HTTPException(403, detail='Lobby with this title already exist. You must make another title.')
    lobby.users = [user]
    if lobby.password:
        lobby.password = get_password_hash(lobby.password)
    db['lobbies'][lobby.title] = lobby
    response.status_code = 201
    return lobby.title


@router.patch('/{lobby_title}/add')
async def come_in_lobby(password: password, response: Response, lobby_title: str, user: str | None = None):
    if not db['lobbies'].get(lobby_title):
        return HTTPException(404, detail='Such lobby is not exist.')
    
    if db['lobbies'][lobby_title].password and verify_password(password.password, db['lobbies'][lobby_title].password):
        db['lobbies'][lobby_title].users.append(user)
    else:
        return HTTPException(403, detail='Wrong password.')
    response.status_code = 204
    

@router.patch('/{lobby_title}/del')
async def leave_from_lobby(lobby_title: str, response: Response, user: str | None = None):
    if not db['lobbies'].get(lobby_title):
        return HTTPException(404, detail='Such lobby is not exist.')
    try:
        db['lobbies'][lobby_title].users.remove(user)
    except ValueError:
        return HTTPException(404, detail='Such user is not in lobby.')
    else:
        if not db['lobbies'][lobby_title].users:
            del db['lobbies'][lobby_title]
    response.status_code = 204

    
