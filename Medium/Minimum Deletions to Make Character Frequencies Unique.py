# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution(object):
    """
    1. Create a dictionary to store the frequencies
    2. Create 2D array, store elements in the index of their frequency
    3. Iterate over the array from right to left. For every inner array with more 
        than 1 character (which represents a 'tie' between two frequencies), move 
        any character to the array on the left (which represents deleting one letter) 
        until there is only 1 character. Keep track of how many times this happens 
        and that is the answer at the end.

    Time complexity:
    O(N) for iterating through the string and building the dictionary
    O(N) for iterating through the dictionary and building the 2D array
    O(N^2) for iterating through the 2D array and calculating the answer in the worst-
    case type of input (if all letters are the same).
    The total worst-case time complexity is O(N^2).

    Space complexity:
    O(N) for the dictionary, as it will store each unique letter in the string along
    with an integer for it's frequency
    O(N) for the 2D array, because it starts as an array with (len(s) + 1) empty arrays,
    Then each unique letter in the dictionary is added to the 2D array.
    O(1) for the variable that stores the final answer, and for other variables like the
    looping variables.

    EXAMPLE:
    "aabbcccddd"

    1. dictionary 
    { a: 2,
      b: 2,
      c: 3,
      d: 3 }

    2. 2D array
    [[], [], [a, b], [c, d], [], [], [], [], [], [], []]
      0   1     2       3     4   5   6   7   8   9   10

    3. Iterating through the array results in 1 letter in index 3 being moved to the
        left, then 2 lettesr in index 2 being moved to the left, then 1 letter in 
        index 1 being moved to the left. 1 + 2 + 1 = 4. 
        So the example string, assuming we delete the rightmost letters, would be:
        "aacccd" which had 4 letters removed from it.
    """

    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1.
        freqs = {}
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1
        
        # 2.
        freqs_arr = [[] for _ in range(len(s) + 1)]
        for c, f in freqs.items():
            freqs_arr[f].append(c)

        # 3.
        total = 0
        for i in range(len(s), 0, -1):
            curr_arr = freqs_arr[i]
            while len(curr_arr) > 1:  # handle ties
                removed = curr_arr.pop() 
                freqs_arr[i-1].append(removed)  # move char to array on the left
                total += 1

        return total
