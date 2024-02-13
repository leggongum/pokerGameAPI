from fastapi import APIRouter, HTTPException, WebSocket, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect

import json

from fake_db import db
from game.connect_manager import get_manager



router = APIRouter(
    prefix="/ws",
    tags=["Game"],
)



@router.websocket("/{lobby_title}")
async def connect_to_lobby(websocket: WebSocket, 
                           lobby_title: str, 
                           user: str | None = None,
                           manager=Depends(get_manager)):
    if user not in db['lobbies'][lobby_title].users or user in {player.id for player in manager.players}:
        return 


    await manager.connect(websocket, user, db['users'][user])
    try:
        while True:
            try:
                data = await websocket.receive_json()
            except json.decoder.JSONDecodeError as ex:
                print(ex)
            else:
                print(data)
                action = data['action']
                if action == 'message':
                    await manager.send_update_in_lobby({'type': 'message', 'content': data['content'], 'from': db['users'][user]})
                elif user == manager.turn.id:
                    manager.action = data
                    manager.event.set()
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"{user} left the chat")

        