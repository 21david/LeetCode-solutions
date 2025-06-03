function searchInsert(nums: number[], target: number): number {
    let [lo, hi] = [0, nums.length - 1];
    let mid;

    while (lo <= hi) {
        mid = lo + Math.floor((hi - lo) / 2);

        if (nums[mid] === target)
            return mid;
        else if (nums[mid] < target)
            lo = mid + 1;
        else
            hi = mid - 1;
    }

    return lo;
};
