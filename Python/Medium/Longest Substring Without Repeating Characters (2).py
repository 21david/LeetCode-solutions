# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        We can use a sliding window technique. Iterate through each letter and add them
        to a set as we go. Have two pointers: the start of the substring/window and the end of it.
        If a letter is already in the set, then we have to remove letters from the start
        of the window until the repeat is removed. If a letter isn't in the set, then
        we just add letters to the end of the window by pushing the end pointer forward.
        The entire time, we have to compare the size of the window with previous any previous
        max length so that by the end, we will have the longest length that the window was.

        This approach is O(N) time complexity because the array is passed at most only one time 
        by each of the two pointers. The space complexity is also O(N) because the set may store
        up to all the letters in the input string (if all letters are unique). It could also be
        described as O(min(N, M)), where N is the length of the string and M is the number of
        unique characters. For example, if the string repeats one letter over and over, the set
        will only ever store that one letter.
        """

        max_length = 0
        start, end = 0, 0
        N = len(s)
        window_letters = set()

        while end < N:
            curr_letter = s[end]
            if curr_letter not in window_letters:
                window_letters.add(curr_letter)
                end += 1
                max_length = max(max_length, end - start)
            else:
                num_remaining_letters = N - start # optimization
                if num_remaining_letters <= max_length: # ^
                    break                               # ^
                window_letters.remove(s[start])
                start += 1

        return max_length
