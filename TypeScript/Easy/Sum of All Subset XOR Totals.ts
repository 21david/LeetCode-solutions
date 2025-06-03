/* 
Explore each subset, but accumulate the XOR of the eggs as you are exploring 
each subset. When you've completed one subset, add the sum to a total sum 
variable. 

TC = O(2^N)
SC = O(N) due to call stack
 */
function subsetXORSum(nums: number[]): number {
    let total = 0;
    const subset = (i, acc) => {
        if (i == nums.length) {
            total += acc;
            return;
        }

        subset(i + 1, acc);  // Skip
        subset(i + 1, acc ^ nums[i]);  // Pick
    };

    subset(0, 0);
    return total;
};
