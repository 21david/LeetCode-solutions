class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        arr = [(y[i], x[i], i) for i in range(len(x))]
        arr.sort(reverse=True)
        seen = set()

        maxes = {}
        for yv, xv, i in arr:
            if xv in maxes:
                maxes[xv] = max(maxes[xv], yv)
            else:
                maxes[xv] = yv

        helper = [myv for xv, myv in maxes.items()]
        helper.sort(reverse=True)
        
        if len(helper) < 3: 
            return -1
        return sum(helper[:3])
©leetcode
