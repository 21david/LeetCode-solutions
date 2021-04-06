//  https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    public boolean isIdealPermutation(int[] A) {
        // Simple O(N^2) solution
        
        if(A.length == 0 || A.length == 1 || A.length == 2)
            return true;
        
        int l = 0, g = 0;
        
        for(int i = 0; i < A.length - 1; i++) {
            for(int j = i + 1; j < A.length; j++) {
                if(A[i] > A[j]) {
                    if(j == i+1)
                        l++;
                    g++;
                }
            }
        }
        return l == g;
    }

}
/*
Sample input:

[3,2,1,0,4] - 3 local, 6 global

[0,1,2,3,5,4] - 1 local, 1 global

[0,1,2,4,3] - 1 local, 1 global

[0,1,3,2] - 1 local, 1 global

[0,2,1] - 1 local, 1 global

[1,0,2] - 1 local, 1 global

[2,1,0,3] - 2 local, 3 global

[2,0,3,1] - 2 local, 3 global

[0,1,2,5,3,4] - 1 local, 2 global

[0,1,2,5,4,3] - 2 local, 3 global

[0,1,2,3,4,5,6,7,8,9] - 0 local, 0 global

[9,8,7,6,5,4,3,2,1,0] - 0 local, many global

[9,0,8,1,7,2,6,3,5,4] - 5 local, many global

[0,9,1,8,2,7,3,6,4,5] - 4 local, 20 global

[0,1,2,3,9,4,5,6,7,8] - 1 local, 5 global

Copy & paste:
[3,2,1,0,4]
[0,1,2,3,5,4]
[0,1,2,4,3]
[0,1,3,2]
[0,2,1]
[1,0,2]
[2,1,0,3]
[2,0,3,1]
[0,2,1,3]
[0,1,2,5,3,4]
[0,1,2,5,4,3]
[0,1,2,3,4,5,6,7,8,9]
[9,8,7,6,5,4,3,2,1,0]
[9,0,8,1,7,2,6,3,5,4]
[0,9,1,8,2,7,3,6,4,5]
[0,1,2,3,9,4,5,6,7,8]

*/
