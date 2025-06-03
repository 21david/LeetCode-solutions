/*
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

May Leetcoding challenge, day 7
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
    public boolean isCousins(TreeNode root, int x, int y) {
        // 1 ms, faster than 32.86%
        // 37.6 mb, less than 7.14%
    
        /*
        We have to find x and y in the tree, so worst runtime complexity
        is O(N).
        
        We can search for both x and y as we traverse the tree, keeping track of the depth. Once we've found both, compare their depths and return either true or false.
        */
        
        int xD = -1;
        int yD = -1;
        
        int xP = -1; // x's parent
        int yP = -1; // y's parent
        
        Stack<TreeNode> stack = new Stack<>();
        Stack<Integer> stackDepths = new Stack<>();
        Stack<Integer> parents = new Stack<>();
        
        stack.push(root);
        stackDepths.push(0);
        parents.push(root.val);
        
        
        TreeNode tempNode;
        int currentDepth;
        int currentParent;
        
        while(xD == -1 || yD == -1) // while at least 1 hasnt been found
        {
            tempNode = stack.pop();
            if(tempNode == null)
            {
                parents.pop();
                stackDepths.pop();
                continue;
            }
            currentDepth = stackDepths.pop();
            currentParent = parents.pop();
            
            stack.push(tempNode.left);
            stack.push(tempNode.right);
            
            stackDepths.push(currentDepth + 1);
            stackDepths.push(currentDepth + 1);
            
            parents.push(tempNode.val);
            parents.push(tempNode.val);
            
            if(tempNode.val == x)
            {
                xP = currentParent;
                xD = currentDepth;
            }
            else if(tempNode.val == y)
            {
                yP = currentParent;
                yD = currentDepth;
            }
        }
        
        return xD == yD && xP != yP;
    }
    
}
