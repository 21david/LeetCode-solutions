/*
https://leetcode.com/problems/find-all-anagrams-in-a-string/
*/

class Solution {
    int[] alphabetP = new int[26];
    
    public List<Integer> findAnagrams(String s, String p) {
        // 1659 ms, faster than 7.32%
        // 40.6 MB, less than 72.28%
        
        // for the example input, we can start a search at every index of s (up to and including s.length() - 3)
        // to check if those 3 letters are an anagram of p. If it is, add it to the final list.
        // for general input, we can start a search at every index of s up to and including s.length() - p.length()
        // to check if those p.length() letters are an anagram of p.
        // Time complexity: O(N * M), N is the # of chars in S, M is the # of chars in P
        // Space complexity: O(N), N is the # of chars in S 
        //   - we store an integer for every index of S that is the start of an anagram. In the worst
        //     case, this could be all the indices of S
        
        if(p.length() > s.length())
            return new ArrayList<>();
        
        // fill up the multiset for P, to be able to check for anagrams
        for(int i = 0; i < p.length(); i++)
            alphabetP[p.charAt(i) - 'a']++;
        
        ArrayList<Integer> startIndices = new ArrayList<>();
        
        // iterate through every possible index, looking for anagrams
        for(int i = 0; i <= s.length() - p.length(); i++)
        {
            if(isAnagram(s.substring(i, i + p.length()), p))
                startIndices.add(i);
        }
        
        return startIndices;
    }
    
    // O(M), where M is the number of characters in S or P, assuming length(S) == length(P)
    // if they have different lengths, this is O(1)
    public boolean isAnagram(String s, String p)
    {
        if(s.length() != p.length())
            return false;
        
        int[] alphabetS = new int[26];  // multiset, count the frequency of each character
        
        for(int i = 0; i < s.length(); i++)
            alphabetS[s.charAt(i) - 'a']++;
        
        for(int i = 0; i < 26; i++)
            if(alphabetS[i] != alphabetP[i])
                return false;
        
        return true;
    }
}
