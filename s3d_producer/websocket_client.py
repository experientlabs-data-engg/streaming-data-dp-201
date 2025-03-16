import asyncio
import websockets
import threading


async def on_message(ws):
    async for message in ws:
        print(f"Received message: {message}")


async def client():
    uri = "ws://0.0.0.0:8765"
    async with websockets.connect(uri) as websocket:
        await on_message(websocket)


def start_websocket_client():
    asyncio.run(client())


if __name__ == "__main__":
    start_websocket_client()