"""
Article: https://leetcode.com/problems/minimum-time-to-activate-string/solutions/7037905/python-binary-search-onlogn-by-david1121-jvhh/
TC = O(NlogN)
SC = O(N)
"""
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        grand_total_substrings = int((n+1) * (n/2))

        # If k is larger than the number of substrings, it's impossible to reach k
        if k > grand_total_substrings:
            return -1

        def calculate_combinations(n):
            return int((n+1) * (n/2))

        def check(t):  # O(N)
            # Create list version of s with asterisks
            s_prime = list(s)  # s prime
            for i in range(t + 1):
                pos = order[i]
                s_prime[pos] = '*'

            # Calculate the total number of non valid substrings
            non_valid_substrings = 0
            consecutive = 0  # count consecutive letters
            for i in range(0, len(s_prime)):
                if s_prime[i] == '*':
                    # calculate previous streak of consecutive letters
                    non_valid_substrings += calculate_combinations(consecutive)
                    consecutive = 0
                else:
                    consecutive += 1

            # Calculate the last streak of consecutive letters if there was one
            non_valid_substrings += calculate_combinations(consecutive)

            # Substracting number of non valid substrings from the
            # total number of substrings gives us the number of valid substrings
            return grand_total_substrings - non_valid_substrings

        # BINARY SEARCH
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = check(mid)
            if res == k:
                return mid
            elif res >= k:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
