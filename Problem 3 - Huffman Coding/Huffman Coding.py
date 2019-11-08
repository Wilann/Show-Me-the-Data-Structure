import sys


def huffman_encoding(data):
    """

    :param data: String
    :return:
    """

    # Determine relative frequencies of characters

    # Build and sort a list of tuples from lowest to highest frequencies

    # Build the Huffman Tree by assigning a binary code to each letter (shorter codes for more frequent letters)

    # Trim Huffman Tree (remove the frequencies from the previously built tree)

    # Encode the text into its compressed form

    # Decode the text form its compressed form

    pass


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
