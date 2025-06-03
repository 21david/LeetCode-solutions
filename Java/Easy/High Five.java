//  https://leetcode.com/problems/high-five/

class Solution {
    public int[][] highFive(int[][] items) {
        // 3 ms, faster than 99.32%
        // 38.6 mb, less than 99.79%
        // Solved in 21 minutes
        
        /*
        We can sort by student ID, and then by their scores in descending order,
        then we can iterate through only the first 5 for each student, and add
        their average to another array which we return at the end.
        
        */
        
        Arrays.sort(items, (x, y) -> {
           if(x[0] == y[0]) {
                if(x[1] == y[1])
                    return 0;
               else if(x[1] > y[1])
                   return -1;
               else
                   return 1;
           }
            else if(x[0] < y[0])
                return -1;
            else
                return 1;
        });
        
        ArrayList<int[]> averages = new ArrayList<>();
        
        // for each ID, sum the top 5, average them, add a new record
        // to the solution array, and move on to the next ID
        int curID = items[0][0];
        int count = 5;
        int sum = 0;
        for(int i = 0; i < items.length; i++) {
            if(count > 0) {
                sum += items[i][1];
                count--;
                
                if(count == 0) // we finished summing the top 5 scores
                    averages.add(new int[] {curID, sum / 5});
            }
            else {
                if(items[i][0] == curID) // if we haven't found a new student
                    continue;
                else // we found a new student
                {
                    count = 5;
                    curID = items[i][0];
                    sum = 0;
                    i--;
                }
            }
            
        }
        
        int[][] ans = new int[averages.size()][];
        
        for(int i = 0; i < averages.size(); i++)
            ans[i] = averages.get(i);
        
        return ans;
    }
}
