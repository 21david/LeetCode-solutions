//  https://leetcode.com/problems/encode-and-decode-tinyurl/

public class Codec {
    // Key: long URL
    // Value: shortened URL
    HashMap<String, String> lookupTable1 = new HashMap<>();
    
    // Key: shortened URL
    // Value: long URL
    HashMap<String, String> lookupTable2 = new HashMap<>();
    
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        // map this URL to the next available tiny url
        // the tiny urls will start at 0 and increase just as an integer would.
        
        String shortUrl;
        
        if(lookupTable1.containsKey(longUrl))
            return lookupTable1.get(longUrl);
        else {
            int curSize = lookupTable1.size();
            shortUrl = "http://tinyurl.com/" + curSize;
            System.out.println(shortUrl);
            lookupTable1.put(longUrl, shortUrl);
            
            lookupTable2.put(shortUrl, longUrl);
        }
        
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        if(lookupTable2.containsKey(shortUrl))
            return lookupTable2.get(shortUrl); // return the long URL of this shortened URL
        else
            return null;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
