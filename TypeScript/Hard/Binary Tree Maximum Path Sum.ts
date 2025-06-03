/*  
DFS from each node. The DFS starting from a node determines highest path downward on
each side, only considering positive total values (if it's negative, we just use 0). 
We check each DFS result for a new max, since each node could be the root of the
longest path sum.

Tips:
Consider carefully that we aren't ever adding negative path sums.
But consider cases where there are only negative numbers.
And make sure to only recursively bubble up one leg each time,
not the sum of both.

TC = O(N) to visit each node once.
SC = O(N) for the recursive call stack. Worst case is a line-tree.
*/
function maxPathSum(root: TreeNode | null): number {
    let max = -Infinity;

    const dfs = (node: TreeNode): number => {
        if (!node) return 0;

        let left = dfs(node.left);
        let right = dfs(node.right);

        let res = Math.max(0, left) + Math.max(0, right) + node.val
        max = Math.max(max, res)
        return node.val + Math.max(0, left, right);
    }

    dfs(root);
    return max;
};

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
