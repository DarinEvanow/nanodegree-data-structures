class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def contains(self, value):
        current = self.head
        while current and current.value is not value:
            current = current.next

        if current is not None:
            return True
        else:
            return False


def union(llist_1, llist_2):
    union_list = LinkedList()
    current = llist_1.head
    while current:
        if not union_list.contains(current.value):
            union_list.append(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if not union_list.contains(current.value):
            union_list.append(current.value)
        current = current.next
    return union_list


def intersection(llist_1, llist_2):
    intersect_list = LinkedList()
    llist_1_size = llist_1.size()
    llist_2_size = llist_2.size()
    if llist_1_size > llist_2_size:
        larger_list = llist_1
        smaller_list = llist_2
    else:
        larger_list = llist_2
        smaller_list = llist_1

    current = larger_list.head
    while current:
        if smaller_list.contains(current.value) and not intersect_list.contains(current.value):
            intersect_list.append(current.value)
        current = current.next

    if intersect_list.size() is 0:
        return 'These two lists have no common elements'

    return intersect_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Union #1')
print(union(linked_list_1,linked_list_2))
print('Intersect #1')
print(intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print('Union #2')
print(union(linked_list_3, linked_list_4))
print('Intersect #2')
print(intersection(linked_list_3, linked_list_4))
