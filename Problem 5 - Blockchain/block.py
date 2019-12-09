import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash=0):
        """
        Creates the Block on the Blockchain using SHA-256 hash and Greenwich Mean Time

        :param data: String of transaction data
        :param previous_hash: Connection to previous block
        """
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")
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
        self.length = 0

    def add_block(self, data=None):
        """
        Adds a block to the blockchain

        :return: None
        """

        # Edge case
        if data is None:
            print("Can't add block without data")
            return

        # If we're adding the first block
        if self.length == 0:
            block = Block(data, 0)
        else:
            block = Block(data, self.blockchain[self.length - 1].hash)

        self.blockchain.append(block)
        self.length += 1

    def __repr__(self):

        # Edge case
        if len(self.blockchain) == 0:
            return "Blockchain empty"

        s = ''
        for i in range(len(self.blockchain)):
            s += "Block " + str(i) + "\n"
            s += str(self.blockchain[i]) + "\n"
        return s


blockchain = BlockChain()

# Edge test cases
print(blockchain)
blockchain.add_block()
print()

# Test cases
blockchain.add_block("0")
blockchain.add_block("1")
blockchain.add_block("2")
print(blockchain)
