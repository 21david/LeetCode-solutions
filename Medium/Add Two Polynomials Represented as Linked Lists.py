# https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/description/?envType=weekly-question&envId=2024-09-01

# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

'''
Two pointer approach. This approach creates a new linked list without modifying
or reusing the input lists.

More optimal approaches could be written if the input can be reused or rewritten.
For example, we could use one of the input nodes, rewrite it, and return that
list, which would minimize the total space used.

M is the length of one linked list, N is the length of the other one
TC: O(M + N) to traverse both lists
Auxiliary SC: O(1) for the pointers and sum variable
'''
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        # Create new linked list to store the answer, with 1 dummy node
        # to make the insertions easier
        answer = PolyNode()
        ans_ptr = answer

        # Maintain two pointers and traverse the lists at the same time
        p1 = poly1
        p2 = poly2
        while p1 and p2:
            # If the terms have the same power, we can sum them and add it
            # to our answer linked list
            if p1.power == p2.power:
                sum = p1.coefficient + p2.coefficient
                if sum == 0:
                    # But if they sum to 0, we must not add it to the linked list
                    p1 = p1.next
                    p2 = p2.next
                    continue

                sum_node = PolyNode(sum, p1.power)
                ans_ptr.next = sum_node
                ans_ptr = sum_node
                p1 = p1.next
                p2 = p2.next

            # If one term is greater than the other, we just add it to our answer
            # and move to the next term in that list
            elif p1.power > p2.power:
                curr_node = PolyNode(p1.coefficient, p1.power)
                ans_ptr.next = curr_node
                ans_ptr = curr_node
                p1 = p1.next
            
            else:
                curr_node = PolyNode(p2.coefficient, p2.power)
                ans_ptr.next = curr_node
                ans_ptr = curr_node
                p2 = p2.next

        # Once at least one of them is done, the other one may still have nodes
        # which can just be added to the answer
        while p1:
            curr_node = PolyNode(p1.coefficient, p1.power)
            ans_ptr.next = curr_node
            ans_ptr = curr_node
            p1 = p1.next

        while p2:
            curr_node = PolyNode(p2.coefficient, p2.power)
            ans_ptr.next = curr_node
            ans_ptr = curr_node
            p2 = p2.next

        # Remove the dummy node from the final answer
        return answer.next

        
