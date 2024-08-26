#ANKITA DAS HITWICKET
import asyncio
import websockets

async def send_move():
    try:
        async with websockets.connect("ws://localhost:6789") as websocket:
            while True:
                move = input("Enter your move (e.g., P1:L or 'end' to finish): ")
                await websocket.send(f"A:{move}")
                response = await websocket.recv()
                print(f"Server response: {response}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

async def main():
    await send_move()

if __name__ == "__main__":
    asyncio.run(main())
