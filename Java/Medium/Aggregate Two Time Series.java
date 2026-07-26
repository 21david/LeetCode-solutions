// TC = O(N + M)
// Aux SC = O(1)
// Output SC = O(N + M)
class Solution {
    public List<List<Integer>> aggregateTimeSeries(int[][] series1, int[][] series2) {
        int a = 0, b = 0;
        int A = series1.length, B = series2.length;

        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        while (a < A || b < B) {
            // Set defaults for these. MAX_VALUE so that when one reaches the end, others will
            // correctly be compared as lower values.
            // 0 because if there's no timestamp to the right, default value is 0
            int at = Integer.MAX_VALUE, bt = Integer.MAX_VALUE;
            int av = 0, bv = 0;

            // Assign actual values only if in-bounds, otherwise default values remain.
            if (a < A) {
                at = series1[a][0];
                av = series1[a][1];
            }
            if (b < B) {
                bt = series2[b][0];
                bv = series2[b][1];
            }

            // Two pointer check. Use the smaller timestamp as the final timestamp for the final sum
            // and the next timestamp of the other series to get the right value for the sum
            if (at < bt) {
                ans.add(Arrays.asList(at, av + bv));
                a++;
            }
            else if (bt < at) {
                ans.add(Arrays.asList(bt, bv + av));
                b++;
            }
            else {
                ans.add(Arrays.asList(at, av + bv));
                a++;
                b++;
            }
        }

        return ans;
    }
}
