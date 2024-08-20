/*
https://leetcode.com/problems/group-anagrams/
*/

class Solution {
    
    // solution using a hash value that uses primes numbers & multiplication to create hash value
    // this way, a hash code for a word will be shared with all of its anagrams, and only its anagrams
    
    // first 26 primes
    int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
    
    public List<List<String>> groupAnagrams(String[] strs) {
        
        // 5 ms, faster than 99.36%
        // 42.4 mb, less than 91.81%
        
        // Map Hash value -> List of words
        HashMap<Long, List<String>> map = new HashMap<>();
        
        long h = hash(strs[0]);
        map.put(h, new ArrayList<>());
        map.get(h).add(strs[0]);
        
        
        iterateStrs:
        for(int i = 1; i < strs.length; i++)
        {
            h = hash(strs[i]);
            if(map.containsKey(h))
                map.get(h).add(strs[i]);
            else
            {
                map.put(h, new ArrayList<>());
                map.get(h).add(strs[i]);
            }
        }
        
        
        List<List<String>> answer = new ArrayList<>();
        
        // create the final list of lists using the hashmap
        for(List<String> list : map.values())
            answer.add(list);
        
        return answer;
    }
    
    public long hash(String s)
    {
        long h = 1;

        for(char c : s.toCharArray())
            h *= primes[c - 'a'];

        return h;
    }
}


/*
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        // 6 ms, faster than 97.07%
        // 42.6 mb, less than 83.63%
        
        if(strs.length == 0)
            return null;
        
        // Runtime:
        // O(N * Mlog(M))
        // where N is the number of words, and M is the length of the longest word in strs
        // each word is sorted then added to the hashmap
        // Mlog(M) to sort a word, and N because each word has to be considered, thus N * Mlog(M)
        
        // A more optimal solution is to create a key using a hash function instead of sorting each word
        // hash function can be written cleverly with prime numbers
        // leetcode.com/problems/group-anagrams/discuss/566709/Java-or-4ms
        // (see above solution)
        
        HashMap<String, List<String>> map = new HashMap<>();
        
        String curWord = "";
        String curWordSorted = "";
        
        for(int i = 0; i < strs.length; i++)
        {
            curWord = strs[i];
            char[] curWordArray = curWord.toCharArray();
            
            Arrays.sort(curWordArray);
            
            curWordSorted = new String(curWordArray);
            
            if(map.containsKey(curWordSorted))
                map.get(curWordSorted).add(curWord);
            else
            {
                map.put(curWordSorted, new ArrayList<String>());
                map.get(curWordSorted).add(curWord);
            }
        }
        
        List<List<String>> answer = new ArrayList<>();
        
        // create the final list of lists using the hashmap
        for(List<String> list : map.values())
            answer.add(list);
        
        
        return answer;
    }
}
*/

/*
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        //  Time limit exceeded
        
        // Runtime:
        // O(N^2)
        // this occurs worst when every word is different
    
        if(strs.length == 0)
            return null;
        
        List<List<String>> result = new ArrayList<>();
        result.add(new ArrayList<String>());
        result.get(0).add(strs[0]);
        
        iterateStrs:
        for(int i = 1; i < strs.length; i++)
        {
            for(int j = 0; j < result.size(); j++)
            {
                if(isAnagram(result.get(j).get(0), strs[i]))
                {
                    result.get(j).add(strs[i]);
                    continue iterateStrs;
                }
            }
            
            // if it didn't find a group to put strs[i] in
            result.add(new ArrayList<String>());
            result.get(result.size() - 1).add(strs[i]);
        
        }
        
        return result;
    }
    
    public boolean isAnagram(String str1, String str2)
    {
        int[] alphabet1 = new int[26];
        int[] alphabet2 = new int[26];
        
        for(char c : str1.toCharArray())
            alphabet1[c - 'a']++;
        
        for(char c : str2.toCharArray())
            alphabet2[c - 'a']++;
        
        // compare both arrays
        for(int i = 0; i < 26; i++)
        {
            if(alphabet1[i] != alphabet2[i])
                return false;
        }
        
        return true;
    }
}
*/
