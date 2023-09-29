# https://leetcode.com/problems/zigzag-conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        30 ms, beats 83.76%
        13.46 MB, beats 65.84%

        Time complexity is O(N) since it only traverses the string once.
        Space complexity is O(N) since we store each letter of the string
        into a matrix, and also into 'ans' at the end. All other variables     
        (numRows, down, row, char) use up O(1) space.
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

'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        33 ms, beats 73.21%
        13.31 MB, beats 88.43%

        Time complexity is O(N) since it only traverses the string once.
        Space complexity is O(N) since we store each letter of the string
        into a matrix. All other variables (numRows, i, rowIdx, letterIdx) 
        use up O(1) space.
        """
        if numRows == 1 or len(s) <= numRows:
            return s

        # Set up first 'numRows' letters
        rows = []
        for i in range(numRows):
            rows += [s[i]]

        # Go up (numRows-1) times, then down (numRows-1) times, and repeat
        rowIdx = numRows-1 
        letterIdx = numRows
        while letterIdx < len(s):
            for _ in range(numRows-1):  # up
                rowIdx -= 1
                if letterIdx < len(s):
                    rows[rowIdx] += s[letterIdx]
                letterIdx += 1
            for _ in range(numRows-1):  # down
                rowIdx += 1
                if letterIdx < len(s):
                    rows[rowIdx] += s[letterIdx]
                letterIdx += 1

        return ''.join(rows)
'''
