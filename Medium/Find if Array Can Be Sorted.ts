/*
https://leetcode.com/problems/find-if-array-can-be-sorted

In one pass, we can compare every element in a group to the maximum
element of the previous group. If any number is less than the previous
maximum, there is no way to sort the array because that number couldn't
be swapped into its place. If we never find such an element, the answer
is true.

Algorithm:
1. Find the max number of the first group
2. For every other group, make sure each number is >= the previous max
    a. Otherwise, return false
3. If we never return false, return true since all numbers in each group are
    less than all numbers in the next group, which is the only requirement
    for the array to be sortable.

TC: O(N) (one pass)
SC: O(1)
*/
function canSortArray(nums: number[]): boolean {
    // 1. Find max number of the first group
    let prevMax: number = nums[0];
    let currGroupBits: number = bitCount(nums[0]);

    let currNumBits: number;
    let i = 1;
    while ((currNumBits = bitCount(nums[i])) === currGroupBits)
        prevMax = Math.max(prevMax, nums[i++]);

    currGroupBits = currNumBits;  // Move on to next group

    // 2. Compare each group's values with the previous max
    let currMax: number = -1;
    for(; i < nums.length; i++) {
        if ((currNumBits = bitCount(nums[i])) === currGroupBits) {
            currMax = Math.max(currMax, nums[i]);
        } else {
            prevMax = currMax;
            currMax = nums[i];
            currGroupBits = currNumBits;
        }
        if (nums[i] < prevMax)
            return false;
    }

    // Return true if we never returned false
    return true;
};

function bitCount(num) {
    if (num === undefined)
        return -1;
    return num.toString(2).split('0').join('').length;
}

