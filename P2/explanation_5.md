# Autocomplete with Tries

## Summary

For this problem we want to use a trie to implement functionality similar to Autocomplete. When we search
for a prefix that is contained in our trie, we return a list of the suffixes below that prefix.

## Implementation

The implementation involves creating a trie of nodes where each node has a list of children as a dictionary.
Each key in the dictionary is a character, and the values point to other nodes. Also, each node has a boolean
that dictates whether it is a word. When we add a word into the tree it is done character by character,
with the last character in the word creating a node with the word boolean set to true. Then, when we pass in
a prefix, we can travel our trie down to that node. From there, we can recursively construct suffixes by
traversing all of the nodes below our prefix node, and appending the suffix to a result when we reach
a node that has the word boolean set to true.

## Time and Space Analysis
This algorithm has a runtime of O(n) since when we are constructing the trie, we will need to iterate
over each element in the word and construct the trie while traversing the word. There is a similar runtime
for searching the trie and constructing the suffixes, as we do a similar process of iterating the prefix 
until we get to the node we are looking for, and then begin constructing of the suffixes recursively. The
space complexity of the tree is also O(n), as it is dependent on how many unique characters are in the words
we are passing in, and we only need to construct each node one time.