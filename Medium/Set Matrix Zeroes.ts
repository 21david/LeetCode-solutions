/**
Constant space solution.
Visit every cell in the matrix with two pointers r and c for rows and columns.
If its a 0, mark only first cell of both the row and column as 0. The top row and
leftmost column (the 0 index ones) will be used to store the rows and columns that
need to be converted to 0s.
Once done iterating, go through the first row, and wherever there is a 0,
convert that column to 0s. Do the same for the columns.
However, skip the top-left most cell (0,0) because if it's a 0 and we set either the
row or column to 0, then every other row/column will be set to 0. Instead, we use two
auxiliary variables (firstRow, firstCol) to track if the first row and column needs
to be converted to 0s.
This does up to 3 passes in total, so O(R*C), and constant extra space.
Solved after seeing hints 1-3 and skimming the solution code.
*/
const setZeroes = (matrix: number[][]): void => {
    const [R, C] = [matrix.length, matrix[0].length];
    let firstRow;

    // Iterate, for each 0 cell, set its top-most and left-most cells to 0
    // or firstRow/firstCol if they are in the first row and/or column.
    for (let r = 0; r < R; r++)
        for (let c = 0; c < C; c++) 
            if (matrix[r][c] === 0) {
                if (r === 0) {
                    firstRow = true;
                } else {
                    matrix[0][c] = 0;
                    matrix[r][0] = 0;
                }
            }

    // Edit: These next two loops could be combined by just checking, for each cell
    // if either their topmost cell or leftmost cell was set to 0, then that cell
    // becomes 0. This would reduce them from two passes to one.
    
    // Iterate left column and convert the rows that were set to 0
    for (let r = 1; r < R; r++)
        if (matrix[r][0] === 0)
            for (let c = 1; c < C; c++)
                matrix[r][c] = 0;
    
    // Iterate top row and convert the columns that were set to 0
    for (let c = 0; c < C; c++)
        if (matrix[0][c] === 0)
            for (let r = 1; r < R; r++) 
                matrix[r][c] = 0;

    // Top-left cell is a special case because if it is 0, if we set that
    // column to 0, then all rows will be set to 0, and vice versa if we
    // do it in the opposite order. So we leave it alone and only set firstRow
    // to true if the first row should be set to 0. matrix[0][0] is used for column 0.
    if (firstRow)
        matrix[0] = Array(C).fill(0);
};

/*  
Test case
[[1,2,3,4],
 [5,0,7,8],
 [0,10,11,12],
 [13,14,15,0]]

[[0,0,3,0],  firstRow = false
 [0,0,7,8],
 [0,10,11,12],
 [0,14,15,0]]

Correct output:
[[0,0,3,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]
*/
