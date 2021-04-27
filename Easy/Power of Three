//  https://leetcode.com/problems/power-of-three/

class Solution {
    
    // using loops
    public boolean isPowerOfThree(int n) {
        // 10 ms, faster than 100%
        // 38.4 mb, less than 85.29%
        
        int num = 1;
        while(num <= n && num >= 0) {
            if(num == n)
                return true;
            num *= 3;
        }
        
        return false;
    }
    
    // without directly using loops or recursion
    public boolean isPowerOfThree2(int n) {
        // 20 ms, faster than 9.71%
        // 38.4 mb, less than 85.29%
        return Integer.toString(n, 3).replace("0", "").replace("2","0").equals("1");
    }
}

/*
Sample input:
-81
-27
-3
0
1
-2147483648
2147483647
3
27
81
243
45
412

*/
