#!/usr/bin/env python

# WS server example

import asyncio
import websockets


async def process(websocket, path):
    value = await websocket.recv()
    print(f"< {value}")
    print(f"Client: {websocket.remote_address} ")
    print(f"Server: {websocket.local_address}")
    print(f"{websocket.open}")
    output = f"client: {value}"

    await websocket.send(output)
    print(f"> {output}")


start_server = websockets.serve(process, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
