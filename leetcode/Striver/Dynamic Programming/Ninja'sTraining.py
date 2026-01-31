points = [[18, 11, 19], [4, 13, 7], [1, 8, 13]]


def tabulation_f(day):
    dp = [[-1] * 4] * 4
    total_no_rows = len(points)

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    for day in range(day):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], points)

    return dp[total_no_rows - 1][3]


def recursive_f(day, last, memoization_array):
    """
    -) base case that stops the execution
    -) only executes when it has reached the last array for processing. here, last array can be first or last one depending on the approach followed (Top-Down or Bottom-Up)
    -) approach is to perform all the options from the given input array
    -) there are repetitive tasks hence the memoization
    """
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    # DP array check if the given sub routine is already calculated and ready to be reused
    if memoization_array[day][last] != -1:
        return memoization_array[day][last]

    maxi = 0

    for task in range(3):
        if task != last:
            point = points[day][task] + recursive_f(day - 1, task, memoization_array)
            maxi = max(maxi, point)

    memoization_array[day][last] = maxi

    return memoization_array[day][last]


def main():
    dp = [[-1] * 4] * 4
    total_no_rows = len(points)
    # passing 3 for the inital run
    return recursive_f(total_no_rows - 1, 3, memoization_array=dp)


print(main())
