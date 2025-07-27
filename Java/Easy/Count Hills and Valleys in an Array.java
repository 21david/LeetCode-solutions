/*  
TC = O(N), one pass
SC = O(1), four auxiliary integers
*/
class Solution {
    public int countHillValley(int[] nums) {
        int answer = 0;
        int left = 0, center = 0;
        for (int i = 0; i < nums.length; i++) {
            int right = nums[i];
            if (right != center) {
                if(i >= 2 && left != 0) {  // left != 0 makes sure left has an actual value from nums already
                    if ((left < center && center > right) || (left > center && center < right)) {
                        answer += 1;
                    }
                }
                left = center;
                center = right;
            } else 
                continue;
        }
        return answer;
    }
}
