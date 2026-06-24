// TC = O(NlogN)
// Aux SC = O(N)
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Populate hashmap with counts (frequency of each number)  O(N)
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int n : nums)
            counts.put(n, counts.getOrDefault(n, 0) + 1);

        // Populate priority queue that uses highest frequency as priority   O(NlogN) ?
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());  
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            pq.add(entry);
        }

        // Get the top k most frequent elements  O(k logN)
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = pq.poll().getKey();
        }

        return ans;
    }
}
