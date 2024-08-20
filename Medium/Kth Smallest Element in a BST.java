/*
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/

May Leetcoding challenge, day 20
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
    public int kthSmallest(TreeNode root, int k) {
        
        // 1 ms, faster than 38.42%
        // 40.2 mb, less than 5.51%
        
        /*
        Approach:
        Do an In-order traversal on the tree
        Store the elements in an ArrayList as you go
        Then, the kth smallest element should be the kth element from the left of the array (from the beginning of the array). Return that element.
        
        Time complexity: O(N), where N is the amount of elements in the tree
        - Tree traversal is O(N), and adding an element to the end of an ArrayList is O(1), so O(N) to create the ArrayList
        - retreiving kth smallest element from the ArrayList is O(1)
        Space complexity: O(N)
        - we create an ArrayList that stores every element in the tree again
        */
        
        ArrayList<Integer> inOrder = new ArrayList<>();
        
        fill(inOrder, root);  // fill with elements of the tree, with an in-order traversal
        
        return inOrder.get(k - 1);
    }
    
    public void fill(ArrayList<Integer> list, TreeNode root)
    {
        if(root == null)
            return;
        
        fill(list, root.left);
        
        list.add(root.val);
        
        fill(list, root.right);
    }
}
