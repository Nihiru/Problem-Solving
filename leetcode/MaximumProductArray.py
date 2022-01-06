def max_product(nums):
    if not len(nums):
        return 0
    res = max(nums)
    curMin, curMax = 1, 1
    for n in nums:
        if n == 0:
            curMin, curMax = 1,1
            continue
        tmp = n * curMax  
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n* curMin, n)
        res = max(res, curMax)
    return res


print(max_product([1,2,3,4,5,6,-9]))

