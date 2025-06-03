'''
Line sweep approach
Build a data structure that can be scanned from left to right
At each shift interval start, add 1 to it, and subtract 1 at each end.
Scan the data structure from left to right, adding up the amout of shifts
(or adding up the number of intervals currently overlapping, which tells
us how much to shift each letter). Shift each letter by that amount.

We can use an array of the same size as the string, which stores an integer
at each index, which represents the amount of shifting intervals that
started and ended there. If we take the prefix sum of that array, we can
get the number of shifts we need to make at each letter. We can also scan
through the array and keep a running sum.

We also need an array to store the shifted letters which will be turned
into the string to return the final answer.

Shifting can be done in O(1) by just calculating the new letter.

N = number of letters in s
M = number of intervals in shift
TC: O(N + M)
    O(N) to create the line sweep array
    O(N) to create an auxiliary array to store the shifted letters
    O(M) to iterate through the shifts array and build the line sweep array
    O(N) to scan through the line sweep array and perform the shifts.
SC: O(N) for the line sweep array and the shifted letters array
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Build sweep array
        N = len(s)
        sweep = [0] * (N + 1)
        for start, end, direction in shifts:
            if direction:
                # Forward shifting, a -> b, z -> a
                sweep[start] += 1
                sweep[end + 1] -= 1
            else:
                # Backward shifting, b -> a, a -> z
                sweep[start] -= 1
                sweep[end + 1] += 1

        #  Scan sweep array and perform shifts
        ans = []
        net = 0  # Running sum of net shift amount
        for idx, delta in enumerate(sweep[:-1]):
            curr_letter = s[idx]
            net += delta

            # Calculate and perform shift
            new_letter = chr((ord(curr_letter) - 97 + net) % 26 + 97)
            ans.append(new_letter)

        return ''.join(ans)
