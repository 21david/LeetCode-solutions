class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        negs = []
        curr_sum = 0
        moved_nums = 0

        for num in nums:
            if num < 0:
                heapq.heappush(negs, num)
                
            curr_sum += num

            # if prefix sum went negative, fix it
            while curr_sum < 0:
                curr_sum -= heapq.heappop(negs)
                moved_nums += 1

        return moved_nums

# Solved after skimming editorial
'''
Special test case:

[100,-1,-1,-40,-2,-30,-3,-23,  -71,  -2,-8,-6,-3,-3,   -16,   -1,   -15,15,  125]
goes negative at -71 (curr sum becomes -71) => 
    remove -40, -30, and -23.
    current sum becomes 22

goes negative at -16 (curr sum becomes -16) =>
    remove -8, -6, and -3
    current sum becomes 1

goes negative at -15 => 
    remove -15
    current sum becomes 0

the 125 makes up for the negative nums moved to the end

final answer is 7
'''
