# LRU Cache

## Summary

For this problem we are implementing a Least Recently Used (LRU) Cache. The premise of a LRU Cache
is that it caches items up to a limit based on the ones that were recently used. Once that cache
reaches it's capacity, the least recently used item in the cache is removed.

## Implementation

The way I implemented my cache makes use of two main data structures: a queue, and a dictionary.

The queue is used to keep track of what items have been used recently. Since we want to delete
the least recently used item if our cache is full, we can keep adding items to our queue until
reaches capacity, and then remove the last one. The FIFO behavior of a queue is well suited
to our cache needs. Also, adding and removing items for a queue have a runtime of O(1), which
satisfies the requirements set by the problem.

The cache itself is implemented using a dict. We simply store the items in the dict using a key-value
pair. When our queue has reached it's capacity, the item that is dequed is the stale cache item, so
we use the value of that dequed node to delete the item from our cache. Dicts also have a runtime of
O(1), so this satisfies our implementation requirements as well.