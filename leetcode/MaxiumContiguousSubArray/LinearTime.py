def maxSubArray(self, array) -> int:
    max_sum = array[0]
    current_sum = max_sum
    for ele in array[1:]:
        """ 
        -) Logic:
            1) Two
        """
        current_sum = max(ele + current_sum, ele)
        max_sum = max(current_sum, max_sum)

    return max_sum
