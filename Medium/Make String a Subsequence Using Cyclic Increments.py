class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            shifted = chr((ord(str1[i]) - 97 + 1) % 26 + 97)
            if str2[j] in (
                str1[i], 
                shifted
            ):
                j += 1
                if j == len(str2):
                    return True

        return False
