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
 // TC = O(N)
 // Aux SC = O(logN)
class Solution {
    private int answer;

    public int countDominantNodes(TreeNode root) {
        this.answer = 0;
        dfs(root);
        return this.answer;
    }

    public int dfs(TreeNode node) {
        if (node == null)
            return 1;

        int left = dfs(node.left);
        int right = dfs(node.right);

        if (node.val >= Math.max(left, right))
            this.answer += 1;

        return Collections.max(Arrays.asList(node.val, left, right));
        // return Stream.of(node.val, left, right).mapToInt(Integer::intValue).max().getAsInt();
    }
}
