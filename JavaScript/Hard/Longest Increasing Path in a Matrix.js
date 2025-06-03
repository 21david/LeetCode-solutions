/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    const dfs = (r, c) => {
        if (prevResults[r][c] !== null) return prevResults[r][c];

        for (let [deltaR, deltaC] of directions)
            if (inBounds(r + deltaR, c + deltaC) && matrix[r + deltaR][c + deltaC] > matrix[r][c])
                prevResults[r][c] = Math.max(prevResults[r][c], dfs(r + deltaR, c + deltaC));

        return ++prevResults[r][c];
    }

    const [R, C] = [matrix.length, matrix[0].length];
    const prevResults = Array.from({ length: R }, () => Array(C).fill(null));  // DP cache/memoization
    const directions = [[1,0], [-1,0], [0,1], [0,-1]];
    const inBounds = (r, c) => (r >= 0 && r < R) && (c >= 0 && c < C);
    let max = 1;

    // DFS starting from each cell. If a cell has already been
    // visited, it will return immediately, so this is O(R * C) TC
    for (let r = 0; r < R; r++)
        for (let c = 0; c < C; c++)
            max = Math.max(max, dfs(r, c));

    return max;
};

// Made a few modifications after seeing the editorial code
