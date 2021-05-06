def single_number(nums) -> int:
    """Every element appears twice in the array. Find the one that appears only once

    Args:
        nums (int): Array of non-empty integers 

    Returns:
        int: Number that exists only once in the arra
    """
    x = 0
    for ele in nums:
        x ^= ele
    return x


print(single_number([2, 2, 1, 4, 8, 6, 6, 4, 2, 8, 6]))
