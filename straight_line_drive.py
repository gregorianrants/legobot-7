from SelfCorrectingRobot import SelfCorrectingRobot

import time


bot = SelfCorrectingRobot()

try: 
 
  stop_at_time = time.time() + 5

  speed = 60

  bot.forward()

  while time.time() < stop_at_time:
    time.sleep(0.01)
    bot.update()
except KeyboardInterrupt:
  bot.stop()
finally: 
  bot.stop()

