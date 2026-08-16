// TC = O(L + A)
// Aux SC = O(1)
class Solution {
    public int minPenalty(int period, int[] lights, int[] arrivalTime) {
        // Greedily use highest light to minimize penalty
        int max = Arrays.stream(lights).max().getAsInt();
        
        // For each arrival time, calculate the minimum penalty possible
        // Store the highest of those, that is the minimum overall possible penalty
        int ans = 0;
        for (int at : arrivalTime) {
            int r = at % period;
            if (r >= max)  // if it falls outside of max green light time, only option is to wait
                ans = Math.max(ans, period - r);
        }
        
        return ans;
    }
}
