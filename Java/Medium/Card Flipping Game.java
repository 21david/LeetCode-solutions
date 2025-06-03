//  https://leetcode.com/problems/card-flipping-game/solution/

class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        // 7 ms, faster than 11.63%
        // 39.3 mb, less than 33.72%
        // Solved in 22 minutes
        
        /*
            If there ever exists a card that has the same number on the
            front as on the back, then that number is not the answer.
            
            I think all we do is find the smallest number for which there is
            no card that has that number on both the front and back.
            
            We can put all #s in a HashSet, iterate through both arrays at the
            same time and remove from the HashSet any number that gets 
            "eliminated". Then, we return the smallest number in the HashSet.
        */
        
        HashSet<Integer> goodNums = new HashSet<>();
        
        for(int n : fronts)
            goodNums.add(n);
        
        for(int n : backs)
            goodNums.add(n);
        
        for(int i = 0; i < fronts.length; i++) {
            if(fronts[i] == backs[i])
                goodNums.remove(fronts[i]);
        }
        
        System.out.println(goodNums);
        
        if(goodNums.size() == 0)
            return 0;
        
        int min = Integer.MAX_VALUE;
        
        for(int n : goodNums)
            min = Math.min(min, n);
        
        return min;   
    }
}

/*

Sample testcases:
[1,2,4,4,7]
[1,3,5,1,3]

[4,5,9,2,3,8,7,1,6]
[4,5,9,2,3,8,7,1,5]

[1,1,3,4,9,7,6]
[2,3,3,5,8,6,5]

[3,3,3,3,3,3,3,3,3,3,6]
[3,1,2,4,5,6,7,8,9,3,5]

[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,9,9,10,11,12]
[1,1,2,2,1,2,2,2,1,3,1,1,4,5,2,1,5,3,2,1,6,7,8,9,6,5,4,3,2,8,3,2,1,9,3,9,8,7]

[1,1,1,2,2,2,2,3,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,20,29]
[1,2,3,2,3,4,5,3,4,5,4,5,5,6,6,7,7,8,8,9,9,1,10,11,11,20,29]

Expected output:
2
6
1
1
7

-----------

Copy-able testcases:
[1,2,4,4,7]
[1,3,5,1,3]
[4,5,9,2,3,8,7,1,6]
[4,5,9,2,3,8,7,1,5]
[1,1,3,4,9,7,6]
[2,3,3,5,8,6,5]
[3,3,3,3,3,3,3,3,3,3,6]
[3,1,2,4,5,6,7,8,9,3,5]
[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,9,9,10,11,12]
[1,1,2,2,1,2,2,2,1,3,1,1,4,5,2,1,5,3,2,1,6,7,8,9,6,5,4,3,2,8,3,2,1,9,3,9,8,7]
[1,1,1,2,2,2,2,3,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,20,29]
[1,2,3,2,3,4,5,3,4,5,4,5,5,6,6,7,7,8,8,9,9,1,10,11,11,20,29]

*/
