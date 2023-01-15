from sshkeyboard import listen_keyboard_manual
from SelfCorrectingRobot import SelfCorrectingRobot
import asyncio

bot = SelfCorrectingRobot()

async def start_listening():
    #do i need to put a sleep in here, how often does it poll input may use up resources?
    await listen_keyboard_manual(
        on_press=press,
    )

async def main():
  listen = asyncio.create_task(start_listening())
  runRobot = asyncio.create_task(bot.start())
  
  await listen



async def press(key):
    print(f"'{key}' pressed")
    if(key=='up'):
        bot.forward(50)
    elif(key=='down'):
        bot.backward()
    elif(key=='left'):
        bot.pivot_left(60)
    elif(key=='right'):
        bot.pivot_right(60)
    elif(key=='space'):
        bot.stop()


def release(key):
    print(f"'{key}' released")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    bot.stop
finally:
    bot.stop