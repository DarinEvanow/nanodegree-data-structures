def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base cases
    if number is 0 or number is 1:
        return number

    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = number
    while start <= end:
        mid = (start + end) // 2

        # If the number we are looking for is a perfect square
        if mid * mid is number:
            return mid

        if mid * mid < number:
            start = mid + 1
            floored_square_root = mid
        else:
            end = mid - 1

    return floored_square_root


print(sqrt(9))
# 3

print(sqrt(0))
# 0

print(sqrt(16))
# 4

print(sqrt(1))
# 1

print(sqrt(27))
# 5
