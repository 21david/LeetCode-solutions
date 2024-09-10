"""
https://leetcode.com/problems/diagonal-traverse-ii/

We can do a BFS starting with the top-left element. The BFS will go through each 
diagonal one at a time, from its bottom to its top-right. This is like a level-order 
traversal of a tree. For each diagonal, to prevent duplicates, only for the first 
element, we will add the number below and to the right of it to the queue. For all 
other elements in that diagonal, we will only add the element to the right. This 
prevents two adjacent elements in a diagonal from adding their "children" to the 
queue two times. We process every diagonal like this.

TC: O(N) where N is the number of elements. It visits every element only once, and 
does constant work for each.

Auxiliary SC: O(min(R, C)) where R is the number of rows, C is the number of columns. This is 
because the length of the longest diagonal is at most the smallest of R and C. 
(C being the length of the longest row.)
We only store one diagonal at a time in the queue, and the next diagonal in the 
'next_diag' array.
"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        R = len(nums)
        answer = []

        # Stores tuples - (row, column)
        # It will start with the top-left element, which is the first 'diagonal'
        queue = deque([(0, 0)])

        while queue:
            # We will put the next diagonal in here, and explore it in the next iteration of this loop
            next_diag = []

            # Process the first node in this diagonal, since it will be processed differently
            r, c = queue.popleft()
            answer.append(nums[r][c])

            # Check if there is an element below
            if (r + 1) < R and c < len(nums[r+1]):
                next_diag.append((r+1, c))

            # Check if there is an element to the right
            if (c + 1) < len(nums[r]):
                next_diag.append((r, c+1))
            
            # Process every element after the first one in only the current diagonal
            while queue:
                r, c = queue.popleft()
                answer.append(nums[r][c])

                # Check if there is an element to the right
                if (c + 1) < len(nums[r]):
                    next_diag.append((r, c+1))

            # Add the next diagonal back to the queue to process it
            queue.extend(next_diag)

        return answer
