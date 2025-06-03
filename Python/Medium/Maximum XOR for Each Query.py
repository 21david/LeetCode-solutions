# https://leetcode.com/problems/maximum-xor-for-each-query

# TC: O(N)
# Auxiliary SC: O(1)
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = deque()
        target = (1 << maximumBit) - 1
        accumulator = 0
        
        for num in nums:
            accumulator ^= num 
            answer.appendleft(accumulator ^ target)

        return list(answer)
