# -*- coding: utf-8 -*-
__author__ = 'wxy'

import os
import time
import logging
from utils import ListProcess
from flask import Flask, request, Response
from QQLogin import QQ
bot = QQ()
bot.login()

import socket
ISOTIMEFORMAT='%Y-%m-%d %X'
app = Flask(__name__)


@app.route('/friends', methods=['POST'])
def friends():
    try:
        start = time.clock()
        #new_msg = bot.check_msg()
        end = time.clock()
        print "read: %f s" % (end - start)

        nickname = request.form['nickname']
        friendlist = bot.get_user_friends2()
        lp = ListProcess(rsp=friendlist,nickname=nickname)
        print friendlist
        tar_uin = lp.get_friend_uin()

        timeis = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        buddy_msg = bot.send_buddy_msg(tar_uin,request.form['content'] + timeis,1)
        return str(buddy_msg)

    except socket.timeout, e:
        logging.warning("RUNTIMELOG check msg timeout, retrying...")

@app.route('/group', methods=['POST'])
def group():
    try:
        start = time.clock()
        #new_msg = bot.check_msg()
        end = time.clock()
        print "read: %f s" % (end - start)

        nickname = request.form['nickname']
        grouplist = bot.get_group_name_list_mask2()
        lp = ListProcess(rsp=grouplist, nickname=nickname)
        tar_uin = lp.get_group_uin()
        print tar_uin

        timeis = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        groupp_msg = bot.send_qun_msg(tar_uin,request.form['content'] + timeis,1)
        return str(groupp_msg)

    except socket.timeout, e:
        logging.warning("RUNTIMELOG check msg timeout, retrying...")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)