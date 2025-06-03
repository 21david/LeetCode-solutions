//  https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    public TreeNode bstToGst(TreeNode root) {
        
        ArrayList<Integer> inOrder = new ArrayList<>();
        
        // traverse in-order, and put the values in the ArrayList
        inOrderTraversal(root, inOrder);
        
     //   System.out.println(inOrder);
        
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // find the sums for each value.
        // map the value to the corresponding sum in 'map'
        int sum = 0;
        for(int i = inOrder.size() - 1; i >= 0; i--) {
            sum += inOrder.get(i);
            
            map.put(inOrder.get(i), sum);
        }
        
      //  System.out.println(map);
        
        // relace all vals in the tree with the corresponsing sum
        replaceValues(root, map);
        
        // return the finished tree
        return root;
    }
    
        
    /*
    Traverse the BST in an in-order style, and add the elements to inOrder
    as they are visited. So we should have a sorted list in inOrder at the end.
    
    in order: L P R
    */
    public void inOrderTraversal(TreeNode root, ArrayList<Integer> inOrder) {
        if(root == null)
            return;
        
        inOrderTraversal(root.left, inOrder);
        inOrder.add(root.val);
        inOrderTraversal(root.right, inOrder);
    }
    
    
    /*
    Traverse the tree, replacing each node value with its corersponding value in the map.
    */
    public void replaceValues(TreeNode root, HashMap<Integer, Integer> map) {
        if(root == null)
            return;
        
        root.val = map.get(root.val);
        replaceValues(root.left, map);
        replaceValues(root.right, map);
    }
}

