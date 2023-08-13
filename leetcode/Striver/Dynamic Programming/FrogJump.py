import sys

"""

Complexity
    Time: O(N) as the operation is performed on each index
    Space: O(N) + O(N) as recursion takes space for each index and space is allocated for them, an array to hold the previously computer values

"""


def action(idx, heights, dp):
    # Base / Stop execution
    if idx == 0:
        return 0

    #  code to convert recursion to dynamic programming by returning already calculated value
    if dp[idx] != -1:
        return dp[idx]

    # calculating previous step
    left = action(idx-1, heights, dp) + abs(heights[idx] - heights[idx - 1])

    # calculating previous two steps
    right = sys.maxsize
    # only calculate if the second step is available
    if idx > 1:
        right = action(idx - 2, heights, dp) + \
            abs(heights[idx] - heights[idx - 2])

    # finding the minimum between the calculated steps
    dp[idx] = min(left, right)
    return dp[idx]


def frog_jump_DP(n, heights):
    dp = [-1] * (n+1)
    action(n-1, heights, dp)
    return dp


ele = [30, 10, 30, 60, 10, 60, 50]
n = len(ele)

# print(frog_jump_DP(n, ele))

"""
-) Approach 2:
    -) Tabulation Method
        -) Following the Bottom-Up technique
        -) Calculation of the next step from the previous step
"""


def frog_jump_tabulation(n, heights):
    dp = [0] * n
    for i in range(1, n):
        fs = dp[i-1] + abs(heights[i] - heights[i-1])
        ss = sys.maxsize
        if i > 1:
            ss = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(fs, ss)
    return dp


# print(frog_jump_tabulation(n, ele))


def frog_jump_optimised(n, heights):
    prev = 0
    prev2 = 0
    for i in range(1, n):
        fs = prev + abs(heights[i] - heights[i-1])
        ss = sys.maxsize
        if i > 1:
            ss = prev2 + abs(heights[i] - heights[i-2])
        curr = min(fs, ss)
        prev2 = prev
        prev = curr
    return prev


print(frog_jump_optimised(n, ele))
