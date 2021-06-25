"""
Problem Statement:

1) Given an array of integers and a target. return indices of the two numbers such that they add up to target
2) Using of the same element twice is prohibited
3) Come up with an algorithm that is less than O(n^2) time complexity ?

"""
def two_sum(nums=[], target=0, approach=1):
    nums_length = len(nums)
    if nums_length == 0:
        return "No element present"
    elif nums_length == 1:
        return  "Need one more element to perform the operation"
    elif nums_length == 2:
        return f"Maximum sum of two indices: {nums[0]+ nums[1]}"
    else:
        if approach == 1:
            """approach 1
            1) Time complexity - O(n^2) as traversing the array twice
            2) Space complexity - 0(1) as no extra memory is consumed while performing this operation
            """
            for i in range(nums_length):
                for j in range(i+1, nums_length):
                    if nums[i] + nums[j] == target:
                        return (i+1,j+1)
        elif approach == 2:
            """approach 2
            1) Time complexity - O(n) as traversing the array only once. Each look up in the table costs O(1) time
            2) Space complexity - O(n) as hash would require the elements present in the array for comparison
            """
            # calculate difference = target - x i.e, x points to the elements
            hash = {}
            for i in range(nums_length):
                diff = target - nums[i]
                if diff in hash:
                    return  (hash.get(diff, 0) + 1, i+1)
                else:
                    hash[nums[i]] = i
        else:
            pass
        return "Target cannot be calculated with the given array"

        




print(two_sum([1,2,3,4,5], 10, 2))