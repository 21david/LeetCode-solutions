import java.io.PrintStream;
class Solution {
    public int countMaxOrSubsets(int[] nums) {
        // PrintStream p = System.out;
        for (int num : nums) {
            // p.println(String.format("%3s", Integer.toBinaryString(num)));
            targetOrValue |= num;
        }

        this.nums = nums;
        backtrack(0, 0);
        return count;
    }

    private int[] nums;
    private int count, targetOrValue;

    private void backtrack(int totalOrValue, int i) {
        if (i == nums.length) {
            if (totalOrValue == targetOrValue)
                count++;
            return;
        }

        backtrack(totalOrValue | nums[i], i + 1);
        backtrack(totalOrValue, i + 1);
        
    }
}
