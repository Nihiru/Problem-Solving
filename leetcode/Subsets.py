import math


def generate_subset_iteratively(set_arr):
    """Funciton to generate subset from a set iteratively
    Since, combinations of all the elements in the set is calculated and the way it represented is via
    2^n

    Args:
        set_arr (int): set of unique elements
    """
    set_size = len(set_arr)
    pow_set_size = (int)(math.pow(2, set_size))
    counter = 0
    j = 0
    """Outer loop runs for k times, inner loop runs for n times where k defines number of combinations and
    n defines the number of elements in the array of unique elements
    """
    for counter in range(0, pow_set_size):
        for j in range(0, set_size):
            if ((counter & (1 << j)) > 0):
                print(set_arr[j], end="")
        print("")


# generate_subset_iteratively([1, 2, 3])


def subset_util(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):
        subset.append(A[i])
        subset_util(A, subset, i+1)
        subset.pop(-1)
    return


def generate_subset_recursively(A):
    subset = []
    index = 0
    subset_util(A, subset, index)


print(generate_subset_recursively([1, 2, 3, 4]))
