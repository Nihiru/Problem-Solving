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


def frog_jump(n, heights):
    dp = [-1] * (n+1)
    return action(n-1, heights, dp)


print(frog_jump(5, [30, 10, 30, 60, 10, 60, 50]))
