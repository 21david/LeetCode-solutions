# https://leetcode.com/problems/find-if-digit-game-can-be-won

class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        Find the sum of both groups of numbers (numbers less than 10 and numbers
        greater than 10). If they are equal, it would result in a tie, so return
        false. If they are different, then Alice can pick the bigger group and
        win, so return True.
        """
        sum1 = sum([x for x in nums if x < 10])
        sum2 = sum([x for x in nums if x >= 10])
        return sum1 != sum2


# One line solution:
def canAliceWin2(self, nums):
    return sum([x for x in nums if x < 10]) != sum([x for x in nums if x >= 10])
        
