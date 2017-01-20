import telepot
import time


def start(token, msg_handle=None):
    bot = telepot.Bot(token)
    if not msg_handle:
        from .msg_handle import default_msg_handle
        msg_handle = default_msg_handle
    bot.message_loop(msg_handle)
    print("Bot started!")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Bot stopped!")


