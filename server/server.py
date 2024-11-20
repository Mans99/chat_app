import asyncio
import websockets

connect_clients = set()

async def handle_client(websocket, path):
    connect_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connect_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        connect_clients.remove(websocket)
        

start_server = websockets.serve(handle_client, "0.0.0.0", 4000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()