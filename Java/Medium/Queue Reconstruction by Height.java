/*
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

June leetcoding challenge, day 6
Solved after seeing solutions
*/

/*
- The first person in the queue will always have k = 0
- The tallest person will always have one k = 0 (if multiple of the tallest, they will all have different ks, but one is gauranteed to be 0)
- The shortest person will always have everyone in front of them be taller than them. So the shortest person will always be in position k (if there are multiple, the nexts ones will follow behind )
Find all the values with k = 0. The value with a minimum h out of those values is the first person in the queue.
*/

/*
Algorithm:
Sort by descending h, and by ascending k
Start from the beginning of the sorted list, and add each
  value (h, k) to index k in a new list.
*/
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Comparator<int[]>() {
           public int compare(int[] arr1, int[] arr2) {
               // descending arr[0], and ascending arr[1]
               if(arr1[0] < arr2[0])
                   return 1;
               else if(arr1[0] > arr2[0])
                   return -1;
               else {  // if arr1[0] == arr2[0], then we sort by ascending arr[1]
                   if(arr1[1] < arr2[1])
                       return -1;
                   else if(arr1[1] > arr2[1])
                       return 1;
                   else  // if both arrays are exactly the same
                       return 0;
               }
           }
        });
        
        // now we construct the list by placing value (h, k) into index k in our new array
        ArrayList<int[]> answer = new ArrayList<>();
        
        for(int[] person : people)
            answer.add(person[1], person);  // add person to 'answer' array at index k (k = person[1])
        
        // convert to int[][]
        int[][] finalAnswer = new int[people.length][];
        
        for(int i = 0; i < answer.size(); i++)
            finalAnswer[i] = answer.get(i);
        
        return finalAnswer;
    }
}
