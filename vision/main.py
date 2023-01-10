
from camera import getFrame
import numpy as np

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://192.168.178.52:3000")
time.sleep(1)

for frame in getFrame():
    socket.send_pyobj({'original': frame })