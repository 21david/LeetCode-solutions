/*
https://leetcode.com/problems/single-element-in-a-sorted-array
*/

/*
If there is an array consisting of only integers that appear twice, then the index of every left element
would be an even number. So if one element is placed somewhere in the array between pairs, 
all the pairs to the right would be displaced by 1, causing their left elements to have an odd index.
This algorithm uses the fact that the left element of a pair will have an even index if there is no single element
anywhere to the left of that pair, and it will have an odd index if there is a single element somewhere
to the left of that pair. The binary search can know which direction to go in like this.
*/
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        int med = (high+low) / 2;
        
        boolean found = false;
        
        while(!found)
        {
            // check if current one is single element
            if( (med == 0 || nums[med] != nums[med - 1])
            && (med == nums.length - 1 || nums[med] != nums[med + 1]) )
                return nums[med];
            
            // check if this is the left element of a pair, if not, move to the left
            int cur = med;
            if(cur > 0 && nums[cur - 1] == nums[cur])
                cur--;
            
            // if the index of the left element is odd, then the single element is to the left
            // else it's to the right
            if(cur % 2 == 1) // single element is to the left
                high = med - 1;
            else // single element is to the right
                low = med + 1;
            
            med = (high + low) / 2;
        }
        
        return -1;
    }
}
    
/*
    // Solution using a multiset, O(N)
    // Performs poorly, faster than about 5% of all java submissions

    HashMap<Integer, Integer> map = new HashMap<>();
    
    // iterate through the array, add each element to the muiltiset
    for(int i = 0; i < nums.length; i++)
    {
        if(map.containsKey(nums[i]))
            map.put(nums[i], map.get(nums[i]) + 1);
        else
            map.put(nums[i], 1);
    }
    
    Iterator<Integer> it = map.keySet().iterator();
        
    while(it.hasNext())
    {
        int key =  it.next() ;
        if(map.get(key) == 1)
            return key;
            
    }
    
    return 0;
    
}
*/
