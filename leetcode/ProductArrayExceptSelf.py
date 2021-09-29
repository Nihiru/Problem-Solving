"""
-) Problem Description:
    -) From the given array calculate the product of all numbers except the current one
    -) Write an algorithm that conforms to O(n) time without using division operator 
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

def product_array_except_self_optimized(arr):
    pass
