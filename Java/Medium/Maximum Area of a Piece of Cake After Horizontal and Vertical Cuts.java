//  https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        // 13 ms, faster than 95.76%
        // 49.3 mb, less than 29.36%
        // Solved in 22 minutes 30 seconds
        
        /*
        
        I think if we find the maximum distance between any two horizontal cuts
        and any two vertical cuts, we can multiply these two to get the area
        of the biggest piece of cake.
        
        Since the arrays don't seems to be sorted, we need to sort them.
        Then, we can iterate through them, finding the difference between every
        two adjacent elements, keeping track of the biggest difference we find.
        
        Then, we can return the product of these two.
        */
        
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        
        // HORIZONTAL CUTS
        
        // find the initial difference, which is the first cut minus the left edge (0)
        int maxHor = horizontalCuts[0] - 0;
        
        // compare that value with all other values to find the max difference
        for(int i = 1; i < horizontalCuts.length; i++) {
            maxHor = Math.max(maxHor, horizontalCuts[i] - horizontalCuts[i-1]);
        }
        
        // find the last difference, which is the right edge (w) minus the last horizontal cut
        maxHor = Math.max(maxHor, h - horizontalCuts[horizontalCuts.length-1]);
        
        
        // VERTICAL CUTS
        
        // find the initial difference, which is the first cut minus the top edge (0)
        int maxVer = verticalCuts[0] - 0;
        
        // compare that value with all other values to find the max difference
        for(int i = 1; i < verticalCuts.length; i++) {
            maxVer = Math.max(maxVer, verticalCuts[i] - verticalCuts[i-1]);
        }
        
        // find the last difference, which is the right edge (w) minus the last horizontal cut
        maxVer = Math.max(maxVer, w - verticalCuts[verticalCuts.length-1]);
        
        return (int) (((long) maxHor * maxVer) % (Math.pow(10,9) + 7));
    }
}
