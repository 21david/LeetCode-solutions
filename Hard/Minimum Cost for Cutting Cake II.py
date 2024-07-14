# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii
# This is the same as "Minimum Cost for Cutting Cake I" but with bigger input sizes

class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        """
        Sort vertical and horizontal cuts descending.
        Pick the biggest one and make a cut.
        Track vertical and horizontal cuts in variables.
        Pick the next biggest one, and make a cut. The cost is calculated
        as the product of (# cuts of opposite direction + 1) * (current cost).
        Add that cost to a grand sum variable.
        Repeat until all done and return the sum of all costs.
        """
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        moreVerticals = len(verticalCut) > len(horizontalCut)
    
        hc = 0  # tally of horizontal cuts
        vc = 0  # tally of vertical cuts

        h = 0   # pointer for horizontalCut array
        v = 0   # pointer for verticalCut array

        sum = 0

        while h < len(horizontalCut) and v < len(verticalCut):
            if horizontalCut[h] > verticalCut[v] or (horizontalCut[h] == verticalCut[v] and not moreVerticals):
                # Horizontal cut
                sum += (vc+1) * horizontalCut[h]
                h += 1
                hc += 1
            elif horizontalCut[h] < verticalCut[v] or (horizontalCut[h] == verticalCut[v] and moreVerticals):
                # Vertical cut
                sum += (hc+1) * verticalCut[v]
                v += 1
                vc += 1
                    
        # Leftovers, similar to merge sort leftovers
        while h < len(horizontalCut):
            # Horizontal cut
            sum += (vc+1) * horizontalCut[h]
            h += 1
        
        while v < len(verticalCut):
            # Vertical cut
            sum += (hc+1) * verticalCut[v]
            v += 1

        return sum
        
