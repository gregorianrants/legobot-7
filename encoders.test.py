from robot import Robot
import time
import numpy as np
from Encoder import EncoderCounter

bot = Robot()

right_encoder = EncoderCounter(16,'right')
right_encoder.set_mode('test')
left_encoder = EncoderCounter(17,'left')
left_encoder.set_mode('test')


try: 
  bot.set_right(40)


  stop_at_time = time.time() + 10
  while time.time() < stop_at_time:
    time.sleep(0.5)
  bot.stop()

  right_encoder.report_test(np)


  bot.set_left(40)


  stop_at_time = time.time() + 10
  while time.time() < stop_at_time:
    time.sleep(0.5)
  bot.stop()

  left_encoder.report_test(np)
except KeyboardInterrupt:
  bot.stop()
finally:
  bot.stop()






