type ZeroArrayFunc = (nums: number[], queries: number[][]) => boolean;

const isZeroArray: ZeroArrayFunc = (nums, queries) => {
    const N = nums.length;

    // 1. Build Line Sweep array with queries
    const lineSweep = Array(N + 1).fill(0);
    for (const [l, r] of queries) {
        lineSweep[l]++;
        lineSweep[r+1]--;
    }

    // 2. Check if the running sum is always ≥ nums at each index
    let sum = 0;
    for (let i = 0; i < N; i++) {
        sum += lineSweep[i];
        if (sum < nums[i])
            return false;
    }

    // If the lineSweep running sum was always ≥, then that means
    // all the numbers in nums could be decremented to 0
    return true;
};
