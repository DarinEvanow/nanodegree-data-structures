import heapq
import sys


class Node:
    def __init__(self, char, freq):
        self.char = char    # The character that the node is representing in our tree
        self.freq = freq    # The frequency in which the character appears in the text we are going to encode
        self.left = None    # A reference to the left child node.
        self.right = None   # A reference to the right child node.

    # Below are custom comparison operators we need for sorting our nodes into the priority queue.
    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []               # Used as a priority queue in order help when constructing the tree
        self.codes = {}              # Used to keep track of the characters and their corresponding value
        self.character_mapping = {}  # Used to keep track of the compressed code and their corresponding character

    def make_frequency_dict(self, text):
        """
        Creates a dict containing the frequencies of all the characters in the passed in text

        :param text: the next that we want to make a frequency dict of
        :return: a dict containing the frequency of all of the characters in our text
        """
        frequency = {}
        for character in text:
            if character not in frequency:
                frequency[character] = 0
            frequency[character] += 1

        return frequency

    def make_tree(self, frequency):
        """
        Creates a tree from the dict containing the frequency of all characters in our text

        :param frequency: a dict containing the frequencies of all the characters in the text
        :return: a tree (specifically a heap) of all the nodes with the character and frequency stored in the nodes
        """
        for key in frequency:
            node = Node(key, frequency[key])
            heapq.heappush(self.heap, node)

        self.merge_nodes()

    def merge_nodes(self):
        """
        Trims down the nodes in our tree.

        :return: A new tree with the merged nodes
        """

        while len(self.heap) > 1:
            # Get the two nodes with the lowest frequency from the heap.
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            # Create a new node with the combined frequency of the least occurring nodes in the heap.
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            # Push the new node onto the heap.
            heapq.heappush(self.heap, merged)

    def make_codes(self):
        """
        Calls our recursive function to set our codes.

        :return: No return, but will set the instance variable for our mapping to and from code to character.
        """
        root = heapq.heappop(self.heap)
        current_code = ""
        self.do_make_codes(root, current_code)

    def do_make_codes(self, root, current_code):
        """
        The actual recursive function that we use to make our codes.

        :param root: The root of our tree.
        :param current_code: The current code that we are assigning to the value for our current node.
        :return: No return, but will set the instance variable for our mapping to and from code to character.
        """
        # Base case to break out of leaf nodes
        if root is None:
            return

        # Add the code to our codes map, and update our character mapping so we can decode later.
        if root.char is not None:
            self.codes[root.char] = current_code
            self.character_mapping[current_code] = root.char

        # Recursively repeat this process for the left and right nodes, adding the appropriate bit for the code
        # of the nodes on the lower levels of our tree.
        self.do_make_codes(root.left, current_code + "0")
        self.do_make_codes(root.right, current_code + "1")

    def get_encoded_text(self, text):
        """
        Encodes a string using our Huffman tree values.

        :param text: The text that we are going to encode using the codes created from our Huffman tree.
        :return: A series of bits that represent our encoded text.
        """
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]

        return encoded_text

    def compress(self, text):
        """
        Compresses our text using Huffman coding.

        :param text: The text we want to encode.
        :return: Our encoded text as a series of bits.
        """
        frequency = self.make_frequency_dict(text)
        self.make_tree(frequency)
        self.make_codes()
        encoded_text = self.get_encoded_text(text)

        return encoded_text

    def decompress(self, encoded_text):
        """

        :param encoded_text: The series of bits that represent our encoded text.
        :return: Our original text.
        """
        current_code = ""
        decoded_text = ""

        # Loop over our bits, building a code string as we go. When we find a code string that matches something in our
        # character mapping, append that character to our decoded text.
        for bit in encoded_text:
            current_code += bit
            if current_code in self.character_mapping:
                character = self.character_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


if __name__ == "__main__":
    compressor = HuffmanCoding()

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = compressor.compress("The bird is the word")

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = compressor.decompress(encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

