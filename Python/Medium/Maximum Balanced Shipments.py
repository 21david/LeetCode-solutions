# TC = O(N)
# SC = O(1)
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # Greedily start with the next two elements, expand until 
        # current shipment meets the conditions then restart and repeat
        answer = 0
        shipment_length = 0
        curr_max = -math.inf
        for i in range(len(weight)):
            if shipment_length < 2:
                shipment_length += 1
                curr_max = max(curr_max, weight[i])
                continue

            if weight[i-1] != curr_max:
                # found shipment that meets condition
                answer += 1
                curr_max = -math.inf
                shipment_length = 1

            curr_max = max(curr_max, weight[i])

        if weight[-1] != curr_max:
            # for the last set of elements
            answer += 1

        return answer
