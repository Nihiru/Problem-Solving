def replacing_zeros_with_fives(n):
    """Function to replace all zeros with fives
    should not use strings, arrays or any other data types to store digits

    Args:
        number (int): number from which zeroes needs to be replaced with fives
    """
    if n == 0:
        return 5
    ans = 0
    exponent = 0

    while n:
        n, r = divmod(n, 10)
        if r == 0:
            r = 5
        ans += r*10**exponent
        exponent += 1
    return ans


print(replacing_zeros_with_fives(102))
