class Solution:
    def permute(self, n: int) -> List[List[int]]:
        def get_permutations(slate, remaining):

            if len(slate) == n:
                ans.append(slate[:])
                return

            for i in range(len(remaining)):
                taken_out = remaining[i]
                if len(slate) >= 1 and (slate[-1] + taken_out) % 2 == 0:
                    continue  # not a valid permutation
                slate.append(taken_out)
                get_permutations(slate, remaining[:i] + remaining[i+1:])
                slate.pop()

        ans = []
        get_permutations([], [num for num in range(1, n + 1)])

        return ans
