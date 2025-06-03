//  https://leetcode.com/problems/minimum-operations-to-make-array-equal/

// Solved with loop in 11 minutes
// with equation in 20-30 mins?

/*
The formula for finding the answer would be
(n-1) + ((n-1) - 2) + ((n-1) - 4) + ... + 0

which is equal to

(N/2)*(N*2-1)

for 
*/
class Solution {
    public int minOperations(int n) {
        return n % 2 == 0? (int) ((((double)n/2)/2) * (((double)n/2)*2)) : ((n/2+1) * ((n/2+1)-1));
    }
    
    public int minOperationsLongFormula(int n) {
        if(n % 2 == 0) {
            n /= 2;
            
            return fEven(n);
        }
        else {
            n /= 2;
            n++;
            
            return fOdd(n);
        }
    }
    
    public int fEven(int N) {
        return (int) (((double)N/2) * (N*2));
    }
    
    public int fOdd(int N) {
        return N * (N-1);
    }
    
    public int minOperationsLoop(int n) {
        int N = n-1;
        int sum = 0;
        
        while(N > 0) {
            sum += N;
            N -= 2;
        }
        
        return sum;
    }
}

/*
Sample input:
[1,3,5]
for n = 3
(2) = 2

[1,3,5,7]
for n = 4
(3 + 1) = 4

[1,3,5,7,9]
for n = 5
(4 + 2) = 6

[1,3,5,7,9,11]
    for n = 6
    (5 + 3 + 1) = 9
    steps:
    [2,3,5,7,9,10]
    [3,3,5,7,9,9]
    [4,3,5,7,9,8]
    [5,3,5,7,9,7]
    [6,3,5,7,9,6]
    [6,4,5,7,8,6]
    [6,5,5,7,7,6]
    [6,6,5,7,6,6]
    [6,6,6,6,6,6]


for n = 7
(6 + 4 + 2) = 12?

The pattern is: for n = K
(K-1) + ((K-1) - 2) + ((K-1) - 4) + ... + 0


Sample data copy and paste:
3
4
5
6
7
8
9

*/
