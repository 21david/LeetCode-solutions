# https://leetcode.com/problems/word-break-ii

'''
Solution 1:
Attempt all combinations, keep the ones that equal the input string.
This approach adds words from the wordbank until it builds the
input string.
'''
class Solution(object):
    def wordBreak(self, s, wordDict, temp=None, chars=0, ans=None):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not temp:
            temp = []
            ans = []

        elif chars == len(s):
            print(temp)
            ans.append(' '.join(temp))

        for word in wordDict:
            if s.find(word, chars) == chars:
                temp.append(word)
                self.wordBreak(s, wordDict, temp, chars + len(word), ans)
                temp.pop()
        
        return ans


'''
Solution 2:
This is the same thing as above, but implemented with an inner function instead.
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.ans = []

        def helper(temp, chars):
            if chars == len(s):
                self.ans.append(' '.join(temp))
                return

            for word in wordDict:
                if s.find(word, chars) == chars:
                    temp.append(word)
                    helper(temp, chars + len(word))
                    temp.pop()
        
        helper([], 0)
        return self.ans


'''
Solution 3:
This takes the same overall approach, but it shortens the word
until it reaches an empty string, rather than adding words until
they equal the input string.
Also Memoize call results to prevent recalculation and "prune" the
recursion call tree.
'''
class Solution(object):
    def wordBreak(self, s, wordDict, memo=None):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if memo is None:
            memo = {'': ['']}
        if s in memo:
            return memo[s]
        
        ans = []

        for word in wordDict:
            if s.find(word) == 0:
                suffix = s[len(word):]  # truncate 'word' off of 's'
                res = self.wordBreak(suffix, wordDict, memo)
                for str in res:
                    if str:
                        ans.append( word + ' ' + str)
                    else:
                        ans.append( word )  # for the first word


        memo[s] = ans
        return ans
