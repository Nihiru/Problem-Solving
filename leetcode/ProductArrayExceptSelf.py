"""
-) Problem Description:
    -) From the given array calculate the product of all numbers except the current one
    -) Write an algorithm that conforms to O(n) time without using division operator 
    -) Solving the problem in O(1)
-) Outcome
    -) Get the multiplied value of each number in the list except the curreny selected one
"""


def product_array_except_self(arr):
    # Violation of rule 2
    response = []
    result = 1
    for i in arr:
        result *= i

    for i in arr:
        response.append(result//i)

    return response


# print(product_array_except_self([1, 2, 3, 4])) # [24, 12, 8, 6]
def product_array_except_rule_1(nums):
    """
    1) Multiplying the left hand side and right side of the selected number 
    2) Working:
        1) Number present in the LHS is multiplied with the next number in the list and cached
        2) The multiplied number is cached and used as reference to multiplied to the next number in the list
        3) Same goes for RHS where the cached value is dependent of the previous number in the list
        3) This is stopped until the position of the selected number is reached
        4) Multiply both the LHS and RHS to get the expected outcome
    """
    output = [1] * len(nums)
    left_hand_arr = [1] * len(nums)
    right_hand_arr = [1] * len(nums)

    for i in range(1, len(nums)):
        left_hand_arr[i] = left_hand_arr[i-1] * nums[i-1]

    for i in range(len(nums) - 2, -1, -1):
        right_hand_arr[i] = right_hand_arr[i+1] * nums[i+1]

    for i in range(len(nums)):
        output[i] = left_hand_arr[i] * right_hand_arr[i]

    return output


def product_array_except_rule_2(nums):
    output = [1] * len(nums)
    L = len(output)
    for i in range(1, L):
        output[i] = output[i-1] * nums[i-1]
    r = 1
    for i in range(L-1, -1, -1):
        output[i] = output[i] * r
        r = r * nums[i]
    return output


print(product_array_except_rule_1([1, 2, 3, 4]))
