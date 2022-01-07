# testcases
test_case_1 = [1, 2, 4, 3, 5]
test_case_2 = [1, 2, 4, 3, 5, 7, 8, 12, -20]

"""
-) Bottom-Up approach
    -) Dynamic Programming
        -) Space Complexity: O(n^2)
        -) Time Complexity: O(N)
"""


def longest_increasing_I(nums):
    LIS = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    print(LIS)
    return max(LIS)

# print(longest_increasing_I(test_case_2))


"""
-) Brute-force recursion (Time Limit Exceed)
    -) Space Complexity: O(2^n)
    -) Time Complexity: O(N)
"""


def longest_increasing_II(nums) -> int:
    def max_lis(idx, cur_max):
        # Base Case
        if idx == len(nums):
            return 0
        # Recursive Case
        if nums[idx] > cur_max:
            return max(1 + max_lis(idx + 1, nums[idx]), max_lis(idx + 1, cur_max))
        return max_lis(idx + 1, cur_max)
    return max_lis(0, float('-inf'))


# print(longest_increasing_II(test_case_1))

""" 
-) Dynamic Programming + Binary Search
    -) Time Complexity: O(n log(n))
    -) Space Complexity: O(n)

"""


def longest_increasing_III(nums):
    if not nums:
        return 0
    dp = [nums[0]]
    len_dp = 1
    for i in range(1, len(nums)):
        left, right = 0, len(dp) - 1
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < nums[i]:
                left = mid + 1
            else:
                right = mid
        if dp[left] < nums[i]:
            dp.append(nums[i])
            len_dp += 1
        else:
            dp[left] = nums[i]
    return dp, len_dp


print(longest_increasing_III(test_case_2))
