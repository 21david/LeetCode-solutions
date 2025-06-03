//  https://leetcode.com/problems/n-ary-tree-preorder-traversal/

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    List<Integer> result = new ArrayList<>();
    public List<Integer> preorder(Node root) {
        // 0 ms, faster than 100%
        // 39.3 mb, less than 88.50%
        // Solved in 7 minutes 30 seconds
        
        /*
        Preorder traversal is [P] [L] [R], or in the case of an N-ary tree,
        [Parent] [Children from left to right] 
        So we can write a recursive function that visits the parent (adds it to the list)
        first, then, recursively, visits children from left to right (adds them to the list).
        
        Time complexity: O(N) (N is the number of nodes)
        Space complexity: O(N)
        
        */
        preorderHelp(root);
        return result;
    }
    
    public void preorderHelp(Node root) {
        if(root == null)
            return;
        
        result.add(root.val);
        
        if(root.children == null)  // for leaves (nodes w/no children), do nothing
            return;
        
        // visit the children
        for(Node child : root.children) {
            preorderHelp(child);
        }
    }
}

/*
Sample inputs:
[]
[1,null,3,2,4,null,5,6]
[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

*/
