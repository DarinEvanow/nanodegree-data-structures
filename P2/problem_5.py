# Each individual node in the tree
class TrieNode:
    def __init__(self, char):
        # Initialize this node in the Trie
        self.char = char
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        # Collects all the suffixes below a point
        current_node = self
        while suffix != '':
            char = suffix[0]
            current_node = current_node.children.get(char)
            if current_node is None:
                return []

            suffix = suffix[1:]

        suffixes_list = current_node.collect_suffixes('')

        return suffixes_list

    def collect_suffixes(self, suffix):
        # Recursive helper function to help collect suffixes

        suffixes = []
        if self.is_word and suffix != '':
            suffixes.append(suffix)

        for child in self.children:
            suffixes += self.children.get(child).collect_suffixes(suffix + child)

        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode('')

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node


TestTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "fraction",
    "trie", "trigger", "trigonometry", "tripod"
]

for item in wordList:
    TestTrie.insert(item)


# Function used to print out the proper result based on what is passed into it
def f(trie, prefix):
    if prefix != '':
        prefix_node = trie.find(prefix)
        if prefix_node:
            print(prefix_node.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('Please pass in one or more characters')


f(TestTrie, 'f')
# ['un', 'unction', 'actory', 'raction']

f(TestTrie, 'fun')
# ['ction']

f(TestTrie, 'ant')
# ['hology', 'agonist', 'onym']

f(TestTrie, 'z')
# z not found

f(TestTrie, '')
# Please pass in one or more characters not found

