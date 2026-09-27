# TC = O(NlogN) (easy change can make it O(N))
# SC = O(N)
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        N = len(nums)
        
        # pairs of already equal numbers
        already = 0

        # store pairs of unequal numbers, smaller one first always
        diffs = defaultdict(int)

        # process all pairs
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                already += 1
            else:
                diffpair = [nums[i], nums[i+1]]
                diffpair.sort()
                diffs[tuple(diffpair)] += 1

        # To-do: replace with heap for O(N) TC
        top = ( sorted([(tup, ct) for tup, ct in diffs.items()], key=lambda x: -x[1]) )
        
        if not top:
            # if there are no unequal pairs, the array just consists of the same number
            # so 'already' already stores the answer
            return already

        # if not, the pair that appeared the most would lead to the maximum
        return already + top[0][1]
        
