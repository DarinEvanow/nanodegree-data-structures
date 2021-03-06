class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Queue:

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity

    def queue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif self.size == self.capacity:
            self.tail = self.tail.previous
            self.tail.next = None
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.size += 1

    def deque(self):
        if self.tail is None:
            return
        elif self.head == self.tail:
            return_node = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return return_node
        else:
            return_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return return_node

    def is_full(self):
        return self.capacity == self.size


class LRUCache(object):

    def __init__(self, capacity):
        self.queue = Queue(capacity)
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            return
        elif self.queue.is_full():
            stale_key = self.queue.deque().value
            del self.cache[stale_key]

        self.queue.queue(key)
        self.cache[key] = value


our_cache = LRUCache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(1))
# Test case #1. This should return '-1' since our cache has a limit of 5, and we have set 6 items.

print(our_cache.get(2))
# Test case #2. This should return '2' since we have set 2 and it falls within our limit.

print(our_cache.get(7))
# Test case #2. This should return '-1' since we never set the number '7'
