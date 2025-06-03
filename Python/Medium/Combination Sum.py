

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = set()

        def helper(target, index, slate):
            if target == 0:
                self.ans.add(tuple(sorted(slate)))
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                slate.append(candidates[i])
                helper(target - candidates[i], i, slate)
                slate.pop()

        helper(target, 0, [])
        return self.ans
        
