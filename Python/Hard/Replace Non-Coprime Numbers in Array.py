class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        stack = [nums[0]]

        for num in nums[1:]:
            if gcd(num, stack[-1]) > 1:
                lcm_res = lcm(stack.pop(), num)
                while stack and gcd(lcm_res, stack[-1]) > 1:
                    lcm_res = lcm(stack.pop(), lcm_res)
                stack.append(lcm_res)
            else:
                stack.append(num)

        return stack

# Solved on my own after seeing solution posts and reading hints
