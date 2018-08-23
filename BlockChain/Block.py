import hashlib
# 定义区块结构
class Block:
    def __init__(self,data,prev_hash):
        self.previous_hash=prev_hash
        self.data=data
    #用了类属性@property装饰器来除了hash的值，即当我用block.hash=xxx的时候，会系统自动调用这个hash函数。
    #计算区块的哈希值
    @property
    def hash(self):
        message=hashlib.sha256()
        message.update(str(self.data).encode('utf-8'))
        return message.hexdigest()

#父区块
def create_genesis_block():
    return Block(data="Genesis Block",prev_hash="")