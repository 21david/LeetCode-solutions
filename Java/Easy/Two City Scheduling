/*
https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

June leetcoding challenge, day 3
*/

class Solution {
    public int twoCitySchedCost(int[][] costs) {
        // 1 ms, faster than 97.36%
        
        /*
        Approach:
        We calculate the cost of sending everyone to city A
        Then, we calculate the refund we would get for each person,
        if we sent them to city B instead.
        We want to maximize the refund that we can get to minimize
        the total cost.
        So we can sort (ascending) the refund array that we will make 
        and take the first N values from that array to maximize the 
        refund.
        Then, we subtract the refund values from the cost of
        sending everyone to city A, and we get the minimum cost
        of sending N candidates to city A and N to city B.
        
        Time complexity: O(N*logN)
        Space complexity: O(N)
        */
        
        // find total cost of sending all candidates to city A
        int totalCost = 0;
        for(int[] arr : costs)
            totalCost += arr[0];
        
        // refund formula: arr[1] - arr[0] (for sending candidate to city B instead of A)
        int[] refunds = new int[costs.length];
        for(int i = 0; i < costs.length; i++)
            refunds[i] = costs[i][1] - costs[i][0];
        
        // sort refund array
        Arrays.sort(refunds);
        
        // get the biggest refunds possible
        for(int i = 0; i < costs.length / 2; i++)
            totalCost += refunds[i];
        
        return totalCost;
    }
}

/*
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        /*
        Approach: (Edit: this did not work for all test cases)
        Sort the arrays by their first and by their second integers
        (to make two sorted lists).
        
        We will make two candidate "minimum costs", the first one takes
        the first N from the first sorted list, and the remaining N from
        the second sorted list (then we calcualte the cost of that). 
        The second one takes the first N from the second sorted list, and
        the remaining N from the first sorted list, and we calculate the
        cost of that. 
        
        Then, we return the minimum of those two costs.
        
        Time complexity: O(N*logN)
        Space complexity: O(N)
        */
        /*
        int N = costs.length / 2;
        int cost1 = 0;
        int cost2 = 0;
        
        int[][] costsCopy = Arrays.copyOf(costs, costs.length);
        
        // FIRST PART
        
        
        Arrays.sort(costsCopy, new Comparator<int[]>() {
           public int compare(int[] arr1, int[] arr2)
           {
               if(arr1[0] < arr2[0]) // make it sort ascending, by first integer
                   return -1;
               else if (arr1[0] > arr2[0])
                   return 1;
               else  // if first integers are equal, sort descending by their other integer
               {
                   if(arr1[1] < arr2[1])
                       return 1;
                   else if(arr1[1] > arr2[1])
                       return -1;
                   else // if both arrays are exactly the same
                       return 0;
               }
           }
        });
        
        // let's take the first N and calculate the cost of that
        int cost = 0;
        
        for(int i = 0; i < N; i++)
        {
            cost += costsCopy[i][0];
            costsCopy[i] = null;
        }
        
        // let's take the remaining N values and add to cost
        for(int i = 0; i < costsCopy.length; i++)
        {
            if(costsCopy[i] != null)
                cost += costsCopy[i][1];
        }
        
        
        
        // SECOND PART
        
        System.out.println(cost);
        cost1 = cost;
        
        // get a copy of the original array again
        costsCopy = Arrays.copyOf(costs, costs.length);
        
        Arrays.sort(costsCopy, new Comparator<int[]>() {
           public int compare(int[] arr1, int[] arr2)
           {
               if(arr1[1] < arr2[1]) // make it sort ascending, by second integer
                   return -1;
               else if (arr1[1] > arr2[1])
                   return 1;
               else  // if first integers are equal, sort descending by their other integer
               {
                   if(arr1[0] < arr2[0])
                       return 1;
                   else if(arr1[0] > arr2[0])
                       return -1;
                   else // if both arrays are exactly the same
                       return 0;
               }
           }
        });
        
        cost = 0;
        
        // let's take the first N values of the second sorted list
        // and calculate the cost of that
        for(int i = 0; i < N; i++)
        {
            cost += costsCopy[i][1];
            costsCopy[i] = null;
        }
        
        // let's take the remaining N values and add to cost
        for(int i = 0; i < costsCopy.length; i++)
        {
            if(costsCopy[i] != null)
                cost += costsCopy[i][0];
        }
        System.out.println(cost);
        cost2 = cost;
        
        
        
        return Math.min(cost1, cost2);
    }
}
*/
