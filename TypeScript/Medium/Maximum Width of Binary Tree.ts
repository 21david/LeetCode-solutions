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
My better definition:
class TreeNode {
    constructor(
        public val: number = 0,
        public left: TreeNode | null = null,
        public right: TreeNode | null = null,
    ) {}
}
*/

function widthOfBinaryTree(root: TreeNode | null): number {
    let ans = 0;

    // BFS
    let queue = new Queue<[TreeNode, bigint]>();
    queue.push([root, 0n]);

    let curr: TreeNode;
    let currQueueNodes: number;
    // Use bigint because the indices multiply by 2 each level.
    // Since there can be 3000 nodes, there can be 3000 levels, so
    // pos can become 2^3000.
    let pos: bigint;
    let firstIdx: bigint;
    let lastIdx: bigint;
    while (!queue.isEmpty()) {
        // Process exactly the current layer
        currQueueNodes = queue.size();
        for (let i = 0; i < currQueueNodes; i++) {
            [curr, pos] = queue.pop();

            if (i === 0) firstIdx = pos;
            if (i === currQueueNodes - 1) lastIdx = pos;

            // Add neighbors
            if (curr.left)
                queue.push([curr.left, 2n * pos]);
            if (curr.right)
                queue.push([curr.right, 2n * pos + 1n]);
        }

        ans = Math.max(ans, Number(lastIdx - firstIdx + 1n))
    }

    return ans;
};

// Solved after seeing previous solutions
