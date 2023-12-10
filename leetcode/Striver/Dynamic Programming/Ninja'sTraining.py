points = [
    [18, 11, 19],
    [4, 13, 7],
    [1,8,13]

]
def f(day, last):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    maxi = 0
    for task in range(3):
        if task != last:
            point = points[day][task] + f(day - 1, task)
            maxi = max(maxi, point)

    return maxi

def main():
    total_no_rows = len(points)
    # passing 3 for the inital run
    return f(total_no_rows - 1, 3)

print(main())