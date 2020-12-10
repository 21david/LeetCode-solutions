//  https://leetcode.com/problems/interval-list-intersections/

class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        ArrayList<int[]> intersections = new ArrayList<>();
        int a = 0, b = 0;
        
        while(a < A.length && b < B.length) {
            if(A[a][1] >= B[b][0]) // found an intersection
            {
                int max = Math.max(A[a][0], B[b][0]);
                int min = Math.min(A[a][1], B[b][1]);
                
                if(max <= min)
                    intersections.add(new int[] {max, min});
            }  
            
            if(A[a][1] >= B[b][0] && A[a][1] <= B[b][1]) 
                a++;
            else if(B[b][1] >= A[a][0] && B[b][1] <= A[a][1])
                b++;
            else if(B[b][1] < A[a][0])
                b++;
            else if(A[a][1] < B[b][0])
                a++;
        }
        
  //      for(int[] arr : intersections)
  //          System.out.println("["+ arr[0] + "," + arr[1] + "]");
        
        // convert ArrayList<int[]> to int[][]
        int[][] result = new int[intersections.size()][];
        
        for(int i = 0; i < intersections.size(); i++) {
            result[i] = intersections.get(i);
        }
        
        return result;
    }
}
