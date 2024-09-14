//  https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
        
/*
An O(N^2) solution is easy, we start with index 0 and compare 
with very other number, while keeping a counter variable. Then 
we move on to index 1 and repeat, until we finish all the indices.
This O(N^2) solution results in time limit exceeded though.

Based off of the 2nd hint, 
We can make an array of size 60. We can modulo every number in the input
array by 60, and add 1 to the corresponding index in the other array.
Then, we can use this array to calculate the answer. 
We can multiply all the pairs that add up to 60 in this array. For example
at index 1, there could be an integer of 5, and at index 59, there could
be an integer of 10. (5 * 10 = 50) represents 50 pairs of songs whose 
lenghts add up to a multiple of 60.
Two exceptions: for indices 0 and 30, we would
multiply those numbers by themselves (arr[0] * arr[0] and arr[30]*arr[30]).
This is an O(N) solution.

2 ms, faster than 99.64%
44.5 mb, less than 55.70%
Solved in 29 minutes and 50 seconds (used hints)
*/
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int count = 0;
        
        // Fill up the remainder array in O(N)
        int[] remainderArr = new int[60];
        for(int n : time)
            remainderArr[n % 60]++;
        
        // Use the remainder array to calculate the answer in O(N)
        for(int i = 1; i < 30; i++) {
            count += remainderArr[i] * remainderArr[60-i];
        }
        
        // Consider the two special exceptions at remainderArr[0] and remainderArr[30]
        // These use triangle numbers (1 + 2 + 3 + 4 + ...) or equivalently (n * (n-1) / 2)
        count += ((remainderArr[0] - 1) * remainderArr[0]) / 2;
        count += ((remainderArr[30] - 1) * remainderArr[30]) / 2;
        
        return count;
    }
}

/*
Sample input:
[30,20,150,100,40]
[60,60,60]
*/
