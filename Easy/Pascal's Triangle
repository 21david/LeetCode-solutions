//  https://leetcode.com/problems/pascals-triangle/

class Solution {
    public List<List<Integer>> generate(int numRows) {
        // 0 ms, faster than 100%
        // 36.2 mb, less than 99.66%
        // Solved in about 10 minutes
        
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        
        for(int i = 0; i < numRows; i++) {
            answer.add(new ArrayList<Integer>());
            answer.get(i).add(1);
        }
        
        if(numRows == 1)
            return answer;
        
        answer.get(1).add(1);
        
        int sum = 0;
        for(int i = 2; i < numRows; i++) {
            for(int j = 1; j < i; j++) {
                // add the two parents
                sum = answer.get(i-1).get(j-1) + answer.get(i-1).get(j);
                answer.get(i).add(sum);
            }
            answer.get(i).add(1);
        }
        
        
        return answer;
    }
}

/*
Sample input:
1
2
3
4
5
10

*/
