class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            ds = 0
            while num:
                ds += num % 10
                num //= 10
            return ds

        # Comparator for sorting according to requirements
        def cmp(tup1, tup2):
            a, s1 = tup1
            b, s2 = tup2

            if s1 == s2:
                return a - b
            else:
                return s1 - s2

        where1 = { nums[i]:i for i in range(len(nums)) }
        where2 = { i:nums[i] for i in range(len(nums)) }

        # Add sums for sorting
        # Doing this before sorting is important, because if the digit sums
        # are calculated during sorting (in the cmp function), it gives TLE
        # since it does it O(NlogN) times instead of O(N) times I believe
        nums = [ (num, digit_sum(num)) for num in nums ]
        nums.sort(key = cmp_to_key(cmp))

        # Iterate through each cycle
        seen = [False] * len(nums)
        seenNum = 0
        ans = 0
        for i in range(len(nums)):
            if seenNum == len(nums):
                break
            if seen[i]:
                continue
            if nums[i][0] != where2[i]:
                seen[i] = True
                seenNum += 1

                currNum = nums[i][0]
                nextIdx = where1[currNum]
                nextNum = nums[nextIdx][0]

                while not seen[nextIdx]:
                    seen[nextIdx] = True
                    seenNum += 1

                    currNum = nextNum
                    nextIdx = where1[currNum]
                    nextNum = nums[nextIdx][0]

                    ans += 1
            else:
                seen[i] = True
                seenNum += 1

        return ans

# Took almost 2 hours to solve
