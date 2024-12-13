'''
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements

1. Put all elements into a doubly linked list, so that each one can access its neighbors
2. Put each node into an array and sort by value
3. From smallest to largest, pick each node and mark its neighbors. Skip marked nodes.
4. Return the sum of all picked nodes.

TC: O(NlogN) for sorting
SC: O(N) for the linked list and array
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Build doubly linked list
        head = Node(nums[0])
        prev = head
        node_arr = [head]
        for i in range(1, len(nums)):
            node = Node(nums[i])
            node.prev = prev
            prev.next = node
            prev = node
            node_arr.append(node)

        # Sort by node values
        node_arr.sort(key = lambda node: node.val)
        
        # Traverse from smallest to largest, marking neighbors, and skipping marked nodes
        answer = 0
        for node in node_arr:
            if node.val is None:
                continue

            answer += node.val

            if node.prev:
                node.prev.val = None
            if node.next:
                node.next.val = None

        return answer
