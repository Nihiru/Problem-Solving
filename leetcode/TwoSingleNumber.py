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
