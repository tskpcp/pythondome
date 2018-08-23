import Block as b
class BlockChain:
    def __init__(self):
        self.blocks=[b.create_genesis_block()]

    def add_block(self,data):
        prev_block=self.blocks[len(self.blocks)-1]
        new_block=b.Block(data,prev_block.hash)
        self.blocks.append(new_block)
        return new_block
'''
1).我们声明一个BlockChain的类，然后里面设置一个blocks列表数据结果，用来存放区块，先把父区块链放进去

2).增加一个add_block函数，用来添加区块：

先生成一个新的区块内存
然后添加data和它的hash值
最后把区块添加到区块链中

'''
