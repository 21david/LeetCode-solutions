//  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {/
        // 3 ms, faster than 100%
        // 48.3 mb, less than 29.61%
        // Solved in 2 minutes 36 seconds
        
        int[] multiset = new int[nums.length];
        
        for(int n : nums)
            multiset[n-1]++;
        
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i = 0; i < multiset.length; i++) {
            if(multiset[i] == 0) // then (i+1) did not appear in the input array
                answer.add(i+1);
        }
        
        return answer;
    }
}
