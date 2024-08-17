class Solution {
    public boolean isStrictlyPalindromic(int n) {
        // No number meets the requirement, so answer is always false.
        // Show proof of value in different bases:
        // (isn't fully accurate for larger numbers)
        for(int base = n-2; base > 1; base--)
            System.out.println( Integer.toString(n, base) );

        return false;
    }
}
