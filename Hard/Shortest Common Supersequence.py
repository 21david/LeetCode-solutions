"""
General idea:
Use LCS algorithm to find the longest common subsequence between both strings, as well
as the set of indices for each letter in the LCS for both strings.

Then build the final answer: for each letter in the LCS, put all letters to the left of it 
from both strings into the final answer, then put the letter, then repeat with the next LCS 
letter. This is the SCS because removing any letter would make it invalid. It has exactly 
the letters it needs for both strings to be a subsequence. Note, if there are multiple LCS 
with the same length, any one works.

Example (spaces added for readability):
    x a    b xx c
      a ww b w  c w

LCS = abc
SCS = x a ww b xx w c w

TC: O(N * M)
SC: O(N * M)
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        S1, S2 = len(str1), len(str2)

        # Build DP table to find LCS
        dp = [[0] * (S1+1) for _ in range(S2+1)]
        mv = mc = mr = 0
        for r in range(S2 - 1, -1, -1):
            for c in range(S1 - 1, -1, -1):
                dp[r][c] = (
                    dp[r+1][c+1] + 1 if str1[c] == str2[r]
                    else max(dp[r+1][c], dp[r][c+1])
                )

                if dp[r][c] > mv:
                    mv = dp[r][c]
                    mr, mc = r, c

        # Get the indices of each letter in the LCS
        ids1, ids2 = set([mc]), set([mr])
        mr += 1
        mc += 1
        while dp[mr][mc]:
            while dp[mr+1][mc] == dp[mr][mc]:
                mr += 1
            while dp[mr][mc+1] == dp[mr][mc]:
                mc += 1

            ids1.add(mc)
            ids2.add(mr)

            mr += 1
            mc += 1

        # Build the answer
        ans = []
        s1 = s2 = 0
        while s1 < S1 or s2 < S2:
            while s1 < S1 and s1 not in ids1:
                ans.append(str1[s1])
                s1 += 1
            while s2 < S2 and s2 not in ids2:
                ans.append(str2[s2])
                s2 += 1

            if s1 < S1:
                ans.append(str1[s1])
                s1 += 1
                s2 += 1

        return "".join(ans)
