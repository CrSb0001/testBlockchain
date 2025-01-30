import datetime as d
import hashlib as h

class Block:
  def __init__(self,index,timestamp,data,prevhash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.prevhash = prevhash
    self.hash = self.hashblock()
  def hashblock(self):
    block_encryption = h.sha256()
    block_encryption.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.prevhash))
    return block_encryption.hexdigest()
  
  @staticmethod
  def genesis_block():
    return Block(0,d.datetime.now(),"genesis block transition"," ")

  @staticmethod
  def newblock(lastblock):
    index = lastblock.index+1
    timestamp = d.datetime.now()
    hashblock = lastblock.hash
    data = "Transition "+str(index)
    return Block(index,timestamp,data,hashblock)

blockchain = [Block.genesisblock()]
prevblock = blockchain[0]

print('Block ID #{} '.format(prevblock.index)) 
print('Timestamp: {}'.format(prevblock.timestamp))
print('Hash of the block:{}'.format(prevblock.hash))
print('Previous Block Hash: {}'.format(prevblock.prevhash))
print('data: {}\n'.format(prevblock.data))

for i in range(5):
  add_block = Block.newblock(prevblock)
  blockchain.append(add_block)
  prevblock = add_block
  
  print('Block ID #{}'.format(add_block.index))
  print('Timestamp: {}'.format(add_block.timestamp))
  print('Hash of the block: {}'.format(add_block.hash))
  print('Previous Block Hash: {}'.format(add_block.prevhash))
  pritn('Data: {}\n'.format(add_block.data))
