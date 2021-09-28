def three_sum(arr, target=0):
    output = []
    # sorting the arr so the search becomes easy
    sorted_arr = sorted(arr)
    for ele in range(len(sorted_arr) - 2):
        if (ele == 0 or (ele > 0 and sorted_arr[ele] != sorted_arr[ele - 1])):

            low = ele + 1
            high = len(sorted_arr) - 1

            sum_to_get = target - sorted_arr[ele]
            while(low < high):
                if (sorted_arr[low] + sorted_arr[high] == sum_to_get):
                    output.append(
                        [
                            sorted_arr[ele],
                            sorted_arr[low],
                            sorted_arr[high]
                        ]
                    )
                    while(low < high and sorted_arr[low] == sorted_arr[low + 1]):
                        low += 1
                    while(low < high and sorted_arr[high] == sorted_arr[high - 1]):
                        high -= 1
                    low += 1
                    high -= 1
                elif (sorted_arr[low] + sorted_arr[high] > sum_to_get):
                    high -= 1
                else:
                    low += 1
    return output


# print(three_sum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]

# [[-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
# print(three_sum([-4, -2, -2, -1, -1, 0, 1, 2, 3, 4]))


def three_sum_closest(arr, target=1):
    comb_sum_set = set()
    sorted_arr = sorted(arr)
    closest_value = None

    """
    .Logic:
        ..fetching all the combinations that sums up to a number
        ..After getting the list of sums from the combinations find the `ranges` of these sums and then 
          selecting the corresponding closest number out of these
    """
    #  Combinational Sums calculation
    for ele in range(len(sorted_arr) - 2):
        # based on the number of integers
        low = ele + 1
        high = len(sorted_arr) - 1
        while(low < high):
            total = sorted_arr[ele] + sorted_arr[low] + sorted_arr[high]
            comb_sum_set.add(total)

            while(low < high and sorted_arr[low] == sorted_arr[low + 1]):
                low += 1
            while(low < high and sorted_arr[high] == sorted_arr[high - 1]):
                high -= 1

            low += 1
            # high -= 1

    # after getting the Combinal Sum Set, find the intervals between the numbers in set and target
    import math
    min = math.inf
    sum_scale = {}

    for i in comb_sum_set:
        if i == target:
            return i
        count = len(range(i, target))
        sum_scale[i] = count

    for key, value in sum_scale.items():
        if value < min:
            min = value
            closest_value = key
    return closest_value


# print(three_sum_closest([-1, 0, 1, 2, -1, -4]))
# print(three_sum_closest([0, 2, 1, -3]))


def sum_of_three_closest(arr, target=1):
    sorted_arr = sorted(arr)
    sorted_arr_len = len(sorted_arr)
    result = sorted_arr[0] + sorted_arr[1] + sorted_arr[sorted_arr_len - 1]
    for i in range(sorted_arr_len):
        j, k = i+1, sorted_arr_len - 1
        while j < k:
            current = sorted_arr[i] + sorted_arr[j] + sorted_arr[k]
            if current == target:
                return target
            elif abs(current - target) < abs(result - target):
                result = current
            elif current > target:
                k -= 1
            else:
                j += 1
    return result


print(sum_of_three_closest([0, 2, 1, -3]))
