class Solution {
    public int maxSum(int[] nums) {
        Set<Integer> uniquePositives = new HashSet<>();
        int answer = 0;
        for (int num : nums) {
            if (!uniquePositives.contains(num) && num > 0) {
                uniquePositives.add(num);
                answer += num;
            }
        }

        // If all values were negative or 0, pick the biggest number to maximize the sum
        if (uniquePositives.isEmpty())
            return Arrays.stream(nums).max().getAsInt();

        return answer;
    }
}

/* 
 Streams API explanation:
 Arrays.stream(nums)  // convert nums to a stream
    .max()  // get the max as an OptionalInt
    .getAsInt()  // convert to an actual int
*/

/*  
Edge cases:
[-1,-2,-3]
[-1,-2,0,-3]
[-100,-50, -2, -5, -10]
[-100]
*/
