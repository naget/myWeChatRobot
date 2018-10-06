# 功能：自动同意好友请求
# 问题：对与验证信息的正则匹配不知道怎么加入
from wxpy import *
import re

add_friends_compile = re.compile(r'Java|python|技术交流|java')
bot = Bot()


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    if add_friends_compile.search(msg.text) is not None:
        new_friend = bot.accept_friend(msg.card)
        new_friend.send("我是个半智障小机器人，欢迎调戏o，但我还小，是不会理你的")


embed()


