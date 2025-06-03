/*  
Use 2 sets to store rows and columns that need to be converted.
Or better, 2 arrays.

TC = O(R * C)
SC = O(R + C)

See Set Matrix Zeroes.ts (TypeScript) for the better, constant-space solution.
https://github.com/21david/LeetCode-problems-TypeScript/blob/main/Medium/Set%20Matrix%20Zeroes.ts
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
*/
const setZeroes = function(matrix) {
    const [R, C] = [matrix.length, matrix[0].length];
    const convertRow = Array(R);
    const convertCol = Array(C);

    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (matrix[r][c] === 0) {
                convertRow[r] = true;
                convertCol[c] = true;
            }
        }
    }


    // Rows
    for (let r = 0; r < R; r++) {
        if (convertRow[r]) {
            for (let c = 0; c < C; c++) {
                matrix[r][c] = 0;
            }
        }
    }

     // Cols
    for (let c = 0; c < C; c++) {
        if (convertCol[c]) {
            for (let r = 0; r < R; r++) {
                matrix[r][c] = 0;
            }
        }
    }

};
