def search(nums, target):
    """
    -) Function to search for a given `target` in an array `nums`
    -) Using extended version of binary search algorithm to provide a solution

    Args:
        nums (List): List of rotated array
        target (Integer): To find the spcecific target

    Returns:
        [Integer]: Position of the given `target` or -1
    """
    l, r = 0, len(nums) - 1
    """
        -) `l` and `r` are the pointers that provides the range for which the search has to be performed
        -) without these, search operation takes an longer approach
        -)  
     """
    while l <= r:
        # fetching the middle number position
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # starting from the first sorted position i.e, left part of the position
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1  # moving onto the next set of array
            else:
                r = mid - 1  # closing in on the current array
        #
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1  # look into the current array
            else:
                l = mid + 1  # look into the left part of the array
    return -1


arr = [4, 5, 6, 7, 8, 9, 10, -1, 0, 1, 2, 3]
arr1 = [4, 5, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, ]
target = -1
print(search(arr1, target))
