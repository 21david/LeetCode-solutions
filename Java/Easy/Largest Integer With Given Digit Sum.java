// TC = O(N), we do one iteration n times
// Aux SC = O(N) for sb AND resulting string
// Output SC = O(1) for the final int
class Solution {
    public int largestInteger(int n, int s) {
        StringBuilder sb = new StringBuilder();

        // Greedily fill with 9s or however much is left from s, going from left to right
        while (n >= 1) {
            if (s > 9) {
                sb.append("9");
                s -= 9;
            }
            else {
                sb.append(Integer.toString(s));
                s = 0;
            }

            n--;
        }

        if (s > 0) {
            // We couldn't fit the total in n slots
            return -1;
        }
        
        return Integer.parseInt(sb.toString());
    }
}©leetcode
