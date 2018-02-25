#!/usr/bin/env python

import asyncio
import websockets


def attend_request(websocket, message):
    return websocket.send("adios %s" % message)


async def consumer_handler(websocket, path):
    async for message in websocket:
        await attend_request(websocket, message)

start_server = websockets.serve(consumer_handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
