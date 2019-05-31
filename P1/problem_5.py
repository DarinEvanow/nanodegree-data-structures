import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = f'{self.data}'.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.tail = None

    def add_block(self, data):
        if self.tail is None:
            self.tail = Block(datetime.datetime.utcnow(), data, 0)
        else:
            block = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            block.previous = self.tail
            self.tail = block

    def print(self):
        block = self.tail
        while block is not None:
            print(f'This block was created at {block.timestamp} with the data {block.data}. It has a hash of {block.hash}.')
            block = block.previous


chain = BlockChain()
chain.add_block(1)
chain.add_block(2)
chain.add_block(3)
chain.add_block(4)
chain.add_block(5)
chain.print()
