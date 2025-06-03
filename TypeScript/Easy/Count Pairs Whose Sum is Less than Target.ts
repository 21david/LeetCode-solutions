// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

// Two pointer, after seeing solutions
// TC: O(N * log N). After the sorting part, it is O(N).
// SC: O(1) (besides the sorting algorithm)
function countPairs(nums: number[], target: number): number {
    nums.sort((a, b) => (a - b));

    let l = 0, r = nums.length - 1;
    let answer = 0;

    while (l < r) {
        if (nums[l] + nums[r] >= target) {
            r--;
        }
        else {
            answer += r - l;
            l++;
        }
    }

    return answer;
};
