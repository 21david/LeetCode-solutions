// TC = O(log N)  
// SC = O(log N)
// more specifically, log base 10
class Solution {
    public boolean checkDivisibility(int n) {
        String strVersion = String.valueOf(n); // OR Integer.toString(n);

        int sum = 0, product = 1;

        for (char digit : strVersion.toCharArray()) {
            byte actualVal = (byte) (digit - 48);
            sum += actualVal;
            product *= actualVal;
        }

        return n % (sum + product) == 0;
    }
}
