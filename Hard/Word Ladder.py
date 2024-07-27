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
        Output space complexity: O(1) since it is just an integer.
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
