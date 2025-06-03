# https://leetcode.com/problems/word-ladder

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        """
        Brute force:
        We can use a BFS approach to do this, storing a word and its 'distance' from beginWord 
        in the queue. Starting from the first word, find all the words that differ by 1 from it 
        in the array. Remove them, because we will have found the shortest 'distance' from 
        beginWord to this  word, and there is no need to revisit these words. Then, for each word 
        added to the queue, repeat that process. If we reach endWord, we can immediately return the
        'distance' we are from beginWord and stop searching. If we never reach it after considering 
        every word in the array, we return 0.  To determine how many letters are different between 
        two words, we compare each letter and count the amount that are different. Optimization: 
        return 0 if endWord is not in the array to begin with.

        Time complexity: 
        N = number of words in wordList
        M = number of characters in beginWord (which is equal for every other word)
        The search for finding all the neighbors always searches the entire list, and is 
        potentially initiated for every word in the list (plus beginWord). For every word in the 
        list, it uses an O(M) algorithm to determine how many characters are different from the 
        current word. So this part has O(N^2 * M) complexity. N^2 because every word may get 
        compared to all the other words, and each comparison is O(M).
        This could probably be slightly optimized by using a set instead the original array,
        and removing words from the set instead of setting the array element to None.

        Space complexity:
            Input space complexity: 
            O(N * M). N words with M characters each.
            
            Auxiliary space complexity:
            The queue may grow to be almost the size of wordList, so this is O(N), because
            only a pointer to the original string is stored in this queue, along with an integer. 
            A pointer takes up constant space.
            All other variables take up constant space (including enumerate(wordList),
            because that returns an iterator that creates the pairs on the fly). So
            the total auxiliary space complexity is O(N).
            
            Output space complexity:
            O(1) since it is just an integer.
        """
        if endWord not in wordList:
            return 0
        
        # BFS starting with first word
        q = deque([(beginWord, 1)])

        while q:
            word, lvl = q.popleft()

            # Find all 'neighbors'
            for i, other_word in enumerate(wordList):
                if other_word and differ_by_one(word, other_word):
                    if other_word == endWord:
                        return lvl + 1
                    wordList[i] = None
                    q.append((other_word, lvl+1))
            
        # If the queue is empty and endWord was never reached, there is no transformation sequence
        return 0

# Compare two words of equal length, and return True if they differ by only 1 character
def differ_by_one(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
    return count == 1 


"""
Solution 2 (inspired by LeetCode editorial):
A similar BFS approach.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        """
        Do a BFS style traversal through the array. Start with the first word.
        We will find all the words that differ by 1 like this:
        Convert the wordList into a hash set.
        Replace every letter in the current word with every other possible letter
        in the alphabet, and each time, check if that new word is in the set.
        For each word that is different by 1 and found to be in the set, we will
        put it in the BFS queue along with its distance from beginWord, which we
        will store as an integer that increments by 1 from the previous distance.
        When we have tried all possible words with 1 different letter, we remove
        the word from the hash set to avoid infinite loops from the following words.
        If we find the endWord, we return the level it was on and stop searching.
        This will return the minimum 'distance' to the endWord because the BFS 
        processes all 'levels' in order from lowest to greatest, so if the endWord
        is reached, then it's level is guaranteed to be the minimum number of
        transformations needed. If we never find it, we return 0. We can still 
        optimize by checking if endWord is even in the set we create, and return 0 
        immediately if it isn't.

        N = length of wordList
        M = number of characters in beginWord (which is equal for every other word)
        Time complexity:
        I think it is O(N * M^2 + N^2). 
        N * M^2 because the BFS loop may run N times, and within each loop, all M letters are
        isolated, and a new word of length M is created for each of those letters.

        N^2 because the loop may run N times, and almost N total words may be removed from 
        the hash set, which is an O(N) operation in the worst case. Note: Python's hash set
        implementation is known to be very efficient, so this N^2 case is very unlikely.
        
        The best case scenario, however, is O(1), if the BFS finds the endWord right away.

        Space complexity:
            Input space complexity: O(N * M). N words with M characters.

            Auxiliary space complexity: O(N * M). Almost all the words could be stored in the
            queue at once in the worst case.

            Output space complexity: O(1) for the integer that is returned.
        """
        words = set(wordList)
        if endWord not in words:
            return 0

        # BFS
        q = deque([(beginWord, 1)])

        while q:  # O(N)
            word, level = q.popleft()

            # Find 'neighbors'
            for i, c in enumerate(word):  # O(M)
                # Try every word that is different by 1 letter ('neighbor' words)
                for l in 'qwertyuiopasdfghjklzxcvbnm':  # O(1)
                    possible_word = word[:i] + l + word[i+1:]  # O(M)
                    if possible_word in words:  # Found a 'neighbor' word
                        if possible_word == endWord:
                            return level + 1
                        q.append((possible_word, level + 1))
                        words.remove(possible_word)  # Remove so that we don't loop back in the future (O(N) worst case)
        
        return 0
        

