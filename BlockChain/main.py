import  BlockChain as bc
if __name__=='__main__':
    bcn=bc.BlockChain()
    b1=bcn.add_block('Jack send 1 BTC TO Sam')
    b2=bcn.add_block('Sam send 2 BTC TO lili')
    b3=bcn.add_block('lili send 3 BTC TO Tom')

    for b in bcn.blocks:
        print('Prev Hash:{}'.format(b.previous_hash))
        print('Data:{}'.format(b.data))
        print('Hash:{}'.format(b.hash))
        print('-'*100)
'''
看我们一共创建了3个区块：

第一个区块：是父区块，没有pre_hash,只有数据和一串hash码

第二个区块：是 "Jack发送1个比特币给Sam"它的区块的pre_hash指像前面的父区块hash码

第三个区块：是"Sam发送了2个比特币给lili"它的区块的pre_hash指像前面的Jack区块
'''