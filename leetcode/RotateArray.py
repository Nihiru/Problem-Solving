def rotate_array(nums, k):
    """This function is responsible for rotating numbers towards right by  `k` factor

    Args:
        nums (Array): A series of integers
        k (integer): Number of shifts to be done on the array
    """
    if len(nums):
        k = k % len(nums)

        # reversing the whole array without using library functions
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # reversing 0 to `k` numbers
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # reversing `k` to last element numbers
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
    print(nums)


rotate_array([1, 2, 3, 4, 5, 6], 3)
