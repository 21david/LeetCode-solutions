//  https://leetcode.com/problems/meeting-scheduler/

/*
This approach is to sort the slots and then use two pointers to 
compare possible times when they will both be available. Check if the overlapping 
times when they will be available meet the required duration. If we find an 
overlapping time that meets the duration, return it as soon as we find it to get the 
earliest time. If we never find such a time, just return an empty array.

TC: O(NlogN)
SC: O(1), assuming O(1) sort

29 ms, beats 67%
55.03 MB, beats 66%
*/
class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, (a, b) -> a[0] - b[0]);
        Arrays.sort(slots2, (a, b) -> a[0] - b[0]);

        int p1 = 0, p2 = 0;
        int len1 = slots1.length, len2 = slots2.length;

        List<Integer> ans = new ArrayList<>();

        while (p1 < len1 && p2 < len2) {

            if (slots1[p1][0] > slots2[p2][1]) {
                // p2 is behind, there can be no overlap, so push p2 forward
                p2 += 1;
            }
            else if (slots2[p2][0] > slots1[p1][1]) {
                // p1 is behind, there can be no overlap, so push p1 forward
                p1 += 1;
            }

            // At this point, there is a guaranteed overlap
            // if person 2 becomes available after person 1
            else if (slots2[p2][0] >= slots1[p1][0]) {
                // check for mutual availability
                if (Math.min(slots1[p1][1],slots2[p2][1]) - slots2[p2][0] >= duration)
                    return Arrays.asList(slots2[p2][0], slots2[p2][0] + duration);
                else {
                    if (slots2[p2][1] < slots1[p1][1])
                        p2 += 1;
                    else
                        p1 += 1;
                }
            }
            // if person 1 becomes available after person 2
            else if (slots1[p1][0] > slots2[p2][0]) {
                // check for mutual availability
                if (Math.min(slots1[p1][1],slots2[p2][1]) - slots1[p1][0] >= duration)
                    return Arrays.asList(slots1[p1][0], slots1[p1][0] + duration);
                else {
                    if (slots1[p1][1] < slots2[p2][1])
                        p1 += 1;
                    else
                        p2 += 1;
                }
            }
        }

        return new ArrayList<Integer>();
    }
}


/*
Brute force approach. Sort and then compare each slot from one person to every other slot
from the other person. This gives a time complexity of O(NlogN + N^2) = O(N^2).

We can slightly optimize by not sorting, still comparing every slot to every other slot,
and keeping a variable to track the earliest valid time when they can meet, and return that
at the end. This reduces the O(NlogN) sorting complexity. However, It reduces the best case
scenario from O(NlogN) to O(N^2).
*/
class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        // 2491 ms, faster than 5.04%
        // 48.3 mb, less than 51.77%
        // Solved in 28 minutes 
        
        // sorts slots1 and slots2 by the first element of each inner array
        Arrays.sort(slots1, (x, y) -> x[0] - y[0]);
        Arrays.sort(slots2, (x, y) -> x[0] - y[0]);
        
        // compare each slot in slot1 to each slot in slot2 until a solution is found
        for(int i = 0; i < slots1.length; i++) {
            for(int j = 0; j < slots2.length; j++) {
                if(isScheduleMatch(slots1[i], slots2[j], duration)) {
                    int start = Math.max(slots1[i][0], slots2[j][0]);
                    return new ArrayList<Integer>(Arrays.asList(start, start + duration));
                }
            }
        }
        
        return new ArrayList<>();
    }
    
    public boolean isScheduleMatch(int[] slot1, int[] slot2, int duration) {
        int startOfMeet = -1, endOfMeet = -1;
        if(slot1[0] >= slot2[0]) {
            startOfMeet = slot1[0];
            endOfMeet = Math.min(slot1[1], slot2[1]);
        }
        else {
            startOfMeet = slot2[0];
            endOfMeet = Math.min(slot1[1], slot2[1]);
        }
        
        if(endOfMeet - startOfMeet <= 0)  // no intersection at all
            return false;
            
        return (endOfMeet - startOfMeet) >= duration;
    }
}
/*
Sample input:
[[10,50],[60,120],[140,210]]
[[0,15],[60,70]]
8

[[60,120],[140,210],[10,50]]
[[60,70],[0,15],[71,72],[5,10]]
8

[[0,2]]
[[1,3]]
1
*/


/*
Brute Force approach would be to create a very big array that starts at the earliest 
available time for either person and ends at the latest available time for either 
person. Then, for each spot in that array, which represents one unit of time, we will 
mark it true if both people are available at that time and false if either one or both 
are not available. Then we iterate through that array looking for a consecutive number 
of units of time where they're both available, of at least length 'duration'. If you 
search from left to right, the first valid overlap we find will be the answer, and we can 
just turn that into an array and return that as the answer.

TC: O(latest - earliest), where latest is highest number in the matrices, and earliest is
the lowest number in the matrices.
SC: O(latest - earliest)

This is correct but only passes 2 test cases and gives Memory Limit Exceeded on LeetCode 
due to the third test case being:
[[0,1000000000]]
[[0,1000000000]]
1000000
*/
class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        // Find earliest and latest time in both arrays
        int earliest = Integer.MAX_VALUE;
        int latest = 0;
        for (int[] slot : slots1) {
            earliest = Math.min(earliest, slot[0]);
            latest = Math.max(latest, slot[1]);
        }
        for (int[] slot : slots2) {
            earliest = Math.min(earliest, slot[0]);
            latest = Math.max(latest, slot[1]);
        }

        // Array with a slot for each unit of time, lets assume minutes
        // Value will be 2 if both are available for that minute
        int[] minutes = new int[latest - earliest + 1];

        for (int[] slot : slots1) {
            for (int m = slot[0]; m <= slot[1]; m++) {
                minutes[m - earliest] += 1;
            }
        }
        for (int[] slot : slots2) {
            for (int m = slot[0]; m <= slot[1]; m++) {
                minutes[m - earliest] += 1;
            }
        }

        // Find mutually available times
        int streak = 0;
        int streakStart = 0;
        for (int t = 0; t < minutes.length; t++) {
            if (minutes[t] == 2) {
                streak += 1;
                if (streak == duration) {
                    return Arrays.asList(earliest + (streakStart+1), earliest + (t+1));
                }
            }
            else {
                streak = 0;
                streakStart = t;
            }
        }
        

        return Arrays.asList();
    }
}
