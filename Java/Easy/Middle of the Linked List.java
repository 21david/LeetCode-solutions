/*
https://leetcode.com/problems/middle-of-the-linked-list/
*/

// LeetCode 30 day challenge, day 8

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int size = 0;
        
        ListNode temp = head;
        
        // first get the size of the list
        while(temp != null)
        {
            size++;
            temp = temp.next;
        }
        
        // iterate to the middle and return that one
        temp = head;
        for(int i = 0; i < size / 2; i++)
        {
            temp = temp.next;
        }
        
        return temp;
    }
}
