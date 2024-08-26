#ANKITA DAS HITWICKET
import asyncio
import websockets

#this is the initial state of the game
game_state = {
    "A": ["P1", "P2", "H1", "P3", "P4"],
    "B": ["P1", "P2", "H1", "P3", "P4"],
    "turn": "A",  # It's Player A's turn
    "board": [["A-P1", "A-P2", "A-H1", "A-P3", "A-P4"],#these are the initial player positions
              ["", "", "", "", ""],
              ["", "", "", "", ""],
              ["", "", "", "", ""],
              ["B-P1", "B-P2", "B-H1", "B-P3", "B-P4"]]
}

#websocket
async def game_handler(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            player, move = message.split(':')
            print(f"Received move: {move} from Player: {player}")

            if player == game_state["turn"]:
                # Process move (simplified for this example)
                if move == "end":
                    await websocket.send("Game Over")
                    print("Game Over")
                    return

                
                game_state["turn"] = "B" if game_state["turn"] == "A" else "A"
                await websocket.send(f"Move received: {move}. It's now {game_state['turn']}'s turn.")
            else:
                await websocket.send("Not your turn!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Client disconnected")

# Starting the server now
async def start_server():
    async with websockets.serve(game_handler, "localhost", 6789):
        print("Server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(start_server())
