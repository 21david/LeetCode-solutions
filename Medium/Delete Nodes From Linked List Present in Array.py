# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)

        # Remove non-wanted nodes from the beginning of the list
        while head != None and head.val in nums:
            head = head.next

        # Remove the rest
        a = head
        t = head.next

        while t != None:
            found = False
            while t != None and t.val in nums:
                # Remove
                t = t.next
                found = True

            if found:
                a.next = t
            a = t
            if t != None:
                t = t.next

        return head
        
