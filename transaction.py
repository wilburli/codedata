#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-01 16:23
# @Author  : windblue
# @contact: q418584383@gmail.com
# @File    : Transaction.py
import datetime


class Transaction: #交易类
    def __init__(self,payer,recer,money): # 付款方 收款方  钱
        self.payer=payer
        self.recer=recer
        self.money=money
        self.timestamp=datetime.datetime.now()

    def __repr__(self):
        return str(self.payer)+" pay "+str(self.recer)+":"+str(self.money)+" time:"+str(self.timestamp)
if __name__=="__main__":
    try:
        t1=Transaction("yichen","wilbur",10000) #交易类
        t2 = Transaction("yichen", "wilbur2", 20000)
        t3 = Transaction("yichen", "wilbur3", 30000)
        t4 = Transaction("yichen", "wilbur4", 13200)
        print(t1)
    except Exception as e:
        print(e)