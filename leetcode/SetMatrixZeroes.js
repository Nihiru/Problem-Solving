// space utilization
class SetZeroMatrix {
    constructor(matrix = null) {
        this.matrix = matrix
    }

    setMatrixZeroes = (choice) => {
        // size  of the matrix
        let height = this.matrix.length // no of rows
        let width = this.matrix[0].length // no of columns

        let row_zeroes = new Array(height).fill(false)
        let col_zeroes = new Array(width).fill(false)

        switch (choice) {
            case 1: {
                /**
                 * Time Complexity: O(n^2)
                 * Space complexity: O(H+W)
                 */
                for (let row = 0; row < height; ++row) {
                    for (let col = 0; col < width; ++col) {
                        if (this.matrix[row][col] == 0) {
                            row_zeroes[row] = true
                            col_zeroes[col] = true
                        }
                    }
                }

                for (let row = 0; row < height; ++row) {
                    for (let col = 0; col < width; ++col) {
                        if (row_zeroes[row] || col_zeroes[col]) {
                            this.matrix[row][col] = 0
                        }
                    }
                }
                break;
            }
            /**
             * Approach 1
             * 1) remove the row array and convert it into a bool checked value. By this space complexity has reduced to O(width)
             * 2) remove the col array 
             */
            case 2: {
                // col_zeroes is required as it would identify the zeroes in the matrix
                for (let row = 0; row < height; ++row) {
                    for (let col = 0; col < width; ++col) {
                        if (this.matrix[row][col] == 0) {
                            col_zeroes[col] = true
                        }
                    }
                }

                for (let row = 0; row < height; ++row) {
                    let contains_zero = false;
                    for (let col = 0; col < width; ++col) {
                        if (this.matrix[row][col] == 0) {
                            contains_zero = true
                            break;
                        }
                    }

                    for (let col = 0; col < width; ++col) {
                        if (contains_zero || col_zeroes[col])
                            this.matrix[row][col] = 0
                    }
                }
                break
            }
            case 3: {
                let first_row_zero = false
                for (let col = 0; col < width; ++col) {
                    if (this.matrix[0][col] == 0)
                        first_row_zero = true
                }

                /**
                 * identifying the 0's in cells and setting the respective 0th column to 0
                 * */
                for (let row = 0; row < height; ++row) {
                    for (let col = 0; col < width; ++col) {
                        if (this.matrix[row][col] == 0)
                            this.matrix[0][col] = 0
                    }
                }


                for (let row = 1; row < height; ++row) {
                    // assuming each row doesn't have 0's in their cells
                    let contains_zero = false
                    for (let col = 0; col < width; ++col) {
                        if (this.matrix[row][col] == 0) {
                            // `row` has zero in it
                            contains_zero = true
                            break
                        }
                    }
                    // after knowing the existence of 0's in cells of the row and updating each cell of the row to 0
                    for (let col = 0; col < width; ++col) {
                        if (contains_zero || this.matrix[0][col] == 0)
                            this.matrix[row][col] = 0
                    }
                }
                // updating 0's in the first row if any of the cell in the first row has 0's in it `first_row_zero` verifies the existence
                if (first_row_zero) {
                    for (let col = 0; col < width; ++col)
                        this.matrix[0][col] = 0
                }
                break
            }
        }


        console.log(`After performing operation ${this.matrix}`)
    }
}


let smzObj = null
smzObj = new SetZeroMatrix([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]).setMatrixZeroes(1)


smzObj = new SetZeroMatrix([
    [4, 7, 2, 5],
    [3, 5, 0, 4],
    [1, 0, 1, 3],
    [5, 6, 9, 9],
    [7, 8, 2, 0]
]).setMatrixZeroes(3)