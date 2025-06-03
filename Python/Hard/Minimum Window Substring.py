'''
https://leetcode.com/problems/minimum-window-substring/

Sliding Window like in 567. Permutation in String
~2 hours to solve, after solving 567
TC: O(T + S) (or O(N + M)). String t is iterated once to get a count of its chars. String S is iterated
    at most once by either r or l (So about twice in total in the worst case.) Each iteration
    does constant work. At the end, creating the answer string is O(M) in the worst case.
Aux SC: O(T) (or O(N)). Window only accepts chars in T, so it will never exceed size of T. 
    t_counter only has chars in t and their counts.
Output SC: O(S) (or O(M)). The entire string might be the answer.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        S = len(s)
        min_l, min_r = -1, S 
        chars_satisfied = 0  # a char is satisfied if the window has at least as many as there are in t
        
        window = {}
        l = r = 0

        while r < S:
            new_char = s[r]  # current char / right char
            if new_char in t_counter:
                # Add the new char to the window
                window[new_char] = window.get(new_char, 0) + 1
                if window[new_char] == t_counter[new_char]:  # If we reached the min required amount
                    chars_satisfied += 1
            
                # Minimize the string as much as possible from the left
                left_char = s[l]
                while left_char not in t_counter or window[left_char] > t_counter[left_char]:
                    if left_char in t_counter:
                        window[left_char] -= 1
                    l += 1
                    left_char = s[l]

                if chars_satisfied == len(t_counter):
                    # Found a valid substring, check if it is a smaller window than before
                    if (r - l) < (min_r - min_l):
                        min_l, min_r = l, r

            r += 1

        return '' if min_l == -1 else s[min_l : min_r + 1]
    

'''
Test cases:
"AXYZBAC"
"ABC"
"aabbcdd"
"abcdd"
"aabbcddxxxabcddxxx"
"abcdd"
"ADOBECODEBANC"
"ABC"
"aaaaaaaaaaaabbbbbcdd"
"abcdd"
"a"
"a"
"a"
"aa"
'''
