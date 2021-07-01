"""
Description:
1)  The problem specified can be solved in Dynamic Programming where 2 different approaches can be processed
    1)  Bottom-up approach
        1)  where the cell that needs to be computed i.e, finding the minimum path to it from another cell is calculated based on
            the previously positioned cells which would have already been computed.
        2) Positions considered  are top and left
    2)  Top-up approach

"""
def maximum_path_sum(grid):
    """get the dimensions of the matrix
    N - defines the row length
    M - defines the column length
    """
    N = len(grid)
    M = len(grid[0])
    """
    1)  Calculating the first row and first column values and then proceed by taking the minimum values of its top and right cells.
    2)  At the end we can return the minimum path present at the last cell
    """
    # initializing the first row 
    for i in range(1, M):
       grid[0][i] += grid[0][i-1]
    
    # initializing the first columns
    for j in range(1, N):
        grid[j][0] += grid[j-1][0]

    # computing the minimum path to reach the last cell
    for i in range(1, N):
        for j in range(1, M):
            grid[i][j] +=  min(grid[i-1][j], grid[i][j-1])

    return grid[N-1][M-1]

grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

grid1 = [
    [1,2,3],
    [4,5,6]

]
print(maximum_path_sum(grid))
print(maximum_path_sum(grid1))