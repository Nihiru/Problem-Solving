def rob(nums):
    """below code would not work for test cases
    [2,1,1,2]
    [10,1,1,1,1,10]
    [25,1,2,27,6,6,88,1]
    """
    n = len(nums)
    # even_numbers = odd_numbers = 0
    # for i in range(1, n, 2):
    #     odd_numbers += nums[i]
    # for j in range(0, n, 2):
    #     even_numbers += nums[j]
    # return max(odd_numbers, even_numbers)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    return dp[n-1]


# nums = [2, 1, 1, 2]
nums = [10, 1, 1, 10]
# nums = [25, 1, 2, 27, 6, 6, 88, 1]
print(rob(nums))
