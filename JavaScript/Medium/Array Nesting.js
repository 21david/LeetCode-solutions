/*  
All the numbers form groups. If you pick any number of a group,
it cycles through the same numbers of its group infintely.
So we must find the biggest group.

We can pick any index and visit every number in it's group.
Groups can be of size 1. We keep track of how many is in each group,
and we mark each element as visited the first time we visit it,
to prevent visiting it again in the future.

This should process each element once and find the biggest cycle/group.

Alternatively, we can modify the input array. We mark each visited element
as null to mark it as visited.

TC = O(N)
SC = O(1) (modifies the input array)
*/
const arrayNesting = function(nums) {
    let max = 0;
    let group, j;
    for (let i = 0; i < nums.length; i++) {
        // Explore the current group if it hasn't been explored
        group = 0;
        j = i;
        while (nums[j] !== null) {
            [nums[j], j] = [null, nums[j]];
            group++;
        }

        max = Math.max(max, group);
    }

    return max;
};
