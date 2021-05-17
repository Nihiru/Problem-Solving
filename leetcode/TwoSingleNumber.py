def single_number_II(nums):
    hash = {}
    for ele in nums:
        if ele in hash:
            hash[ele] = hash.get(ele) + 1
        else:
            hash[ele] = 1
    for key in hash.keys():
        if hash[key] < 3:
            return key

    return None


print(single_number_II([2, 2, 2, 3, 3, 3, 4, 1, 4, 4, 5, 1, 1, 5]))


def single_number_II_one_line_solution(nums):
    return (3*sum(set(nums))-sum(nums))//2


print(single_number_II_one_line_solution(
    [2, 2, 2, 3, 3, 3, 4, 4, 4, 1, 5, 5, 5]))


def single_number_II_bit_manipulation(nums):
    ans = 0
    x = 1
    """bitwise left shift operator moves the bits of its first operand to the left by the number of places 
    specified in the second operand    
    """
    mask = (x << 31)
    while(mask):
        count = 0
        for i in list(range(len(nums))):
            # here (mask & nums[i]) returns 0 or 1 based on least-significant bit of mask
            if mask & nums[i]:
                count += 1
        if count % 3 != 0:
            ans += mask
        mask >>= 1
    return ans


print(single_number_II_bit_manipulation(
    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5]
))
