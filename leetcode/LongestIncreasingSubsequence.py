def longest_increasing(nums):
    LIS = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    print(LIS)
    return max(LIS)


test_case_1 = [1, 2, 4, 3, 5]
test_case_2 = [1, 2, 4, 3, 5, 7, 8, 12, -20]
print(longest_increasing(test_case_2))
