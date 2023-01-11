from SelfCorrectingRobot import SelfCorrectingRobot

import time
import asyncio


bot = SelfCorrectingRobot()

async def stopAfter3():
  global bot
  await asyncio.sleep(3)
  bot.stop()

async def main():
  runRobot = asyncio.create_task(bot.start())
  stopRobot = asyncio.create_task(stopAfter3())
  bot.forward(50)
  await runRobot

try:
  asyncio.run(main())
except KeyboardInterrupt:
  bot.robot.stop()
finally:
  bot.robot.stop()


