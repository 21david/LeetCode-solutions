'''
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2024-09-25

Time complexity:
    For each digit in arr1, we put it in a trie. This is O(1) work for each digit.
    For each digit in arr2, we search through the trie. Also O(1) work.
    TC is O(m), where m is the number of total digits across the arrays.
    or O(len(arr1) + len(arr2))

Aux space complexity:
    The trie holds only the digits of arr1, so it is O(len(arr1))

This could be space-optimized by always choosing the array with less total digits.
'''
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        # Determine array with less total digits
        len_arr1 = sum(len(str(num)) for num in arr1)
        len_arr2 = sum(len(str(num)) for num in arr2)

        # Make sure arr1 has the smaller one
        if len_arr2 < len_arr1:
            arr2, arr1 = arr1, arr2

        # Construct trie for arr1 only
        trie_head = {}
        trie_ptr = None
        for num in arr1:
            trie_ptr = trie_head
            for digit in str(num):
                if digit not in trie_ptr:
                    trie_ptr[digit] = {}
                trie_ptr = trie_ptr[digit]

        # Find max prefix length
        max_prefix_len = 0
        for num in arr2:
            trie_ptr = trie_head
            curr_prefix_len = 0
            for digit in str(num):
                if digit in trie_ptr:
                    trie_ptr = trie_ptr[digit]
                    curr_prefix_len += 1
                else:
                    break
            max_prefix_len = max(max_prefix_len, curr_prefix_len)

        return max_prefix_len
