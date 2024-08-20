//  https://leetcode.com/problems/brick-wall/submissions/

class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        // 8 ms, faster than 96.19%
        // 42.5 mb, less than 29.81%
        // Solved in 30 minutes 24 seconds
        
        /*
        I think we can iterate through each row of bricks, and
        figure out at what x-value all the gaps are (by summing
        each element to all the previous ones). With these x-values,
        we can put them in some HashMap that counts the number
        of gaps at each x-value (the number of gaps we would pass if
        we drew a vertical line at that x-value). After iterating
        through every row, the HashMap would contain a count of how
        many gaps are at each x-value (for x-values that have at least 1
        gap). We could find the maximum value in this map, and the key
        of that value would represent the x-value of our desired
        vertical line. To find the answer, we would subtract this value from
        the height of the brick wall (height - gaps = bricks crossed).
        
        
        */
        int rows = wall.size();
        
        HashMap<Integer, Integer> countGaps = new HashMap<>();
        
        int sum = 0;
        
        List<Integer> curRow;
        for(int i = 0; i < rows; i++) {
            curRow = wall.get(i);
            sum = 0;
            for(int j = 0; j < curRow.size() - 1; j++) {
                sum += curRow.get(j);
                countGaps.put(sum, countGaps.getOrDefault(sum, 0) + 1);
            }
        }
        
   //     System.out.println(countGaps);
        
        // if there are no gaps, the best solution is just a line
        // drawn vertically anywhere, crossing all rows
        if(countGaps.isEmpty())
            return rows;
        
        // now we find the highest value in the map, and use the
        // key of that value to find the answer
        int maxVal = Integer.MIN_VALUE;
        int maxKeyVal = Integer.MIN_VALUE;
        Set<Integer> keySet = countGaps.keySet();
        for(Integer key : keySet) {
            if(countGaps.get(key) > maxVal) {
                maxVal = countGaps.get(key);
                maxKeyVal = key;
            }
        }
        
        return rows - maxVal;
    }
}

/*
Sample input:
[[1]]
[[100]]
[[5],[5],[5]]
[[6],[3,3],[6],[6],[6]]
[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

*/
