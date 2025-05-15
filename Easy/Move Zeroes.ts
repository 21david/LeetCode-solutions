/**
 Do not return anything, modify nums in-place instead.
 */
/*  
Similar to lomuto's partitioning from quick sort, and Dutch National Flag problem.
TC: O(N)
SC: O(1)
*/
function moveZeroes(nums: number[]): void {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
        if (nums[j]) {
            if (j === i) {
                // This non-zero is already in place, no swapping needed
                i++; 
                continue;
            }
            // Else, there is at least one zero before nums[j]
            nums[i++] = nums[j];
            nums[j] = 0;
        }
    }
};
