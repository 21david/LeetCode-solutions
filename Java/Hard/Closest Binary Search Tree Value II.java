// TC = O((N+K)logN), NlogN for traversing the tree and adding to PQ, and KlogN to pop K closest values from PQ
//      can also be written as NlogN since K is capped at N.
// Aux SC = O(N), for the PriorityQueue and the Stack
// Output SC = O(K) for the K closest values
class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        // PriorityQueue that orders based on distance to target. Closest ones = highest priorities
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {
            double distA = Math.abs(a - target);
            double distB = Math.abs(b - target);
            // -# if a has more priority (closer to target), 0 if equal, +# if b has more priority
            if (distA < distB) return -1;
            else return 1;
        });

        // DFS through tree, adding all values to the priority queue
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node == null) continue;

            pq.offer(node.val);

            stack.push(node.left);
            stack.push(node.right);
        }

        // Get the K closest values
        ArrayList<Integer> answer = new ArrayList<>();
        while (k-- > 0)
            answer.add(pq.poll());

        return answer;
    }
}

// Possible optimization: PriorityQueue only needs to be size K at the most

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
