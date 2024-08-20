//  https://leetcode.com/problems/combination-sum-iv/

class Solution {
    public int combinationSum4(int[] nums, int target) {
        /*
        Brute force solution would be to visit each element in the array,
        pass in target - (the current element)
        then recursively call each element again, until all possible combinations are tested.
        If we find that target - (the current element) is ever 0, then we found a combination
        and we can keep track of how many we found with a global counter variable.
        This solution would be O(N^N). I doubt this will pass the time limit.
        
        If we memoize this solution, it performs much better.
        */
        
        int r = 0;
        
        r = recursiveSol(nums, target); 
        
        return r;
    }
    
    // This will store different values for 'target' as the key
    // and the number of combinations that add up to that value
    // as the value. This prevents redundant recursive calls
    // and lets us effectively use recursion (dynamic programming).
    HashMap<Integer, Integer> memoization = new HashMap<>();
    
    public int recursiveSol(int[] nums, int target) {
        if(target == 0)
            return 1;
        
        if(memoization.containsKey(target))
            return memoization.get(target);
        
        
        int result = 0;
        for(int i = 0; i < nums.length; i++) {
            // passing in the array, the current position, and target - (the current element)
            if(target - nums[i] >= 0)
                result += recursiveSol(nums, target - nums[i]);  
        }
        
        memoization.put(target, result);
        return result;
    }
}

/*
Sample input:
[1,2,3]
4
[1,2,3,4,5]
9
[5]
10

*/
