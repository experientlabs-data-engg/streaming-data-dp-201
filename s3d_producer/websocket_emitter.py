import csv
import json
import asyncio
import websockets
from deh.poisson import PoissonTriggerGenerator
from deh.events import RandomEventGenerator
import random
import numpy as np

RATE = 20

random.seed(24)
np.random.seed(24)

with open("deh/country_codes.csv", "r") as file:
    country_codes = list(csv.reader(file))[1:]

with open("deh/tracking_ids.json", "r") as file:
    tracking_ids = json.load(file)


async def serve(websocket):  # Removed the _ argument
    event_generator = RandomEventGenerator(
        country_codes=country_codes, tracking_ids=tracking_ids
    )
    p = PoissonTriggerGenerator(event_generator.get_event, RATE)

    await p.start()  # Start the Poisson generator

    try:
        async for event in p.get():
            try:
                await websocket.send(json.dumps(event, default=str))
            except websockets.exceptions.ConnectionClosedError:
                print("Client disconnected.")
                break
    except Exception as e:
        print(f"Error in serve function: {e}")
    finally:
        await p.stop()
        print("Connection closed.")


async def main():
    async with websockets.serve(serve, "0.0.0.0", 8765):
        print("WebSocket server started.")
        await asyncio.Future()  # Keep the server running

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")