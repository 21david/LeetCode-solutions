'''
For each spot in the final answer, you want to pick the smallest letter you can
(closest to a). You can only either go forward to any letter in the string, or
pick the last one in the stack.

We should go through each letter from left to right.
The algo should go for the next smallest letter, which is either the letter at
the top of the stack, or the smallest letter to the right.

If the last stack letter is the smallest, pop it and add it to the final answer.
If the next smallest letter is somewhere to the right, we keep adding to the stack
until we reach it.

To know where the next smallest letter to the right is, we can do this:

we can store the count of all letters in a hash map or multi set (array of size 26 with frequencies).
Each time we process a letter, we subtract once from its frequency. This means that the counts
represent all letters to the right.

We assume the smallest letter is 'a'. If the map doesn't have any a's, we push it one
letter at a time until it has that letter. For example, if there are no b's either, we
push it to c, etc. This can be done with a while loop:
    cts = [0, 0, 2, ...]
    while ctIdx < len(cts) and cts[ctIdx] == 0:
        ctIdx += 1  

Once we know what the next smallest letter is, we can use that to decide whether to pop
the stack or keep adding. While the last stack element is smaller than or equal to the
next smallest, we should add it to the answer.
    while stack and stack[-1] <= nextSmallest:
        ans.append(stack.pop())

Solved after reading editorial and debugging solution, after over an hour

TC = O(N)
SC = O(N)
'''
class Solution:
    def robotWithString(self, s: str) -> str:
        cts = [0] * 26
        for c in s:
            cts[ord(c) - 97] += 1

        stack = []
        answer = []
        ctIdx = 0

        for c in s:
            stack.append(c)
            cts[ord(c) - 97] -= 1  # basically mark as processed

            while ctIdx < 26 and cts[ctIdx] == 0:  # If no more of current smallest
                ctIdx += 1    # try the next one
            nextSmallest = chr(ctIdx + 97)

            # Now we know the smallest available letter that we haven't seen.
            # For all the current letters in the stack that are smaller, add those first
            # if none of them are smaller, this won't do anything and the loop will keep 
            # adding until reaching that next smallest letter
            while stack and stack[-1] <= nextSmallest:
                answer.append(stack.pop())

        return ''.join(answer)
            
