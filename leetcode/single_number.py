"""Complexity

    Time: O(N) -- traversing all the elements in the array
    Space: O(1) -- only one use of variable
    """


def single_number(nums) -> int:
    """Every element appears twice in the array. Find the one that appears only once

    Args:
        nums (int): Array of non-empty integers 

    Returns:
        int: Number that exists only once in the array
    """
    x = 0
    for ele in nums:
        x ^= ele
    return x


print(single_number([2, 2, 1, 4, 8, 6, 6, 4, 2, 8, 2]))

"""Complexity

    Time: O(N) -- Need to traverse all the elements in the array
    Space: O(N) -- Another array is being used to find single occurence of various numbers
    """


def multi_occurence_of_numbers(nums):
    """Numbers that exist only once in the list of numbers occuring twice

    Args:
        nums ([int]): Array of non-empty lists

    Returns:
        [int]:  Numbers that exists only once in the array
    """
    ret = []
    for ele in nums:
        if ele in ret:
            ret.remove(ele)
        else:
            ret.append(ele)
    return ret


print(multi_occurence_of_numbers([2, 2, 1, 4, 8, 6, 6, 4, 8, 6]))
