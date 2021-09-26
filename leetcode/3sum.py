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
print(three_sum([-4, -2, -2, -1, -1, 0, 1, 2, 3, 4]))
