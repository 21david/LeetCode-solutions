/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

May Leetcoding challenge, day 10
*/

class Solution {
    public int findJudge(int N, int[][] trust) {
        /*
        If there is a town judge, then his number will appear N - 1 times in the input data (as the 2nd element of an array)
        We can create a multiset containing each person, and how many people trust that person.
        Then we can look out for the person that has N-1 people who trust him, and if he doesn't trust anyone,
        then return him as the judge. If he trusts someone or if no one has N-1 people trusting him, return -1.
        
        Should be O(N) runtime.
        */
        
        // edge cases
        if(N <= 1)
            return 1;
        else if(N == 2 && trust.length == 1)
            return trust[0][1];
        else if(N == 2 && trust.length == 2)
            return -1;
        
        HashMap<Integer, Integer> trustCount = new HashMap<>();
        Set<Integer> trustsSomeone = new HashSet<Integer>(); // judge must trust no one, so he can't appear in this set
        int temp;
        
        int townJudgeSuspect = -1;
        
        for(int[] trustInfo : trust)
        {
            trustsSomeone.add(trustInfo[0]);
            if(trustCount.containsKey(trustInfo[1]))
            {
                temp = trustCount.get(trustInfo[1]);
                if(temp + 1 == N - 1) // if this guy is already trusted by N-1 people, we found the judge
                    townJudgeSuspect = trustInfo[1];
                trustCount.put(trustInfo[1], temp + 1);
            }
            else
                trustCount.put(trustInfo[1], 1);
        }
        
        if(!trustsSomeone.contains(townJudgeSuspect))
            return townJudgeSuspect;
        else
            return -1;
    }
}
