# -*- coding: utf-8 -*-
__author__ = 'wxy'
import requests


if __name__ == "__main__":
    data = {'nickname': 'Peter Bishop', 'content': 'this is a test'}

    rp = requests.post("http://127.0.0.1:5000/friends", data=data)
    data = {'nickname': '某宝信誉交流群', 'content': 'this is a test'}
    group = requests.post("http://127.0.0.1:5000/group", data=data)
