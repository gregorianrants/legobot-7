from sshkeyboard import listen_keyboard
from robot import Robot

bot = Robot()

def press(key):
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
    listen_keyboard(
        on_press=press,
        on_release=release,
    )
except KeyboardInterrupt:
    bot.stop
finally:
    bot.stop