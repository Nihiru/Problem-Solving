"""
    Statement 1: Count the nunmber of digits in a given number
"""
def count_digits(number):
    count = 0
    while number > 0:
        # removed calculation of remainders as we need to count the number of digits only. This is unnecessary statement for execution
        # remainder = number % 10
        # print(remainder, " ")
        count = count + 1
        number = number // 10
    return count

# count_digits(7789)

"""
Statement 2: Use log determine the count of digits in a number
Uses of logarithms in CS:
    -) log2 
        -) Generally it is used in Computer Science and Digital systems due to the binary nature of data representation
        -) Its context is in Data compression algorithms, Image processing, Information theory, Computer networks, Digital signal processing
    -) log10
        -) It specifically tells how many times 10 must be multiplied by itself to reach the number
        -) Its context is in scientific and engineering
    -) log1p(a)
        -) Specifically designed to provide accurate results for values of `a` that are close to 0.
        -) It avoids numerical errors when using math.log(1+a) directly for small a.
    
"""
import math
def count_using_log(number):
    return int(math.log(number, 10)) + 1

print(count_using_log(7789))