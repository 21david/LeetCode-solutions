//  https://leetcode.com/problems/prefix-and-suffix-search/
// 801 ms, faster than 5.15%
// 56.3 mb, less than 82.83%
// Solved in 23 minutes, used the hint
class WordFilter {
    String[] dict;
    HashMap<String, Integer> cache;  // cache inputs and their outputs
    
    public WordFilter(String[] words) {
        dict = words;
        cache = new HashMap<>();
    }
    
    public int f(String prefix, String suffix) {
        if(cache.containsKey(prefix + "#" + suffix))
            return cache.get(prefix + "#" + suffix);
        
        int wordIndex = -1;
        boolean found = false;
        
        for(int i = 0; i < dict.length; i++) {
            if(dict[i].startsWith(prefix) && dict[i].endsWith(suffix)) {
                found = true;
                wordIndex = i;
            }
        }
        
        cache.put(prefix + "#" + suffix, wordIndex);
        
        return wordIndex;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */

/*
Sample input:
["WordFilter","f"]
[[["apple"]],["a","e"]]
["WordFilter","f"]
[[["apple", "banana", "cat", "dogecoin", "elephant", "fred", "google", "groogle", "halloween"]],["g","e"], ["d","n"]]
["WordFilter","f","f"]
[[["google", "halloween", "cat", "groogle", "elephant", "fred", "banana", "dogecoin", "apple"]],["g","e"], ["d","n"]]
*/
