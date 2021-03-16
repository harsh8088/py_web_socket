import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: websockets.WebSocketServerProtocol) -> None:
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connected.")

    async def unregister(self, ws: websockets.WebSocketServerProtocol) -> None:
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnected.")

    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def ws_handler(self, ws: websockets.WebSocketServerProtocol) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: websockets.WebSocketServerProtocol) -> None:
        async for message in ws:
            await self.send_to_clients(message)


if __name__ == '__main__':
    server = Server()
    start_server = websockets.serve(server.ws_handler, "localhost", 4000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()

# async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
#     async for message in websocket:
#         log_message(message)
#
#
# def log_message(message: str) -> None:
#     logging.info(f"Message:{message}")
#
#
# async def consume(hostname: str, port: int) -> None:
#     websocket_resource_url = f"ws://{hostname}:{port}"
#     async with websockets.connect(websocket_resource_url) as websocket:
#         await consumer_handler(websocket)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(consume(hostname="localhost", port=4000))
#     loop.run_forever()
