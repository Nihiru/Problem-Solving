def find_min(nums):
    # return min(nums) # approach takes O(N) time
    low = 0
    high = len(nums) - 1
    if nums[high] > nums[0]:
        return nums[0]

    # performing a binary search to get time complexity as O(log N)
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            low = mid + 1
        else:
            high = mid - 1


arr = [4, 5, 6, 7, 8, 0, 1, 2, 3]
print(find_min(arr))
