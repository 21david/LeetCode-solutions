// TC = O(max(PlogP,DlogD))
// Aux SC = O(max(P, D))
class Solution {
    public double minPrice(int[] prices, int[] discounts) {
        // Max heap priority queue for both arrays
        PriorityQueue<Integer> ppq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < prices.length; i++)
            ppq.add(prices[i]);
            
        PriorityQueue<Integer> dpq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < discounts.length; i++)
            dpq.add(discounts[i]);

        double finalSum = 0;

        // Greedily apply highest discounts to highest prices
        while (dpq.size() > 0) {
            double percentToPay = 1 - dpq.poll() / 100.0;

            if (ppq.size() > 0) {
                int aPrice = ppq.poll();
                finalSum += aPrice * percentToPay;
            } 
            else 
                break;
        }

        // Add any leftover prices if all discounts were used
        finalSum += ppq.stream().mapToLong(Integer::longValue).sum();

        return finalSum;
    }
}

/*
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        # Sort + greedy
        from heapq import heappop_max as pop, heapify_max

        heapify_max(prices)
        heapify_max(discounts)

        final = 0
        
        while discounts:
            max_disc = pop(discounts)

            try:
                max_pr = pop(prices)
            except IndexError:
                break
            
            final += (1 - (max_disc / 100)) * max_pr

        while prices:
            final += pop(prices)
        
        return final
*/
