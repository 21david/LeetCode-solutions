'''
https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it

Monotonic stacks
left to right and right to left
then use a forumla, ltr[i] - rtl[i] - 1, to get ans
'''
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        N = len(nums)

        def next_greater_array(arr, val):
            res = [val] * len(arr)
            st = []
            for i in range(len(arr)):
                while st and arr[i] > arr[st[-1]]:
                    # Current num maybe bigger than many, so update all those indices
                    res[st.pop()] = i
                st.append(i)
            return res

        ltr = next_greater_array(nums, N)

        rtl = list(reversed(next_greater_array(nums[::-1], -1)))
        rtl = [(N-1) - rtl[i] if rtl[i] >= 0 else -1 for i in range(N)]

        return [ltr[i] - rtl[i] - 1 for i in range(N)]
