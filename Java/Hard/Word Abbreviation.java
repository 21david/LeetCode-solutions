// LC Premium problem
import static java.lang.System.out;
class Solution {
    private class Node {
        char ch;
        short index;
        boolean belongsToOne;  // track if character belongs to only one word
        Node[] children;

        public Node(char c, short i) {
            ch = c;
            belongsToOne = true;
            index = i;
            children = new Node[26];
        }

    }

    private class Trie {
        Node head;

        public Trie() {
            head = new Node('_', (short) -1);
            head.belongsToOne = false;
        }

        // Add a word
        public void add(String word, short index) {
            Node temp = head;
            for (char c : word.toCharArray()) {
                short pos = (short) (c - 'a');
                if (temp.children[pos] != null) {  // Letter already used for another word
                    temp = temp.children[pos];
                    temp.belongsToOne = false;  // False bc if we got here, then it belonged to some previous word
                } else {
                    Node newNode = new Node(c, index);
                    temp.children[pos] = newNode;
                    temp = newNode;
                }
                
            }
        }
    }
    public List<String> wordsAbbreviation(List<String> words) {
        /* 
        1. Create hash map where the keys have the first letter, length, and last letter, like "i9n"
        and the values have a list of all words in that group. Each word (value) will also need to know
        its index in the original list. May use Pair or Map.Entry or custom class 
        */
        HashMap<String, ArrayList<Pair<String, Short>>> groups = new HashMap<>();
        for (short i = 0; i < words.size(); i++) {
            String word = words.get(i);
            short length = (short) word.length();
            char firstLetter = word.charAt(0), lastLetter = word.charAt(length - 1);
            String group = firstLetter + "," + length + "," + lastLetter;

            ArrayList<Pair<String, Short>> groupList;
            if (groups.containsKey(group)) {
                groupList = groups.get(group);

            } else {
                groupList = new ArrayList<>();
                groups.put(group, groupList);
            }

            groupList.add(new Pair<>(word, i));
        }

        /* 
        2. For each group in the hash map (each key-value pair), create a trie with all those words.
        Each node in the trie will have 1) character of the node, 2) index of the word (from original 
        list), 3) count of words that use this letter, and 3) list of children nodes. For 2, for the
        nodes that belon to more than one word, this will just be set to -1. It will be used to 
        determine which index to put the final abbreviation, which is determined as soon as we reach 
        a node with a count of 1.

        3. DFS through the each trie. Add each traversed letter to a temporary ArrayList. As soon as a 
        letter has a count of 1, we can determine the final abbreviation by using the letters in the 
        ArrayList, adding the number of remaining characters (can be calculated), and the last letter,
        and we can set it to the index in the input list using the index stored on the node. 
        */ 

        for (String group : groups.keySet()) {
            ArrayList<Pair<String, Short>> groupList = groups.get(group);
            String[] values = group.split(",");
            short wordLength = Short.parseShort(values[1]);
            char lastLetter = values[2].charAt(0);

            if (groupList.size() == 1) {  // No need to build trie
                String word = groupList.get(0).getKey();
                Short index = groupList.get(0).getValue();
                String finalAbbrv = "" + word.charAt(0) + (wordLength - 2) + lastLetter;
                if (finalAbbrv.length() < wordLength) 
                    words.set(index, finalAbbrv);
                continue;
            } 

            Trie trie = new Trie();

            for (Pair<String, Short> pair : groupList) {
                String word = pair.getKey();
                Short index = pair.getValue();
                trie.add(word, index);
            }


            dfs(words, new ArrayList<Character>(Arrays.asList()), (short) 0, wordLength, lastLetter, trie.head);
        }

        // 4. When done with all groups, we can return the original input list which has been replaced with
        // the abbreviations
        return words;
    }

    // Todo: possibly optimize chars to use stack or linkedlist instead of ArrayList
    private void dfs(List<String> words, ArrayList<Character> chars, short currLength, short wordLength, char lastLetter, Node node) {
        if (node.belongsToOne) {
            // We can for sure know the final abbreviation for this word because all subnodes also only belong to one
            short remainingLength = (short) (wordLength - 1 - currLength);
            StringBuilder finalAbbrv = new StringBuilder();

            for (char ch : chars) 
                finalAbbrv.append(ch);
            finalAbbrv.append("" + remainingLength);
            finalAbbrv.append(lastLetter);

            // Rule 3 is only abbreviate if it becomes shorter
            if (finalAbbrv.length() < wordLength) 
                words.set(node.index, finalAbbrv.toString());
            
            return;  // No need to finish exploring the entire word
        }


        for (byte i = 0; i < 26; i++) {
            if (node.children[i] != null) {
                // Found child, explore it
                chars.add((char) (i + 'a'));
                dfs(words, chars, (short) (currLength + 1), wordLength, lastLetter, node.children[i]);
                chars.remove(chars.size()-1);
            }
        }
    }
}

// Input constraints: 400 * 400 = 160,000 = 1.6 * 10 ^ 5
/*  
Hint used:
My general approach here was to partition the words into groups of the form 
(first_letter, last_letter, length). Then for each group, I created a Trie T 
where the nodes contained the current letter, children letters, and count of 
words that use this node (the number of words in the group that have the shared 
prefix represented by this node). Then, once we add all the words in a group to 
T we can traverse T using each word in the group again, once we hit a node that 
has count = 1, we can now safely abbreviate that word.
*/
