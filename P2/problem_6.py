import random


def get_min_max(ints):
    if len(ints) is 0:
        return "Please pass a non-empty list as an argument."

    min_elem = ints[0]
    max_elem = ints[0]

    for elem in ints:
        if elem < min_elem:
            min_elem = elem
        if elem > max_elem:
            max_elem = elem

    return min_elem, max_elem


# Test Case of Ten Random Integers
random_ints = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(random_ints)
print("Pass" if ((0, 9) == get_min_max(random_ints)) else "Fail")
# Pass

# Test Case for Typical Array of Numbers
print(get_min_max([10, 3, 27, 8, 11, 10, 50, 33]))
# (3, 50)

# Test Case for List with One Element
print(get_min_max([1]))
# (1, 1)

# Test Case for Empty List
print(get_min_max([]))
# Please pass a non-empty list as an argument.
