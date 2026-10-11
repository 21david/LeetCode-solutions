class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1
        fibs = [0, 1, 1]
        
        while c < 10**9:
            if sum(fibs[-3:]) == n:
                return True

            a, b, c = b, c, c + b
            
            fibs.append(c)

        return False
