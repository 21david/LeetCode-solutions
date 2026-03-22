class Solution:
    # DP and subsets
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        xor = reduce(lambda x, y: x ^ y, nums)
        t2 = target ^ xor  # target2 which is target comb of 1s and 0s to remove

        '''
        Draw a recursion tree to understand this. (No need to trace with variables.)
        Bottom leaves of the tree means one of the possible combinations of picking and not
        picking was selected, and its XOR value has already been calculated. 
        If this XOR value is not the one we need to hit target, then we return infinity,
        otherwise we return 0.
        This way, only the return values of combinations that hit the target will bubble up.
        The return values represent how many numbers were actually selected (because we add 1
        to op1 which picks an element, and don't add to op2 which skips an element).
        So the smallest value that gave us the target accumulated XOR will always bubble up,
        and the root recursive call will pick the smallest possible.
        If it was never possible, the root call will return infinity, so in that case we
        return -1.
        '''
        @cache
        def rec(acc, i):
            if i == n:
                if acc != t2:
                    return math.inf
                else:
                    return 0
                    
            # pick
            op1 = rec(acc ^ nums[i], i + 1) + 1
            
            # skip
            op2 = rec(acc, i + 1)

            return min(op1, op2)

        res = rec(0, 0)
        if res == math.inf:
            return -1
        return res

# SC = O(N) where N = len(nums)
# TC = O(N^2) ?

        
