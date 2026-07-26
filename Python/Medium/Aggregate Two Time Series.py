# TC = O(N + M)
# Aux SC = O(1)
# Output SC = O(N + M)
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        # Two pointer technique
        a = b = 0
        A, B = len(series1), len(series2)
        ans = []

        while a < A or b < B:
            if a == A:
                at = math.inf
                av = 0
            else:
                at, av = series1[a]

            if b == B:
                bt = math.inf
                bv = 0
            else:
                bt, bv = series2[b]

            if at < bt:
                ans.append([at, av + bv])
                a += 1
            elif bt < at:
                ans.append([bt, bv + av])
                b += 1
            else:
                ans.append([at, av + bv])
                a += 1
                b += 1

        return ans
