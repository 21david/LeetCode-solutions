# TC = O(N)
# SC = O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cons = 1
        two_cons = 0
        chosen = set()
        cons_copy = 0
        ans = 1
        for i in range(len(fruits)):
            if i >= 1 and fruits[i] == fruits[i-1]:
                cons += 1
            else:
                cons_copy = cons
                cons = 1

            if len(chosen) < 2:
                chosen.add(fruits[i])
                two_cons += 1
                ans = max(ans, two_cons)
                continue

            if fruits[i] not in chosen:
                # Found a third number
                chosen = set([fruits[i], fruits[i-1]])
                two_cons = cons_copy + 1
            else:
                two_cons += 1

            ans = max(ans, two_cons)
        

        ans = max(ans, two_cons)

        return ans
"""

2 3 
1 2 

2

0 1 0 1 1 1 0 0 2 0 2  0 0 0 22 2 3 4 4 4 6 0 0 1
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4

0 1 
0 1


"""    
"""  
Keep a count of consecutive repetitions of the current fruit
and a count of the streak of the two chosen fruits
Keep a set with the two current chosen fruits
Always assign a new max streak to a max variable

When a third fruit is found, create a new set with the 
new fruit and the last fruit (check index to the left)
Set the two-fruit streak to the consecutive repetitions value

"""
