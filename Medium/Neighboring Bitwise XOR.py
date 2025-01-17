'''
After seeing NeetCode's solution video except the code

TC: O(N)
SC: O(1)
'''
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        curr_orig = 0

        for i in range(len(derived) - 1):
            curr_derived = derived[i]

            if curr_derived == 1:
                # Numbers in original were different
                curr_orig = 1 - curr_orig
            else:
                # Numbers in original were the same
                pass

        
        if derived[-1] == 1:
            return curr_orig == 1  # 1 ^ 0 == 1
        else:
            return curr_orig == 0
        
    '''
    [1, 1, 0]
    [0, 1, 0]
    '''


# Shortened version
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        curr_orig = 0
        for curr_derived in derived[:-1]:
            curr_orig = abs(curr_derived - curr_orig)
        return curr_orig == (derived[-1] == 1)
