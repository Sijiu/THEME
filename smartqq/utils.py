# -*- coding: utf-8 -*-
__author__ = 'wxy'

class ListProcess(object):
    def __init__(self, rsp, nickname):
        self.rsp = rsp
        self.nickname = nickname

    def get_friend_uin(self):
        try:
            for list in self.rsp['result']['info']:
                if list['nick'] == self.nickname:
                    tar_uin = list['uin']
                    return tar_uin
        except:
            return False

    def get_group_uin(self):
        try:
            for list in self.rsp['result']['gnamelist']:
                if list['name'] == self.nickname:
                    print '++++++++++++++++++++++++++++++++++'
                    print list
                    tar_uin = list['gid']
                    return tar_uin
        except:
            return False
