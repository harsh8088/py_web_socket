import asyncio
import websockets


def produce(message: str, host: str, port: int) -> None:

    websockets.connect(f"ws://{host}:{port}")
        # await ws.send(message)
        # await ws.recv()


if __name__ == '__main__':
    produce(message="hi htishskl", host="localhost", port=4000)
