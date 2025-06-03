class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 1. Find dominant elem
        dom = None
        ct = 0

        # Clever technique I saw in another editorial (Boyer-Moore Majority Voting Algorithm)
        for num in nums:
            if not dom:
                dom = num
                ct = 1
            elif num == dom:
                ct += 1
            else:
                ct -= 1
                if ct == 0:
                    dom = None

        # print(dom)

        # 2. Calculate occurrences of it
        N = len(nums)
        occ = nums.count(dom)  # Sub 1 if N is even

        # print(occ)

        # If odd total nums and bare minimum amt of dom elem, its not possible
        # I deduced this just by trying it (Example 3)
        if N & 1 and occ == N // 2 + 1:
            return -1

        # 3. Go through indices from left to right until finding first subarr with dom elem
        ct = 0
        subarr_len = 0
        for i, num in enumerate(nums):
            subarr_len += 1
            if num == dom:
                ct += 1
                if subarr_len // 2 + 1 == ct:
                    # Found a first subarr with 'dom' as the dom element
                    return i
        
        return -1
