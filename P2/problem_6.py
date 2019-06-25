import random

def get_min_max(ints):
    if len(ints) is 0:
        return -1

    pivot = ints[len(ints) // 2]
    smaller = []
    larger = []
    for elem in ints:
        if elem < pivot:
            smaller.append(elem)
        if elem > pivot:
            larger.append(elem)

    return get_min(smaller), get_max(larger)


def get_max(ints):
    pivot = ints[len(ints) // 2]
    larger = []
    for elem in ints:
        if elem > pivot:
            larger.append(elem)

    if len(larger) is 0:
        return pivot
    else:
        return get_max(larger)


def get_min(ints):
    pivot = ints[len(ints) // 2]
    smaller = []
    for elem in ints:
        if elem < pivot:
            smaller.append(elem)

    if len(smaller) is 0:
        return pivot
    else:
        return get_min(smaller)


# Example Test Case of Ten Integers
random_ints = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(random_ints)

print("Pass" if (9 == get_max(random_ints)) else "Fail")
print("Pass" if (0 == get_min(random_ints)) else "Fail")
print("Pass" if ((0, 9) == get_min_max(random_ints)) else "Fail")

# Example Test Case of Empty List
print("Pass" if (-1 == get_min_max([])) else "Fail")