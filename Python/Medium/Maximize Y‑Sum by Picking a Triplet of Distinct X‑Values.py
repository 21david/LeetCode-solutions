class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        N = len(x)
        maxes = {}
        for i in range(N):
            if x[i] in maxes:
                maxes[x[i]] = max(maxes[x[i]], y[i])
            else:
                maxes[x[i]] = y[i]

        if len(maxes) < 3:
            return -1

        return sum(sorted(maxes.values(), reverse=True)[:3])
