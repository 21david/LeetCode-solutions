# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        We can use a sliding window technique. We can store the letters as the keys and
        their indices as the values in a hash dictionary. For every new letter, we check
        if it is in the dictionary. If it isn't, we add it and its index to the dictionary.
        If it is, then first we have to check if it the previous index is within our current
        window. If it is, then we have to shorten the window by making it start at the very
        next letter of the old index (to not have a repeated character in our window).
        If it isn't, then we do nothing because it's not a repeating letter in our window. 
        This way, the window always consists of unique characters as it grows, and we can 
        continually keep track of its maximum size in a variable. It will expand and shrink
        as we iterate through the array. At the end, we return the maximum length it had.

        We could also stores the indices of the start and end whenever a new maximum is
        reached or tied if we want to retreive the actual longest substring(s).

        This approach is O(n) time complexity because in one pass through the array, it will 
        find the longest substring with all unique characters. The space complexity is O(N)
        because by the end, every letter will be stored in the dictionary with an index.
        """

        """
        Example 1:
        abcdefghijk

        Example 2:
        abcabcbb

        Example 3:
        aaaaaaaa

        Example 4:
        pwwekpew
        """

        seen = {}
        max_length = 0
        cur_length = 0
        left = 0 # represents the index of the first letter of a substring without repeating characters
        indices = {}

        for i, letter in enumerate(s):
            if letter in seen:
                if seen[letter] >= left:
                    left = seen[letter] + 1
                seen[letter] = i
            else:
                seen[letter] = i

            # Bonus: keep the indices of each longest substring (optional)
            cur_length = i - left + 1
            cur_string = s[left:i+1]
            if cur_length > max_length:
                max_length = cur_length
                indices = {cur_string: [(left, i)]}

            elif cur_length == max_length:
                if cur_string in indices:
                    indices[cur_string].append((left, i))
                else:
                    indices[cur_string] = [(left, i)]

        print(indices)

        return max_length
