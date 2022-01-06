Input = [1, 2, 1, 2, 3, 3, 4, 5, 5, 6]


def calculate_occurences(input):
    occurences = {}  # { 1: 2, 2: 1}
    for item in input:
        if item in occurences:
            occurences[item] = occurences.get(item) + 1
        else:
            occurences[item] = 1
    return occurences


print(calculate_occurences(Input))
