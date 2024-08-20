//  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        // 1 ms, faster than 33%
        // 40.2 mb, less than 20.02%
        // Solved in 27 minutes
        
        /*
        I think we could write some recursive function:
        The recursive function takes in an array, finds the center,
        and adds it to the binary tree. (The root of the BST will be
        the center element.) Then, it calls itself recursively twice,
        with the first half of the array and with the second half
        of the array. Then it does the same thing again, finding the
        center of the array and adding to the BST with the normal
        BST logic.
        
        */
        if(head == null)
            return null;
        
        // convert the linkedlist to an array:
        // find the size
        int size = 0;
        ListNode t = head;
        while(t != null) {
            size++;
            t = t.next;
        }
        
        // fil the array
        int[] inputNums = new int[size];
        t = head;
        int i = 0;
        while(t != null) {
            inputNums[i++] = t.val;
            t = t.next;
        }
        
        // run the recursive function
        recursive(inputNums, 0, inputNums.length-1);
        
        // return
        return sol;
    }
    
    TreeNode sol;
    
    public void recursive(int[] array, int start, int end) {
        if(start > end)
            return;
        
        int mid = (start + end) / 2;
        
        if(sol == null)
            sol = new TreeNode(array[mid]);
        else 
            addToBST(sol, array[mid]);
        
        // recursive call with left half of array
        recursive(array, start, mid-1);
        
        // recursive call with right half of array
        recursive(array, mid+1, end);
        
    }
    
    public void addToBST(TreeNode root, int number) {
        if(root == null)
            return;
        
        if(number < root.val) { // if number belongs somewhere to the left of current node
            if(root.left == null) // if there is an open spot
                root.left = new TreeNode(number);  // put it where it belongs
            else
                addToBST(root.left, number);  // keep searching for its spot
        }
        else if(number >= root.val) {   
            if(root.right == null)
                root.right = new TreeNode(number);
            else
                addToBST(root.right, number);
        }
    }
}

/* 
Sample input:
[-10,-3,0,5,9]
[-3,-2,-1,0,1,2,3]
[-5,-4,-3,-2,-1,0,1,2,3,4,5]
[-5,-4,-3,-2,-1,0,1,2,3,4,5, 6]

*/
