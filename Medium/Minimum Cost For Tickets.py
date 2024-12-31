"""
After watching NeetCode's solution video
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Top down dynamic programming solution:
        For each index i, this function will find the cheapest combination to travel all days.

        Since it's recursive and starts at 0, it will first travel down the tree in DFS manner, 
        then it will determine the cheapest option starting at the last index, memoize, 
        backtrack, and repeat for the second last index, this time potentially using the 
        memoized results. As it goes backwards and finds the cheapest option for smaller indices, 
        the memoized results increase. At index 0, it is able to use all memoized results to 
        get the answer quickly.

        TC: O(N)
        SC: O(N)

        Written after seeing NeetCode's code.
        """
        D = len(days)
        @cache
        def find_cheapest(idx):
            if idx == D:
                # Base case: $0 if we passed the last day
                return 0

            res = math.inf
            j = idx + 1
            for cost, dur in zip(costs, [1, 7, 30]):
                while j < D and days[j] < days[idx] + dur:
                    j += 1
                res = min(res, cost + find_cheapest(j))

            return res

        return find_cheapest(0)
