import asyncio
import zmq
import zmq.asyncio

ctx = zmq.asyncio.Context()

async def distance_gen():
    sock = ctx.socket(zmq.SUB)
    sock.connect("ipc://camera")
    sock.setsockopt(zmq.SUBSCRIBE,"".encode('utf-8'))
    while True:
      msg = await sock.recv_pyobj() # waits for msg to be ready
      yield msg
   

