/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
/* 
After seeing editorial of 1123. Lowest Common Ancestor of Deepest Leaves:
Recursive solution with dfs. Always bubble up the max depth and LCA with each return.
For the dfs call of a node, 
If left subtree has greater depth, use the LCA that was bubbled up.
Same for right subtree.
If depths of left and right are equal, current node is LCA, so return that.
Base case: a null has a depth of 0 and  no LCA.

TC: O(N) each node visited once
SC: O(N) call stack reaches height of tree.
 */
type Node = TreeNode | null;
type DFS = (Node) => [number, Node];  // [depth, LCA node]
function subtreeWithAllDeepest(root: Node): Node {
    const dfs: DFS = (node) => {
        if (!node)
            return [0, null];
        
        let [left_depth, left_lca, right_depth, right_lca] = [...dfs(node.left), ...dfs(node.right)];

        if (left_depth > right_depth)
            return [left_depth + 1, left_lca];
        else if (right_depth > left_depth)
            return [right_depth + 1, right_lca];
        else
            return [left_depth + 1, node];
    }

    return dfs(root)[1];
};
