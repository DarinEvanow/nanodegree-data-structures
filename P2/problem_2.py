def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    # If the list has not been rotated
    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)

    return binary_search(input_list, pivot + 1, len(input_list) - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def find_pivot(input_list, low, high):
    # Base cases
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid

    if mid > low and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[low] >= input_list[mid]:
        return find_pivot(input_list, low, mid - 1)

    return find_pivot(input_list, mid + 1, high)


def binary_search(input_list, low, high, key):
    if high < low:
        return -1

    mid = int((low + high) / 2)

    if key == input_list[mid]:
        return mid

    if key > input_list[mid]:
        return binary_search(input_list, (mid + 1), high, key)

    return binary_search(input_list, low, (mid - 1), key)


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
