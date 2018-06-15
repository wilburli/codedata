#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-01 15:29
# @Author  : windblue
# @contact: q418584383@gmail.com
# @File    : Block_wilbur.py
import datetime
import hashlib
from  Message import WilburMessage
from transaction import Transaction
from Message import InvalidMessage
class Block:
    def __init__(self,*args):
        self.messageList=[] #存储多个交易记录
        self.timestamp=None
        self.hash=None #当前hash散列
        self.prev_hash=None #上一块的hash散列
        if args:
            for arg in args:
                self.add_message(arg)

    def add_message(self,message): #增加交易信息
        if len(self.messageList)>0:
            message.link(self.messageList[-1]) # 取最后一个进行连接
        message.seal()
        message.validate()
        self.messageList.append(message)
    def link(self,block):
        self.prev_hash=block.hash

    def seal(self): # 密封
        self.timestamp = datetime.datetime.now()
        self.hash = self._hash_block()

    def _hash_block(self): # 密封上一块hash 时间线 交易记录的最后一个
        return hashlib.sha256( (str(self.prev_hash)+str(self.timestamp)+str(self.messageList[-1].hash)).encode("utf-8") ).hexdigest()


    def validate(self): # 验证
        for i,message in enumerate(self.messageList): # enumerate 枚举  对于一个可迭代的对象，enumerate将其组成一个索引序列，利用它可以同时获取索引和值
            message.validate() # 每一条验证一下
            if i>0 and message.prev_hash != self.messageList[i-1].hash: # raise "无效block，交易记录被修改为在第{}条记录".format(i) # raise引发一个异常和throw类似
                raise InvalidBlock("无效block，交易记录被修改为在第{}条记录".format(i)+str(self)) # raise引发一个异常和throw类似
                return str(self)+"数据No"
        return str(self)+"数据ok"
    def __repr__(self): # 格式化
        return "money block = hash:{},prehash:{},len:{},time:{}".format(self.hash,self.prev_hash,len(self.messageList),self.timestamp)

class InvalidBlock(Exception):
    def __init__(self,*arg,**kargs):
        Exception.__init__(self,*arg,**kargs)



if __name__=="__main__": #单独模块测试
    try:
        t1 = Transaction("yichen", "wilbur", 10000)  # 交易类
        t2 = Transaction("yichen", "wilbur2", 20000)
        t3 = Transaction("yichen", "wilbur3", 30000)
        t4 = Transaction("yichen", "wilbur4", 13200)

        m1=WilburMessage(t1)
        m2=WilburMessage(t2)
        m3=WilburMessage(t3)
        m4=WilburMessage(t4)

        yin = Block(m1,m2,m3) # 加入4条数据
        yin.seal()
        # m2.hash="test"
        # yin.messageList[2]=m1
        print(yin.validate())
        print(yin)
    except InvalidMessage as e:  # 消息被修改
        print(e)
    except InvalidBlock as e: # 区块被修改
        print(e)