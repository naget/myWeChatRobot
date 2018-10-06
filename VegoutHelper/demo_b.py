# 功能：自动同意一定范围的的好友请求
import itchat
import re
from itchat.content import *

add_friends_compile = re.compile(r'Java|python|技术交流|java')


@itchat.msg_register(FRIENDS)
def add_friends(msg):
    if add_friends_compile.search(msg['Content']) is not None:
        itchat.add_friend(**msg['Text'])
        # python小知识：**表示参数成为一个字典，并且我们在字典中取出键Text对应的值
        # itchat文档：从Text对应的值就是add_friend需要的属性
        itchat.send_msg('我是半智障小机器人，欢迎调戏哦！当然了，现在我还小，是不会理你的', msg['RecommendInfo']['UserName'])


if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()