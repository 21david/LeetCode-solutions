/*
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3348/

June Leetcode challenge, day 2
Finished in ~5 minutes
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        if(node == null || node.next == null)
            return;
        
        while(node.next != null)
        {
            node.val = node.next.val;
            
            if(node.next.next == null)
                node.next = null;
            else
                node = node.next;
        }
    }
}
