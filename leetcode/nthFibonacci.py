"""
Complexity:
    Time: O(N) where N number of fibonacci is acccessed
    Space: O(2^n), At any given time 2 calls are branched out 
"""


def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)


# print(getNthFib(3))

"""
Complexity:
    Time: O(N) where N number of fibonacci is acccessed
    Space: O(N), At any given time only N numbers exists in the callstack
"""


def getNthFibMem(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = getNthFibMem(n-1, mem) + getNthFibMem(n-2, mem)
        return mem[n]


"""
Complexity:
    Time: O(N) where N number of fibonacci is acccessed
    Space: O(1), because nothing is being stored expected for constant space
"""


def getNthFibIter(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


def tribonacci(n):
    """
    Tribonacci is defined as
    T0 = 0, T1 = 1, T2 = 1 and for T(n+3) = T(n) + T(n+1) + T(n+2)
    """
    # if n <= 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    # else:
    #     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

    dp = [0, 1, 1]
    for i in range(3, n+1):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])

    return dp[n]


# print(tribonacci(4))


def climbing_stairs(n):
    """ 
    - Observations
        - Perspective
            - Either start from first step and look first by selecting 1 or 2 steps to go forward and reach destination
            - Or from the reached step look backward and understand the logic taken to reach that point
    - Complexity
        - Time: O(N) each element is traversed to calculate the next values in the list
        - Space: O(N) to store the calculated values
    - A Fibonacci Sequence pattern occurs when this problem is dissected manually.
    """
    # dp = [1, 1] + [0] * (n-1)  # F(1) = 1, F(2) = 1
    # # Calculating from F(3) based on F(1) + F(2)
    # for i in range(2, n+1):
    #     # Current problems solution is dependent on previous solution
    #     dp[i] = dp[i-1] + dp[i-2]

    # return dp[n]

    a, b = 1, 1
    c = a + b
    for _ in range(n-2):  # halting condition is n-2 because we've already calculated the F(1) and F(2)
        a = b
        b = c
        c = a + b

    return c


print(climbing_stairs(4))
