enum numeral {
    zero,
    M,
    CM,
    D,
    CD,
    C,
    XC,
    L,
    XL,
    X,
    IX,
    V,
    IV,
    I
};

class Solution {
public:
    int romanToInt(string s) {
        int len = s.length();
        int ans = 0;
        
        for(int i = 0; i < len; i++) {
            if(hash_it(s.substr(i, 2)) != zero) {
                ans += helper(s.substr(i, 2));
                i++;
                continue;
            }
            else {
                ans += helper(s.substr(i, 1));
                continue;
            }
        }
        
        return ans;
    }
    
    int helper(string letters) {
        switch(hash_it(letters)) {
            case M:
                return 1000;
            
            case CM: 
                return 900;
            
            case D: 
                return 500;
            
            case CD: 
                return 400;
            
            case C: 
                return 100;
            
            case XC: 
                return 90;
            
            case L: 
                return 50;
            
            case XL: 
                return 40;
            
            case X: 
                return 10;
            
            case IX: 
                return 9;
            
            case V: 
                return 5;
            
            case IV: 
                return 4;
            
            case I: 
                return 1;
            
            default: return 0;
        }
    }
    
    numeral hash_it(string letters) {
        if(letters == "M") return M;
        if(letters == "CM") return CM;
        if(letters == "D") return D;
        if(letters == "CD") return CD;
        if(letters == "C") return C;
        if(letters == "XC") return XC;
        if(letters == "L") return L;
        if(letters == "XL") return XL;
        if(letters == "X") return X;
        if(letters == "IX") return IX;
        if(letters == "V") return V;
        if(letters == "IV") return IV;
        if(letters == "I") return I;
        
        return zero;
    }
};


/*
Order:
M
CM
D
CD
C
XC
L
XL
X
IX
V
IV
I

*/
