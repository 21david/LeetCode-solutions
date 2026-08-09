# TC = O(max(PlogP, DlogD))
# SC = O(1)
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        # Sort + greedy
        from heapq import heappop_max as pop, heapify_max

        heapify_max(prices)
        heapify_max(discounts)

        final = 0

        # Greedily use up highest discounts on highest prices
        while discounts:
            max_disc = pop(discounts)

            try:
                max_pr = pop(prices)
            except IndexError:
                break
            
            final += (1 - (max_disc / 100)) * max_pr

        # Add leftover prices if all discounts used
        final += sum(prices)
        
        return final
