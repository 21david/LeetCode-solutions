/*
1. Generate all permutations of binary strings of length n
2. For each one, calculate the cost and add the passing ones to the final answer list
    - Don't let strings with consecutive 1s pass

TC = O(2^N * N)
Aux SC = O(N)
Output SC = O(2^N * N) 
*/
import static java.lang.System.*;
class Solution {
    int n, k;
    ArrayList<String> ans = new ArrayList<>();
    
    public List<String> generateValidStrings(int n, int k) {
        this.n = n;
        this.k = k;

        perms(new ArrayList<String>());

        return ans;
    }

    // Calcualte the "cost" of a binary string
    // O(N), N = length of binary string
    public int cost(List<String> binary) {
        int sum = 0;

        for (int i = 0; i < binary.size(); i++) {
            if (binary.get(i) == "1") {
                if (i < n - 1 && binary.get(i+1) == "1")  // Prevent consecutive 1s
                    return Integer.MAX_VALUE;
                
                sum += i;
            }
        }

        return sum;
    }

    // Find all binary strings of length n
    // Add the ones with cost <= k to the final answer list
    // O(2^n)
    public void perms(List<String> arr) {
        if (arr.size() == n) {
            if (cost(arr) <= k)
                ans.add(String.join("", arr));
            return;
        }

        arr.add("1");
        perms(arr);
        arr.remove(arr.size() - 1);
        
        arr.add("0");
        perms(arr);
        arr.remove(arr.size() - 1);
    }
}
