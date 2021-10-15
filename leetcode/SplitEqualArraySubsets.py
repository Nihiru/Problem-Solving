from typing import final


def split_array_subsets(array):
    s = sum(array)
    final_target = s // 2
    if s % 2 != 0:
        return False

    T = [[0] for _ in range(final_target + 1)]  # Initalizing the rows

    for target in range(final_target + 1):
        for partition in range(1, len(array) + 1):
            new_element = array[partition-1]
            closest_if_include = T[target-new_element][partition-1] + \
                new_element if(target-new_element >= 0) else float('-inf')

            closest_if_not_include = T[target][partition-1]
            T[target].append(closest_if_not_include if abs(
                closest_if_not_include-target) < abs(closest_if_include-target) else closest_if_include)

    return T[final_target][len(array)] == final_target


print(split_array_subsets([1, 1, 3, 4, 5]))
