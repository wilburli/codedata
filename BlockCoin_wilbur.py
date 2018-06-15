#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-01 15:30
# @Author  : windblue
# @contact: q418584383@gmail.com
# @File    : BlockCoin_wilbur.py

from Block_wilbur import Block
from Block_wilbur import InvalidBlock
from  Message import WilburMessage
from transaction import Transaction
from Message import InvalidMessage
class Wilbur_BlockCoin: # 区块链
    def __init__(self):
        self.blocklist=[] #装载所有区块

    def add_block(self,block): # 增加区块
        if len(self.blocklist) >0:
            block.prev_hash=self.blocklist[-1].hash #  区块链的hash
        block.seal()
        block.validate()
        self.blocklist.append(block) #增加区块

    def validate(self):
        for i,block in enumerate(self.blocklist):
            try:
                block.validate()
            except InvalidBlock as e:
                raise InvalidBlockCoin("区块校验错误，区块索引{}".format(i))


    def __repr__(self):
        return "blockCoin_wilbur:{}".format(len(self.blocklist))

class InvalidBlockCoin(Exception):
    def __init__(self,*arg,**kargs):
        Exception.__init__(self,*arg,**kargs)


if __name__=="__main__":
    # try:
        t1 = Transaction("yichen", "wilbur", 10000)  # 交易类
        t2 = Transaction("yichen", "wilbur2", 20000)
        t3 = Transaction("yichen", "wilbur3", 30000)
        t4 = Transaction("yichen", "wilbur4", 13200)
        t5 = Transaction("yichen", "wilbur5", 30000)
        t6 = Transaction("yichen", "wilbur6", 13200)
        m1 = WilburMessage(t1)
        m2 = WilburMessage(t2)
        m3 = WilburMessage(t3)
        m4 = WilburMessage(t4)
        m5 = WilburMessage(t5)
        m6 = WilburMessage(t6)
        wilbur1 = Block(m1,m2)
        wilbur1.seal()
        # wilbur1.link()
        # wilbur1.validate()
        wilbur2 = Block(m3,m4)
        wilbur2.seal()
        wilbur3 = Block(m5,m6)
        wilbur3.seal()

        # wilbur3.messageList.append(m1)  # 验证区块

        myWilbur = Wilbur_BlockCoin()
        myWilbur.add_block(wilbur1)
        myWilbur.add_block(wilbur2)
        myWilbur.add_block(wilbur3)
        myWilbur.validate()
        print(myWilbur)
    # except Exception as e:
    #     print(e)