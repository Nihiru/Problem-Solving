""" 
-) return the `maximum length` of contiguous sub-array with equal number of 0 & 1

"""


def findMaxLength(nums, approach=1):
    counts = {0: -1}
    max_len = 0
    count = 0
    if approach == 1:
        for i in range(len(nums) - 2):
            zero_count = ones_count = 0
            for j in range(i, len(nums) - 1):
                if nums[j] == 0:
                    zero_count += 1
                else:
                    ones_count += 1

                if zero_count == ones_count:
                    max_len = max(max_len, j - i + 1)
    elif approach == 2:
        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1

            if count in counts:
                max_len = max(max_len, i - counts.get(count))

            else:
                counts[count] = i
    return max_len


arr = [0, 1, 1, 0, 1, 0, 1, 1]
print(findMaxLength(arr, 1))
