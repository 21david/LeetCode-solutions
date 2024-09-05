'''
https://leetcode.com/problems/find-missing-observations/submissions/1379453662/?envType=daily-question&envId=2024-09-05
My solution article: 
https://leetcode.com/problems/find-missing-observations/solutions/5739347/o-n-math-approach-with-explanation-and-pictures/?envType=daily-question&envId=2024-09-05
'''

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Find the sum of the missing observations
        # Mathematically, there is only one answer to this
        total_rolls = len(rolls) + n
        sum_of_current_rolls = sum(rolls)
        sum_of_missing = total_rolls * mean - sum_of_current_rolls

        # This number must fall between n and n * 6.
        # If it does, we can split it into n values of 1 through 6.
        # Otherwise, we wouldn't be able to
        if not (n <= sum_of_missing <= n*6):
            return []

        # We need to split sum_of_missing into n dice values
        quotient, remainder = divmod(sum_of_missing, n)
        answer = [quotient] * (n - remainder) + [quotient+1] * remainder

        return answer

'''
Test cases:
[4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5]
4
40
=> 
[6,6,6,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
or
[4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,4,4,4,4,4,5,4,5,4,4,4,4,5,4,5,4,4,4,4,4,4,5,5,4,4]

'''

'''
Thought: If mean is 6, isn't the answer just an array of 6s, only if current rolls are 6s?
Optimization possibility? Same for 1s?
'''
