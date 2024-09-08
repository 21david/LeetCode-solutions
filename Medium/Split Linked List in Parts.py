# https://leetcode.com/problems/split-linked-list-in-parts

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
TC: O(N)
SC: O(1)
'''
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Get length of the linked list
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next

        # Edge case where k >= length. All lists will have length 1 or 0.
        if k >= length:
            answer = []
            ptr = head

            # Build a list out of each node
            while ptr:
                next_head = ptr.next
                ptr.next = None
                answer.append(ptr)
                ptr = next_head

            # Add any remaining empty arrays
            for _ in range(k - length):
                answer.append(None)

            return answer

        # Get number of nodes per list, plus remainder
        # remainder has to be distributed evenly across the first lists
        base, remainder = divmod(length, k)
        num_bigger_lists = remainder
        num_smaller_lists = k - remainder

        # Build the linked lists that will have the longer lengths
        answer = []
        ptr = head
        curr_head = head
        for _ in range(num_bigger_lists):
            # Move pointer 'base' positions ahead
            # So that we have the next 'base+1' total elements
            # Which will form our next list
            for _ in range(base):
                ptr = ptr.next

            # Rewire nodes and add to final array
            next_head = ptr.next  # start of the next list
            ptr.next = None  # Cut this list from the rest of the list
            answer.append(curr_head)

            # Get ready for the next list
            curr_head = next_head  
            ptr = curr_head

        # Build the rest of the linked lists
        for _ in range(num_smaller_lists):
            # Move pointer 'base - 1' positions ahead
            # So that we have the next 'base' total elements
            # Which will form our next list
            for _ in range(base - 1):
                ptr = ptr.next

            # Rewire nodes and add to final array
            next_head = ptr.next
            ptr.next = None
            answer.append(curr_head)

            # Get ready for the next list
            curr_head = next_head
            ptr = curr_head

        return answer
