# https://leetcode.com/problems/word-break

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        '''
        Solution inspired from Alvin's DP tutorial video
        attempt to build the input string with all different
        combinations in wordDict. 
        So to do this, find words in wordDict that are a prefix
        (or the same word itself). Then continue searching for
        strings that match the input word. Don't try strings
        that wouldn't continue constructing the input word. If it finds
        a combination that fully constructs the word, then return true.
        This will be a recursive solution that does a recursive
        call using the currently selected words from wordDict
        (a temporary string that is being constructed) along
        with every other word that doesn't break the temporary
        string.
        '''

        self.ans = False

        # memo will store numbers where there is no
        # solution if N characters have already been
        # constructed.
        # Example, if we've constructed "aa" out of
        # of "aaaaaab", we've constructed 2 characters
        # If we already found that adding words to "aa"
        # doesn't lead to an answer, we can memoize it in
        # the set. So if it's in the set, it represents false.
        # If another recursive calls tries it again,
        # it won't recompute.
        def helper(temp, chars, memo=set()):
            if chars in memo:
                return False
            if chars == len(s) or self.ans:
                self.ans = True
                return True

            for word in wordDict:
                if s.find(word, chars) == chars:
                    temp.append(word)
                    helper(temp, chars + len(word))
                    temp.pop()

            memo.add(chars)
            return False
        
        helper([], 0)
        return self.ans
