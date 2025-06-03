function findMaxAverage(nums: number[], k: number): number {
    // Get the sum of the first k numbers
    let sum = 0;
    let i;
    for (i = 0; i < k; i++)
        sum += nums[i];

    // Iterate through the rest, subtracting the leftmost and 
    // adding the right most, looking for the highest running sum
    let max = sum;
    for (; i < nums.length; i++) {
        sum -= nums[i-k];
        sum += nums[i];
        max = Math.max(max, sum);
    }

    // Divide by k to get the actual average
    return max / k;
};
