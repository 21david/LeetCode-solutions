'''
After seeing https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/5972947/clean-code-easy-to-understand-freq-array/?envType=daily-question&envId=2025-05-13

This basically simulates the entire transformations by keeping track
of the frequencies. We iterate through a loop t times. For each iteration,
we do the transformation on all letters by iterating once through a 
26 length array. For each letter, we just push its frequency into the next
position. The zs become the equivalent amount of as and bs.
Then we sum all the frequencies after all transformations, and mod it.

TC = O(S + 26 * T) = O(S + T) I believe
'''

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7

        freqs = [0] * 26

        # Get frequencies
        for ch in s:
            freqs[ord(ch)-97] += 1

        while t > 0:
            z_count = freqs[-1]  # store to convert to as and bs later
            freqs[-1] = 0

            # for y through a, move their frequencies to the right by 1
            # this is one transformation
            for i in range(24, -1, -1):
                freqs[i+1] = freqs[i]
                freqs[i] = 0

            # Handle zs turning to as and bs
            freqs[0] += z_count
            freqs[1] += z_count

            t -= 1

        return sum(freqs) % mod



# Previous attempt:  611 / 824 testcases passed
# TC: O(S + T^2)
class Solution:
    def lengthAfterTransformations(self, s: str, t_orig: int) -> int:
        mod = 10 ** 9 + 7

        def calcLetter(letter, freq):
            t = t_orig + (ord(letter) - ord('a'))  # offset since algo below only starts from 'a'
            ans = 1

            arr1 = [0, 0]
            arr2 = [1]  # To build pascal's triangle
            delt = 0  # delta
            trs = 1  # number of transformations done
            while (trs := trs + 25) <= t:
                for j in range(delt):
                    arr2.append(arr1[j] + arr1[j+1])
                delt += 1

                i = 0
                while (i+trs <= min((delt-1+trs), t)):
                    ans += arr2[i]
                    ans %= mod  
                    i += 1

                arr2.append(0)
                arr1 = arr2
                arr2 = [1]

            return ans * freq

        # Frequency of each letter
        freqs = Counter(s)

        ans = 0
        for letter, freq in freqs.items():
            ans += calcLetter(letter, freq)
            ans %= mod

        return ans

# One of the hardest i've attempted, spent two total hours on this
