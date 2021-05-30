
def max_sub_array(nums):
    n = len(nums)
    maximum_sub_rray = float('-inf')
    for left in range(n):
        running_window_sum = 0
        for right in range(left, n):
            running_window_sum += nums[right]
            maximum_sub_rray = max(maximum_sub_rray, running_window_sum)

    return maximum_sub_rray


print(max_sub_array([-4, -3, -2, -1, 0, 1, 2, 3, 4]))
