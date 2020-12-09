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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        // 2 ms, faster than 31.11%
        // 39.9 mb, less than 28.69%
        
        // took 1 hour and 5 minutes total
        
        ArrayList<TreeNode> result = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();
        
        // turn to_delete to a hashset for O(1) lookup time complexity
        for(int n : to_delete)
            set.add(n);
        
        if(!set.contains(root.val))
            result.add(root);
        
        traverse(root, result, set);
        
        // delete the ones marked for deletion
        for(TreeNode r : result) {
            delete(r);
        }
        
        for(int i = result.size()-1; i >= 0; i--) {
            if(result.get(i).val == -1)
                result.remove(i);
        }
        
        return result;
    }
    
    public void traverse(TreeNode root, ArrayList<TreeNode> result, HashSet<Integer> set) {
        if(root == null)
            return;
        
        if(set.contains(root.val)) {
            if(checkLeft(root))
                result.add(root.left);
            if(checkRight(root))
                result.add(root.right);
            root.val = -1;
        }
        
        traverse(root.left, result, set);
        traverse(root.right, result, set);
    }
    
    // delete all nodes that are marked as -1
    public void delete(TreeNode root) {
        if(root == null)
            return;
        
        if(root.left != null && root.left.val == -1)
            root.left = null;
        
        if(root.right != null && root.right.val == -1)
            root.right = null;
        
        delete(root.left);
        delete(root.right);
    }
    
    public boolean checkLeft(TreeNode root) {
        if(root == null)
            return false;
        if(root.left != null)
            return true;
        else
            return false;
    }
    
    public boolean checkRight(TreeNode root) {
        if(root == null)
            return false;
        if(root.right != null)
            return true;
        else
            return false;
    }
}
