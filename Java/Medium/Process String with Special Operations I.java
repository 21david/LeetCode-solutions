// Solution 1
class Solution {
    public String processStr(String s) {
        StringBuilder answer = new StringBuilder();

        boolean empty;
        for (Character c : s.toCharArray()) {
            empty = answer.length() == 0;
            switch (c) {
                // Java 21 syntax
                case Character ch when Character.isAlphabetic(ch) -> answer.append(c);
                case '*' -> { 
                    if (!empty) 
                        answer.deleteCharAt(answer.length() - 1);
                }
                case '#' -> { 
                    if (!empty) 
                        answer.append(answer);
                } 
                case '%' -> { 
                    if (!empty) 
                        answer.reverse(); 
                }
                default -> {}
            }
        }

        return answer.toString();
    }
}


// Solution 2
class Solution {
    public String processStr(String s) {
        StringBuilder answer = new StringBuilder();

        for (char c : s.toCharArray()) {
            final boolean empty = answer.length() == 0;

            switch ((Character) c) {
                // Java 21 syntax
                case Character ch when Character.isAlphabetic(ch) -> answer.append(ch);

                case Character ch when !empty && ch == '*' -> 
                    answer.deleteCharAt(answer.length() - 1);

                case Character ch when !empty && ch == '#' -> 
                    answer.append(answer);

                case Character ch when !empty && ch == '%' -> 
                    answer.reverse();

                default -> {}
            }
        }

        return answer.toString();
    }
}
