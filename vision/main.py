
from camera import getFrame
import numpy as np

import time
import zmq

context = zmq.Context()
tcp_socket = context.socket(zmq.PUB)
ipc_socket = context.socket(zmq.PUB)
tcp_socket.bind("tcp://192.168.178.52:3000")
ipc_socket.bind("ipc://camera")

time.sleep(1)

for frame in getFrame():
    [originalImage,left_closest,right_closest] = frame
    tcp_socket.send_pyobj({'original': originalImage })
    ipc_socket.send_pyobj({'left': left_closest, 'right': right_closest})