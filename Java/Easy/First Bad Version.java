/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

May 30-day LeetCoding challenge, day 1
*/

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int lowestBad = n;
        
        int calls = 0;
        
        int hi = n, lo = 1;
        int mid;
        
        while(lo <= hi)
        {
            mid = lo + (hi - lo) / 2;
            
            if(isBadVersion(mid))
            {
                lowestBad = mid;
                hi = mid - 1;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return lowestBad;
    }
}
