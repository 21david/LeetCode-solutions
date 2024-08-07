

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
 /*
    BFS solution. This solution goes through each level one by one. For each level, it
    records the position of the left-most node and the right-most node. Then, it 
    calculates the width of the level by subtracting those, and only records the longest
    width it finds.

    The position of each node is calculated like this:
        - left children get twice their parent's position
        - right children get twice their parent's position plus one

    Time complexity:
    O(N) because we visit every node once.

    Auxiliary space complexity:
    O(H), where H is the height of the tree. level_nodes stores 2 elements for every level,
    and the call stack reaches a size equivalent to the height at its peak.
    If the tree is balanced, we can say the SC is O(logN) because a balanced tree has a height
    of approximately log(base2)N.
    If it is skewed, we can say the SC is O(N) because the height may be linearly proportional
    to the number of nodes.
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        Queue<Object[]> q = new LinkedList<>();
        q.add(new Object[] {root, 0});
        int max_width = 0;

        // BFS
        while (q.size() > 0) {
            // At this point, exactly one entire level is stored in the queue
            // get the length so that we can traverse exactly this amount
            // also get the position of the first node in this level
            // and create a variable that will store the rightmost positions
            // as they are visited, so that the rightmost one is stored in the end
            int level_length = q.size();
            int leftmost = (int) q.peek()[1];
            int rightmost = leftmost;

            // Iterate through the current level
            for(int i = 0; i < level_length; i++) {
                Object[] curr_node_and_pos = q.poll();
                rightmost = (int) curr_node_and_pos[1];
                TreeNode curr_node = (TreeNode) curr_node_and_pos[0];
                int curr_position = (int) curr_node_and_pos[1];

                // Add children if not null
                if (curr_node.left != null)
                    q.add(new Object[] {curr_node.left, 2 * curr_position});

                if (curr_node.right != null)
                    q.add(new Object[] {curr_node.right, 2 * curr_position + 1});
            }

            // calculate width of the level we just traversed, keep it if it is a max
            // and move on to the next level
            max_width = Math.max(max_width, rightmost - leftmost + 1);
        }

        return max_width;
    }
}
