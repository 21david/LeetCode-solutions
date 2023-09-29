# https://leetcode.com/problems/zigzag-conversion

# 30 ms, beats 83.76%
# 13.46 MB, beats 65.84%

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        rows = []
        for i in range(numRows):
            rows += ['']

        down = True
        row = 0
        for char in s:
            rows[row] += char

            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False

            if down:
                row += 1
            else:
                row -= 1

        ans = ''
        for strg in rows:
            ans += strg

        return ans
