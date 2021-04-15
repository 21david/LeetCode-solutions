//  https://leetcode.com/problems/fibonacci-number/

class Solution {
    public int fib(int n) {
        // 0 ms, faster than 100%
        // 35.5 mb, less than 74.08%
        // Solved in 2 minutes 10 seconds
        
        if(n == 0)
            return 0;
        else if(n == 1)
            return 1;
        
        int a = 0;
        int b = 1;
        int c = 0;
        
        for(int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        
        return c;
    }
}
