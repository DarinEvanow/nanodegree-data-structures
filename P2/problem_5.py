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

    def suffixes(self, suffix='', suffixes=[]):
        # Recursive function that collects the suffix for
        # all complete words below this point

        suffix += self.char

        if self.is_word:
            suffixes.append(suffix[1:])

        for child in self.children:
            self.children[child].suffixes(suffix, suffixes)

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


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "fraction",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

prefixNode = MyTrie.find('fu')

if prefixNode is not None:
    print(prefixNode.suffixes())
else:
    print('That prefix does not exist in the tree.')

