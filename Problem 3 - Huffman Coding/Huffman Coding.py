import sys


class Node:
    def __init__(self, letter=None, frequency=None, left_child=None, right_child=None):
        self.letter = letter
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child
        self.binary_code = ''

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def __str__(self):
        s = 'Node(' + self.letter + ', ' + str(self.frequency) + ')'
        return s


class Tree:
    def __init__(self, node):
        self.root = node
        self.visit_order = []

    def create_binary_codes(self, node):
        """
        Creates binary codes by traversing in-order
        :param node: root
        :return:
        """
        if node:
            # If there's a left child
            if node.get_left_child() is not None:
                # Traverse left subtree
                self.create_binary_codes(node.get_left_child())

                # Update binary code
                node.binary_code += '0'

            # visit node
            self.visit_order.append(node)

            # If there's a right child
            if node.get_right_child() is not None:
                # traverse right sub-tree
                self.create_binary_codes(node.get_right_child())

                # Update binary code
                node.binary_code += '1'

    # TODO: Define str for Tree
    def __str__(self):
        s = ''
        return s


class PriorityQueue:
    def __init__(self):
        self.queue = []  # Queue of Nodes
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def put(self, node):
        self.queue.append(node)
        self.length += 1

    def pop_least_frequent(self):
        least_frequent_node = self.queue[0]  # Least frequent node
        index = 0  # Index of least frequent node

        # Find least frequent node
        for i in range(self.length):
            if self.queue[i].frequency < least_frequent_node.frequency:
                least_frequent_node = self.queue[i]
                index = i

        # Decrement length of queue
        self.length -= 1

        # Remove node
        del self.queue[index]

        # Return node
        return least_frequent_node

    def __str__(self):
        s = ''
        for node in self.queue:
            s += node.__str__() + ', '
        return s


def huffman_encoding(data):
    """
    Encodes data using Huffman Encoding

    Sequence of encoded characters (on the leaves of the Huffman Tree) makes up the Huffman Code

    :param data: String to encode
    :return: encoded_data: Encoded data
    :return: binary_tree: Binary tree with characters on leaves
    """

    # Convert data to lowercase
    data = data.lower()
    print("data:", data)

    # Determine frequencies of each character and store in dictionary of (character --> frequency)
    frequencies = dict()
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    print("frequencies:", frequencies)

    # Build Priority Queue by iterating through data
    priority_queue = PriorityQueue()
    for char in frequencies:
        # Build Nodes using (character --> frequency) dictionary
        node = Node(char, frequencies[char])

        # Insert Nodes into a Priority Queue
        priority_queue.put(node)
    print("priority_queue:", priority_queue)

    # Build the Huffman Tree from Priority Queue
    while priority_queue.length > 1:
        # Pop 2 nodes with least frequency count
        node1 = priority_queue.pop_least_frequent()
        node2 = priority_queue.pop_least_frequent()

        # Create a parent node with: sum of frequencies of 2 nodes, left and right child which are the 2 nodes
        parent_node_frequency = node1.frequency + node2.frequency
        parent_node = Node('', parent_node_frequency, node1, node2)

        # Push parent node back into Priority Queue
        priority_queue.put(parent_node)

    # Finally, the priority queue will have 1 node that represents the root of the tree
    print("priority_queue after creating tree:", priority_queue)

    # Create (character --> binary code) dictionary
    # binary_codes = dict()

    # Assign a binary code to each letter (shorter codes for more frequent letters)
    # From the root, every time we go left, we add a 0 & every time we go right, we add a 1
    # When we hit a leaf node that holds a letter, we return that binary code and assign it to that letter
    # e.g. 0111 is "left right right right", so binary_codes[letter] = "0111"
    root = priority_queue.queue[0]
    binary_tree = Tree(root)
    binary_tree.create_binary_codes(root)
    print("binary_tree:", binary_tree)

    # Encode text into its compressed form (sequence of binary codes that were assigned to each letter)
    # Read input and access (character --> binary code) dictionary
    # E.g. binary_codes[first_letter] + binary_codes[second_letter] + ...
    compressed_form = ''
    for node in binary_tree.visit_order:
        compressed_form += node.binary_code
    print("compressed_form:", compressed_form)

    return compressed_form, binary_tree


def huffman_decoding(data, tree):
    """
    Decodes data on a tree using Huffman Decoding

    :param data:
    :param tree:
    :return:
    """
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
