//  https://leetcode.com/problems/inorder-successor-in-bst/

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
    List<Integer> l = new ArrayList<>();
    boolean found = false;
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        // 3 ms, faster than 19.74%
        // 39.4 mb, less than 88.48%
        // Solved in 13 minutes
        
        /*
        A basic approach:
        Traverse the tree in-order (L P R) and create a list.
        Iterate the list. Once you find the target item, return the next item.
        Return null by default, so if fthe target item is the last item,
        it will exit the loop and return the default value of null.
        
        */
        
        inOrder(root, p);
        
        
        boolean found = false;
        for(int i = 0; i < l.size(); i++) {
            if(found)
                return new TreeNode(l.get(i));
            
            if(l.get(i) == p.val)
                found = true;
        }
        
        return null;
    }
    
    public void inOrder(TreeNode root, TreeNode p) {
        if(root == null)
            return;
        
        
        inOrder(root.left, p);
        l.add(root.val);
        inOrder(root.right, p);
    }
}
