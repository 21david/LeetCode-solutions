'''
https://leetcode.com/problems/find-the-celebrity

After reading editorial, except code:
Logical deduction. With every call, you can eliminate at least
one node. The celebrity is known by everyone and knows no one
therefore:
    If a knows b, a can't be the celebrity
    If a doesn't know b, b can't be the celebrity

In one pass, we can eliminate everyone who is not a celebrity, leaving us
with one person who may or may not be a celebrity. So we check if they
are the celebrity or not with two more passes.
'''
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:
        possible = 0

        for i in range(1, n):
            if knows(possible, i):
                # If current person knows someone, they are NOT the celebrity
                # But that other person may be
                possible = i

        # If we found the celebrity at any point, he would stay stuck in possible
        # because he would know no one. But it's also possible that we just got
        # someone who knew people that we didn't ask about. So we should check if
        # possible is actually the celebrity by checking all his incoming and outgoing
        # edges
        
        return possible if all(
                not knows(possible, i)  # celebrity doesn't know anyone
                and knows(i, possible)  # everyone knows celebrity
                for i in range(n) if i != possible
            ) else -1



        
