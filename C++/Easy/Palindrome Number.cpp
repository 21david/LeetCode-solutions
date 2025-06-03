class Solution {
public:
    bool isPalindrome(int x) {
        long int orig = x;
        long int reversed = 0;
        
        while(x > 0) {
            reversed += x % 10;
            x /= 10;    
            reversed *= 10;
        }
        reversed /= 10;

        // cout << reversed << endl;
        // cout << orig << endl;
        // cout << (reversed == orig) << endl;
        
        return reversed == orig;
    }
};
