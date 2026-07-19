/*
From a simple observation, I can see that a horse always goes from a white to a black square or vice versa
in one move. So in an even number of moves, it always ends up on the same color.
So We can basically check the color of the starting square and ending square and check if they are the same.
Black squares are ones where the indices add to an even number, and white ones are ones where they add
to an odd number.
TC = SC = O(1)
*/
class Solution {
    public boolean canReach(int[] start, int[] target) {
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2);
    }
}©leetcode
