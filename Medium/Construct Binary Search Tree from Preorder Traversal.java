/*
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

LeetCode 30 Day Challenge, day 20
*/

/*
Inorder: Left, Root, Right (L P R)
Preorder: Root, Left, Right (P L R)
Postorder: Left, Right, Root (L R P)
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode bstFromPreorder(int[] input) {
        if (input.length == 0)
            return null;

        TreeNode root = new TreeNode(input[0]);

        for (int i = 1; i < input.length; i++) {
            addNumber(root, input[i]);
        }

        return root;
    }

    public void addNumber(TreeNode root, int num) {
        if (root != null) {
            if (num <= root.val) {
                if (root.left != null)
                    addNumber(root.left, num);
                else
                    root.left = new TreeNode(num);
            } else {
                if (root.right != null)
                    addNumber(root.right, num);
                else
                    root.right = new TreeNode(num);
            }
        }
    }
      
      /* Another recursive version of 'addNumber()':
          public void addToBST(TreeNode root, int num) {
            
            if(root.left == null && root.right == null) {
                if(num < root.val)
                    root.left = new TreeNode(num);
                else
                    root.right = new TreeNode(num);
                
                return;
            }
            
            
            if(num < root.val) {
                if(root.left == null)
                    root.left = new TreeNode(num);
                else
                    addToBST(root.left, num);
            }
            else {
                if(root.right == null)
                    root.right = new TreeNode(num);
                else
                    addToBST(root.right, num);
            }
    
        }
    */
}
