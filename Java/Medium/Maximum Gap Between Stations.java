// TC = O(N + M)
// Aux SC = O(N)
// N = skill.length(),  M = station.length()
class Solution {
    public int maximumGap(String skill, String station) {

        // Leftmost possible position for each letter in skill
        int[] leftmost = new int[skill.length()];
        int j = 0;
        for (int i = 0; i < skill.length(); i++) {
            while (skill.charAt(i) != station.charAt(j))
                j++;

            leftmost[i] = j;
            j++;
        }

        // Right most possible position for each letter in skill
        int[] rightmost = new int[skill.length()];
        j = station.length() - 1;
        for (int i = skill.length() - 1; i >= 0; i--) {
            while (skill.charAt(i) != station.charAt(j))
                j--;

            rightmost[i] = j;
            j--;
        }

        // For each pair of two consecutive letters in skill, find their max possible distance, 
        // and return the largest distance
        int ans = 0;
        for (int i = 1; i < skill.length(); i++) {
            int left_leftmost = leftmost[i - 1];  // left letter's leftmost position
            int right_rightmost = rightmost[i];  // right letter's rightmost position
            ans = Math.max(ans, right_rightmost - left_leftmost);
        }

        return ans;
    }
}

/*
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        # we have to have a way to check for the max gap between any pair of two consecutive letters in skill
        # max TC logN for that check for a total max complexity of NlogN
        # each letter in skill has a first letter it could be assigned to in station, and a last one
        # we can know by trying to greedily assign from both dierctions?
        # then we take those mins and maxes and do a subtraction between all pairs to find max possible distance
        # storing the max of all of those
        
        sk, st = skill, station
        S = len(skill)

        # Earliest possible position for each letter in skill
        mns = [0] * S
        j = 0
        for i in range(S):
            while st[j] != sk[i]:
                j += 1

            # now sk[i] == st[j]
            mns[i] = j
            j += 1

        # Latest posible position for each letter in skill
        mxs = [0] * S
        j = len(station) - 1
        for i in range(S - 1, -1, -1):
            while st[j] != sk[i]:
                j -= 1

            # now sk[i] == st[j]
            mxs[i] = j
            j -= 1

        # For each pair of two consecutive letters in skill, compare left letter's earliest possible position
        # with right letter's latest possible position. Store the max of all of those.
        ans = 0
        for i in range(1, len(mns)):
            min_l = mns[i-1]
            max_r = mxs[i]
            ans = max(ans, max_r - min_l)

        return ans


    */
