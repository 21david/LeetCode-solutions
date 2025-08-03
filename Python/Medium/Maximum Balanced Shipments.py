# TC = SC = O(N)
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # Greedily start with the next two elements, and expand until current shipment meets the conditions

        count = 0
        curr = []
        curr_max = -math.inf
        for i in range(len(weight)):
            if len(curr) < 2:
                curr.append(weight[i])
                curr_max = max(curr_max, weight[i])
                continue

            if curr[-1] != curr_max:
                # found shipment that meets condition
                count += 1
                curr = []
                curr_max = -math.inf

            curr.append(weight[i])
            curr_max = max(curr_max, weight[i])

        if curr[-1] != curr_max:
            # for the last set of elements
            count += 1

        return count
