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

    # If the pivot point is the number we are looking for, return it
    if input_list[pivot] == number:
        return pivot

    # If the front section of our array is less than the number we are looking for, search everything before the pivot
    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)

    # Search everything after the pivot
    return binary_search(input_list, pivot + 1, len(input_list) - 1, number)


def find_pivot(input_list, low, high):
    """
    Used to find the index of the pivot point, which is where the list has
    been rotated from in the case it has been rotated, and returns it
    """
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


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
# 2

print(rotated_array_search([1], 1))
# 0

print(rotated_array_search([0], 1))
# -1
