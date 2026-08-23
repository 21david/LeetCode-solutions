class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:

        N = len(nums)

        def get_prime_factors(n):
            prime_factors = []
            while n % 2 == 0:
                prime_factors.append(2)
                n //= 2
            i = 3
            root_n = sqrt(n)
            while i <= root_n:
                while n % i == 0:
                    prime_factors.append(i)
                    n //= i
                i += 2
            if n > 2:
                prime_factors.append(n)
        
            return prime_factors

        pfs = [None] * N

        for i, num in enumerate(nums):
            cpfs = set(get_prime_factors(num))
            pfs[i] = cpfs

        # Greedy sliding window
        curdict = defaultdict(int)
        l = 0
        ans = 0
        
        for r in range(N):
            for cpf in pfs[r]:
                curdict[cpf] += 1
                
            if len(curdict) <= k:
                ans = max(ans, r - l + 1)
            else:
                while len(curdict) > k:
                    # remove one of each from position l
                    for cpf in pfs[l]:
                        curdict[cpf] -= 1
                        if curdict[cpf] == 0:
                            del curdict[cpf]
                    l += 1

        return ans
