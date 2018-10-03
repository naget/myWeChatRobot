#!/usr/bin/env python
# coding:utf8
import itchat
from itchat.content import *


@itchat.msg_register([TEXT, SHARING], isMpChat=True)
def forwardInfo(msg):
    sources = []
    chatroom = itchat.search_chatrooms(name='dd')
    chatrooms = [chatroom]
    source = itchat.search_mps('Vegout')[0]['UserName']
    sources.append(source)
    if sources.__contains__(msg['FromUserName']):
        print(msg['FromUserName'])
        for chatroom in chatrooms:
            if msg['Type'] == SHARING:
                itchat.send('\n%s\n%s' % (msg['FileName'], msg['Url']), toUserName=chatroom[0]['UserName'])
            elif msg['Type'] == TEXT:
                content = msg['Text']
                itchat.send(content, toUserName=chatroom[0]['UserName'])


if __name__ == '__main__':
    itchat.auto_login(True)
    # 开始监测
    itchat.run()
