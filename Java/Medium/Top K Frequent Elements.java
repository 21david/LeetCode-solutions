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


// Better version which uses a simpler priority queue that uses the map's values to compare. Uses less space for the priority queue as well.
// TC = O(NlogN)
// Aux SC = O(N)
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Populate hashmap with counts (frequency of each number)  O(N)
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int n : nums)
            counts.put(n, counts.getOrDefault(n, 0) + 1);

        // Populate priority queue that uses highest frequency as priority   O(NlogN)
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a));  
        pq.addAll(counts.keySet());

        // Get the top k most frequent elements  O(k logN)
        int[] ans = new int[k];
        for (int i = 0; i < k; i++)
            ans[i] = pq.poll();

        return ans;
    }
}
