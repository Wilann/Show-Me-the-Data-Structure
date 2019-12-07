import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        """
        Creates the Block on the Blockchain using SHA-256 hash and Greenwich Mean Time

        :param timestamp: Time when created
        :param data: String of transaction data
        :param previous_hash: Connection to previous block
        """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Calculates hash for information we want to store in the blockchain
        e.g. transaction time, data, previous chain, etc.

        :return: SHA-256 Hash
        """

        # Create SHA-256 Hash Object
        sha = hashlib.sha256()

        # Encode data
        hash_str = self.data.encode('utf-8')

        # Feed encoded byte-like object to sha
        sha.update(hash_str)

        # Return string representation of SHA-256 Hash Object
        return sha.hexdigest()

    def __repr__(self):
        s = ''
        s += "Timestamp: " + self.timestamp + "\n"
        s += "Data: " + self.data + "\n"
        s += "SHA256 Hash: " + str(self.hash) + "\n"
        s += "Prev_Hash: " + str(self.previous_hash) + "\n"
        return s


class BlockChain:

    def __init__(self):
        self.blockchain = []

    def add_block(self, block):
        """
        Adds a block to the blockchain

        :return: None
        """
        self.blockchain.append(block)

    def __repr__(self):
        s = ''
        for i in range(len(self.blockchain)):
            s += "Block " + str(i) + "\n"
            s += str(self.blockchain[i]) + "\n"
        return s


block0 = Block(str(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")), "Block 0's Information",
               0)
block1 = Block(str(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")), "Block 1's Information",
               block0.hash)
block2 = Block(str(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")), "Block 2's Information",
               block1.hash)

blockchain = BlockChain()
blockchain.add_block(block0)
blockchain.add_block(block1)
blockchain.add_block(block2)
print(blockchain)
