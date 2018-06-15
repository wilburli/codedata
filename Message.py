import datetime
import hashlib  # 信息加密包
from transaction import Transaction # transaction指文件名 Transaction指类
class WilburMessage:  # 交易记录类
    def __init__(self,data):
        self.hash=None # 自身hash
        self.prev_hash=None  # 上一个信息记录的hash
        self.timestamp=datetime.datetime.now() #交易时间
        self.data=data
        self.payload_hash=self._hash_payload() #交易后的哈希
    def _hash_payload(self): #对于交易时间和数据进行哈希512加密
        return hashlib.sha256((str(self.timestamp)+str(self.data)).encode('utf-8')).hexdigest()


    def __hash__message(self): #对交易进行锁定
        return hashlib.sha256((str(self.prev_hash) + str(self.data)).encode('utf-8')).hexdigest()

    def seal(self): #密封
        self.hash=self.__hash__message() #对应数据锁定，对交易前的链进行锁定

    def validate(self):
        if self.payload_hash != self._hash_payload(): #判断是否有人修改
            raise InvalidMessage("无效的交易数据与时间被修改"+str(self))
        if self.hash!=self.__hash__message(): #判断消息链
            raise InvalidMessage("交易的哈希链被修改"+str(self))
        return "数据正常"+str(self)

    def __repr__(self): #返回对象的基本信息
        mystr="hash:{},prev_hash:{},data:{}".format(self.hash,self.prev_hash,self.data)
        return mystr

    def link(self,Message): #链接起来
        self.prev_hash=Message.hash


class InvalidMessage(Exception): #异常类
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


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

        m1.seal()
        m2.link(m1)
        m2.seal()
        m3.link(m2)
        m3.seal() #密封
        m4.link(m3)
        m4.seal() #密封
        #修改数据
        m2.data="修改交易数据"
        m2.prev_hash="测试数据"

        print(m1)
        print(m2)
        print(m3)
        print(m4)
        m1.validate()
        m2.validate()
        m3.validate()
        m4.validate()
    except InvalidMessage as e:
        print("erro:",e)