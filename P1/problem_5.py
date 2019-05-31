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
        if block is None:
            print("This blockchain has no blocks.")
        while block is not None:
            print(f'This block was created at {block.timestamp} with the data {block.data}. It has a hash of {block.hash}.')
            block = block.previous


# Test Case 1: Empty Chain
chain = BlockChain()
chain.print()
# This blockchain has no blocks.

# Test Case 2: One Block
chain.add_block(1)
chain.print()
# This block was created at <time> with the data 1. It has a hash of <hash>.

# Test case 3: Multiple blocks
chain.add_block(2)
chain.add_block(3)
chain.add_block(4)
chain.add_block(5)
chain.print()
# Each of the blocks printed from most recently to least recently added.
