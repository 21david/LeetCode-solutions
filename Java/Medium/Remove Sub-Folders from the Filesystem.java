class Solution {
    class Node { 
        public HashMap<String, Node> children;
        public boolean isFolder;

        public Node(boolean isF) {
            children = new HashMap<>();
            isFolder = isF;
        }
    }

    public List<String> removeSubfolders(String[] folderPaths) {
        // Create a tree similar to Tries, where nodes that represent the end of some folder path
        // will be marked. This will tell us that all nodes under it are sub folders and we can
        // skip and even delete them while building the tree.

        Node root = new Node(false);

        folderPaths:
        for (String folderPath : folderPaths) {
            String[] names = folderPath.substring(1).split("/");

            Node curr = root;

            for (String name : names) {
                if (curr.isFolder) continue folderPaths;  // current path is a subfolder

                // add name as child to children map in the current Node
                if (!curr.children.containsKey(name))
                    curr.children.put(name, new Node(false));
                curr = curr.children.get(name);
            }

            // Set the last node as a folder
            curr.isFolder = true;

            // Delete any sub folders since they won't be needed
            curr.children = new HashMap<>();
        }

        List<String> answer = new ArrayList<>();

        names.push("");
        dfs(answer, root, null);

        return answer;
    }

    private Stack<String> names = new Stack<>();

    private void dfs(List<String> answer, Node currNode, String name) {
        if (currNode.isFolder) {
            // If its a folder, we can add to the answer and skip all sub folders
            answer.add(String.join("/", names)); 
            return;
        }

        // Iterate through children
        for (Map.Entry<String, Node> child : currNode.children.entrySet()) {
            String childName = child.getKey();
            names.push(childName);
            dfs(answer, child.getValue(), childName);
            names.pop();
        }
    }
}
