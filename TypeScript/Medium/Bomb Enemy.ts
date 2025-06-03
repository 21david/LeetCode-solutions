// LeetCode Premium problem
function maxKilledEnemies(grid: string[][]): number {
    let [R, C] = [grid.length, grid[0].length];

    // Matrix to record how many kills can be done from each cell
    let kills = Array.from({ length: R }, () => Array(C).fill(0));
    let max = 0;

    // Row traversals
    for (let r = 0; r < R; r++) {
        // Count the total for each row
        let count = 0;
        let prevStart = 0;
        for (let c = 0; c <= C; c++) {
            if (c === C || grid[r][c] === 'W') {
                // iterate from prevStart to previous position (to exclude the wall)
                // and fill in the count into every corresponding cell in kills
                for (let i = prevStart; i < c; i++) {
                    if (grid[r][i] === 'E') continue;  // Can't place on an enemy
                    kills[r][i] += count;
                }

                prevStart = c + 1;
                count = 0;
            } else if (grid[r][c] === 'E') {
                count++;
            }
        }
    }

    // Column traversals
    for (let c = 0; c < C; c++) {
        // Count the totals for each column
        let count = 0;
        let prevStart = 0;
        for (let r = 0; r <= R; r++) {
            if (r === R || grid[r][c] === 'W') {
                // iterate from prevStart to previous position (to exclude the wall)
                // and fill in the count into every corresponding cell in kills
                for (let i = prevStart; i < r; i++) {
                    if (grid[i][c] === 'E') continue;
                    kills[i][c] += count;
                    max = Math.max(kills[i][c], max);
                }

                prevStart = r + 1;
                count = 0;
            } else if (grid[r][c] === 'E') {
                count++;
            }
        }
    }

    return max;
};
