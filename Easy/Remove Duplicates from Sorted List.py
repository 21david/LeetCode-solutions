# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Solved in 9 minutes

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Edge case for list with 0 or 1 elements
        if not head or not head.next:
            return head

        p1 = head

        while p1 and p1.next:
            p2 = p1.next

            # Traverse all duplicates
            while p2 and p2.val == p1.val:
                p2 = p2.next

            # Remove duplicates
            p1.next = p2
            p1 = p1.next

        return head
            
