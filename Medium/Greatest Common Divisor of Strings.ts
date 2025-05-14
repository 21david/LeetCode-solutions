/*  
1. Get divisors of each (O(√N))
2. For each divisor, from least to greatest, 
   check if it the string can be "divided" with this divisor.
3. Store the divisors that divide the string in a set, only for the first string. 
4. For the second string, for each divisor that divides it, check if it is in 
   the set, and that the divisor substrings are actually equal. If so, store it 
   as the current highest GCD string.
5. When done, return the highest GCD string.

TC: O(N √N)
SC: O(√N)
*/
function gcdOfStrings(str1: string, str2: string): string {
    function getDivisors(length) {
        let divs = [1];
        let bigDivs = [];
        if (length > 1) bigDivs.push(length);
        let bigDiv;
        for (let num = 2; num <= Math.floor(Math.sqrt(length)); num++) {
            if (length % num === 0) {
                divs.push(num);
                bigDiv = length / num;
                if (num !== bigDiv)
                    bigDivs.push(bigDiv);
            }
        }
        bigDivs.reverse();
        divs.push(...bigDivs);
        return divs;
    }

    let divs1 = getDivisors(str1.length);
    let divs2 = getDivisors(str2.length);

    let divisors = new Set<number>();

    // Find divisors of first string
    outer:
    for (let div of divs1) {
        // Check current divisor
        let sub = str1.slice(0, div);
        for (let i = div; i < str1.length; i += div) {
            if (str1.slice(i, i + div) !== sub)
                continue outer;
        }
        // If a divisor can divide the entire string, add it to the set
        divisors.add(div);
    }

    // Find divisors of second string
    let gcd = '';
    outer:
    for (let div of divs2) {
        // Check current divisor
        let sub = str2.slice(0, div);
        for (let i = div; i < str2.length; i += div) {
            if (str2.slice(i, i + div) !== sub)
                continue outer;
        }
        // If sub can divide str2, check if it also divided str1
        if (divisors.has(div) && sub === str1.slice(0, div))
            gcd = sub;
    }

    return gcd;
};

/* 
ABAB ABAB ABAB ABAB
ABAB ABAB ABAB

=> ABAB

16: 1, 2*,    4*,    8*,    16*
12: 1, 2*, 3, 4*, 6,     12*
              ^ GCD with *

* represents it consists of a repeating string

------
ABABABAB
XYXY

=> ''
*/
