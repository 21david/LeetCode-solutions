// https://leetcode.com/problems/delete-characters-to-make-fancy-string

// TC = O(N), process each character once
// Aux SC = O(N), for the string builder
class Solution {
    public String makeFancyString(String s) {
        StringBuilder answer = new StringBuilder();
        answer.append(s.charAt(0));

        int consecutive = 1;

        for (int i = 1; i < s.length(); i++) {
            // Keep track of amount of consecutive equal characters
            if (s.charAt(i) == s.charAt(i-1))
                consecutive++;
            else
                consecutive = 1;

            // If the amount is 3 or more, skip character so there's only 
            // 2 equal consecutive characters max
            if (consecutive >= 3)
                continue;

            answer.append(s.charAt(i));
        }

        return answer.toString();
    }
}
