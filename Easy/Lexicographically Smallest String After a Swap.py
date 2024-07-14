class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Go through each pair of characters in the string from left to right,
        because the significance of each digit is highest at the left and
        lowest at the right. So, the first swap that we can make starting 
        from the right will be the one that will decrease the value of the
        number the most.
        This is done by iterating through each pair and checking the parity
        of each number in each pair. When we find the first pair that matches
        in parity and where the first number is less than the second number,
        swapping those will give us the answer. If we reach the end of the
        string without finding such a pair, then the answer is the original
        string.
        Time complexity is O(N) because we pass through the array once.
        Auxiliary space complexity is O(N) only because we need to create a
        new string and return it, since strings are immutable in Python.

        Examples:
        4613 -> 4613

        9744 -> 7944

        9875431 -> 9857431
        """

        for i in range(1,len(s)):
            d1 = int(s[i-1])
            d2 = int(s[i])

            if d1 % 2 == d2 % 2 and d1 > d2:
                return s[:i-1] + str(d2) + str(d1) + s[i+1:]

        return s
