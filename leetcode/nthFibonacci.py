"""
Complexity:
    Time: O(N) where N number of fibonacci is acccessed
    Space: O(2^n), At any given time 2 calls are branched out 
"""


def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)


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
