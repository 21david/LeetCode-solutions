// Solved during Omkar DSA session on IK
// TC = O(N)
// SC = O(N)
class Solution {
    public int knightDialer(int n) {
        int mod = (int) 1e9+7;
        // System.out.println(mod);
        long[][] table = new long[n+1][10];
        for (int i = 0; i < 10; i++)
            table[1][i] = 1;

        for (short i = 2; i <= n; i++) {
            table[i][0] = (table[i-1][4] + table[i-1][6]) % mod;
            table[i][1] = (table[i-1][6] + table[i-1][8]) % mod;
            table[i][2] = (table[i-1][7] + table[i-1][9]) % mod;
            table[i][3] = (table[i-1][4] + table[i-1][8]) % mod;
            table[i][4] = (table[i-1][0] + table[i-1][3] + table[i-1][9]) % mod;
            table[i][5] = 0;
            table[i][6] = (table[i-1][0] + table[i-1][1] + table[i-1][7]) % mod;
            table[i][7] = (table[i-1][2] + table[i-1][6]) % mod;
            table[i][8] = (table[i-1][1] + table[i-1][3]) % mod;
            table[i][9] = (table[i-1][2] + table[i-1][4]) % mod;
        }

        // System.out.println(Arrays.deepToString(table));
        int answer = 0;
        for (long sum : table[n]) {
            answer += sum;
            answer %= mod;
        }
        return answer;
    }
}

/*
Keypad move map:

0 → 4, 6   // 0 can go to 4 and 6 only (and 4 and 6 can go to 0)
1 → 6, 8  
2 → 7, 9  
3 → 4, 8  
4 → 0, 3, 9  
5 → (no moves)  
6 → 0, 1, 7  
7 → 2, 6  
8 → 1, 3  
9 → 2, 4
*/