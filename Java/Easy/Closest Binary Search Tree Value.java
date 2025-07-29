// TC = O(N)
// SC = O(H), H = height of tree
class Solution {
    public int closestValue(TreeNode root, double target) {
        // DFS through tree, searching for the value with the smallest distance
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        double minDist = Double.POSITIVE_INFINITY;
        int answer = 0;

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node == null) continue;

            // Check if current value has smallest distance to target
            double currDist = Math.abs(node.val  - target);
            if (currDist < minDist) {
                minDist = currDist;
                answer = node.val;
            } else if (currDist == minDist && node.val < answer) {
                // "If there are multiple answers, print the smallest."
                answer = node.val;
            }

            stack.push(node.left);
            stack.push(node.right);
        }

        return answer;
    }
}

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
