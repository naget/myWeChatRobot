from wxpy import *


if __name__ == '__main__':
        bot = Bot()
        group_receiver = ensure_one(bot.groups().search('dd'))
        Vegout = ensure_one(bot.mps().search('Vegout'))

        @bot.register(Vegout, [TEXT, SHARING])
        def print_others(msg):
                msg.forward(group_receiver)
        embed()