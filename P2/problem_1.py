def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is 0 or number is 1:
        return number
    else:
        i = 1
        result = 1
        while result <= number:
            i += 1
            result = i * i

    return i - 1


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
