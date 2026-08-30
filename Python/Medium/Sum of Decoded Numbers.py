'''
TC is O(N log D)
N = length of nums
D = max length of a num
'''
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9+7
        ans = 0

        for num in nums:
            width = num % 10
            d = num // 10

            string_d = str(d)
            
            x = int(string_d[:width])
            y = int(string_d[width:])

            ans = (ans + pow(x, y, mod)) % mod

        return ans
