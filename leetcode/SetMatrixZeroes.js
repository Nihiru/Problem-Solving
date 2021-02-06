var setMatrixZeroesBF = function (matrix) {
    // size  of the matrix
    let height = matrix.length // no of rows
    let width = matrix[0].length // no of columns

    let row_zeroes = new Array(height).fill(false)
    let col_zeroes = new Array(width).fill(false)

    for (let row = 0; row < height; ++row) {
        for (let col = 0; col < width; ++col) {
            if (matrix[row][col] == 0) {
                row_zeroes[row] = true
                col_zeroes[col] = true
            }
        }
    }

    // changing the matrix
    for (let row = 0; row < height; ++row) {
        for (let col = 0; col < width; ++col) {
            if (row_zeroes[row] || col_zeroes[col]) {
                matrix[row][col] = 0
            }
        }
    }

    console.log(`After performing operation ${matrix}`)
}

var setMatrixZeroesEF = function (elements) {

}


setMatrixZeroesBF([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
setMatrixZeroesBF([
    [4, 7, 2, 5],
    [3, 5, 0, 4],
    [1, 0, 1, 3],
    [5, 6, 9, 9],
    [7, 8, 2, 0]
])