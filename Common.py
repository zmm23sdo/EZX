from TestInterface import Interface

import pytest
import json
import time
import random
import hmac, base64, struct, hashlib, time
import random
import datetime
import oss2
import os


inter = Interface()

#生成随机手机号
def SetPhone():
    random_phone = '' .join(random.sample('0123456789',10))
    print(random_phone)
    return random_phone
#随机单个汉字
def Unicode():#第一种方法:Unicode码
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def GBK2312():#第二种方法:GBK2312
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)   # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


def TimeNow():
    time_now = int(time.time())    
    Random = str(time_now)
    return Random
def Today():
    # 获取当前时间
    now = datetime.datetime.now()
    # 获取今天零点
    zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)
    # 获取23:59:59
    lastToday = zeroToday + datetime.timedelta(hours=23, minutes=59, seconds=59)
    # 获取前一天的当前时间
    yesterdayNow = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    # 获取明天的当前时间
    tomorrowNow = now + datetime.timedelta(hours=23, minutes=59, seconds=59)
    
    print('时间差',datetime.timedelta(hours=23, minutes=59, seconds=59))
    print('当前时间',now)
    print('今天零点',zeroToday)
    print('获取23:59:59',lastToday)
    print('昨天当前时间',yesterdayNow)
    print('明天当前时间',tomorrowNow)
    return zeroToday,lastToday
def Now():
    now = datetime.datetime.now().isoformat() + "Z"
    print(now)
    return now

def NowDate():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    now_time = str(now_time)
    print(now_time)
    return now_time

def loginOne():
    login = inter.verify(
        username = "zhangmingwei", 
        password = "qwer1234", 
        platform = "admin"
    )
    # print(login.json())
    expiry = str(login.json()['expiry'])
    token = str(login.json()['token'])
    # print("expiry",expiry)
    # print("token",token)
    return token

def loginTwo():
    login2 = inter.session(
        token = loginOne(), 
        company = 1
    )
    # print(login2.json())
    access = str(login2.json()['access'])
    create = str(login2.json()['create'])
    expiry = str(login2.json()['expiry'])
    refresh = str(login2.json()['refresh'])
    # print("access",access)
    # print("create",create)
    # print("expiry",expiry)
    print("refresh",refresh)
    return refresh
