//  https://leetcode.com/contest/weekly-contest-234/problems/evaluate-the-bracket-pairs-of-a-string/
//  (Need a LeetCode account to see ^)

class Solution {
    public String evaluate(String s, List<List<String>> knowledgeInput) {
        HashMap<String, String> knowledge = new HashMap<>();
        
        for(List<String> know : knowledgeInput)
            knowledge.put(know.get(0), know.get(1));
        
        int i = 0;
        boolean inPar = false;
        char cur;
        StringBuilder answer = new StringBuilder();
        StringBuilder sb = new StringBuilder();
        String key;
        while(i < s.length()) {
            cur = s.charAt(i);
            if(inPar) {
                if(cur == ')') { // reached the end of a key
                    inPar = false;
                    
                    // get the key's value, and add it to the answer string
                    key = sb.toString();
                    if(knowledge.containsKey(key))
                        answer.append(knowledge.get(key));
                    else
                        answer.append('?');
                    
                    // reset the temp string
                    sb = new StringBuilder();
                }
                else { // still processing the key
                    sb.append(cur);
                }
            }
            else {
                if(cur == '(')  { // found a new key
                    inPar = true;
                    i++;
                    continue;
                }
                else { // a regular character, just add it to the answer string regularly
                    answer.append(cur);
                    
                }
            }
            
            i++;
        }
        
        return answer.toString();
    }
}

/*
Sample input:
"(name)is(age)yearsold"
[["name","bob"],["age","two"]]
"hi(name)"
[["a","b"]]
"(a)(a)(a)aaa"
[["a","yes"]]
"(a)(b)"
[["a","b"],["b","a"]]

*/
