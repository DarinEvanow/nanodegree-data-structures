# Blockchain

## Summary

A blockchain is simply a linked list where each node in the list contains some data, a timestamp,
and the hash of the previous block in the list.

## Implementation

To create our blockchain, we simply create a linked list where each node is a block. Our blocks
simply have the data needed, and a hash that we create using a hash function on the data of
the block. When inserting a block into the blockchain, we make sure the new block references
not only the previous block in the linked list, but also that it has a reference to the previous
blocks hash. Our blockchain will have similar O(n) for the operations on it, though creating new
blocks does take extra time depending on the difficulty of the hash function.
 