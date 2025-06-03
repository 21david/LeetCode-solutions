// After seeing editorial of version 1
function maximumTripletValue(nums: number[]): number {
    let ans = 0, max_diff = 0, max_num = 0;

    for (let k = 0; k < nums.length; k++) {
        ans = Math.max(ans, max_diff * nums[k]);
        max_diff = Math.max(max_diff, max_num - nums[k]);
        max_num = Math.max(max_num, nums[k]);
    }

    return ans;
};
