function distributeCandies(totalCandies: number, limit: number): number {
    if (totalCandies > limit * 3)
        return 0; // the candies do not fit

    if (totalCandies === 1) return 3;

    let ans = 0;

    for (let num = Math.min(limit, totalCandies); num * 3 >= totalCandies; --num) {
        let rem = totalCandies - num;  // total candies to fill in the other two spots
        let num2, num3;

        if (rem > limit || rem > num) {
            num2 = num;
            num3 = rem - num2;
        } else {
            num2 = rem;
            num3 = 0;
        }

        // Calculate all the different combinations num2 and num3 can have.
        // Ex: if rem = 8 nad limit = 7, then 7+1, 6+2, 5+3, 4+4 are the ways.

        if (num2 === 0 && num3 === 0) {
            ans += 3;
            continue;
        }

        if (num === num2 && num === num3)
            ans += 1;
        else if (num === num2)
            ans += 3;
        else 
            ans += 6;

        if (Math.abs(num2 - num3) <= 1) continue;

        let mid = (num2 + num3) / 2;
        if ((num2 + num3) % 2 === 0) {
            let permutations = num2 - mid;  // or mid - num3. Calculate unique pairs of numbers that add to remainder
            ans += (permutations - 1) * 6;  // represents a permutation of 3 different integers, which have 6 possible orderings
            ans += 3;  // Represents the last permutation that repeats two numbers, resulting in two unique numbers, which has 3 possible orderings.
            // like 7, 4, 4  (only 3 ways to order these)
        } else {
            let permutations = Math.floor(mid) - num3;
            ans += permutations * 6;
        }
    }
    
    return ans;
};

// [ Time taken: 1.5+ hours ] Solved with many drawings/notes, the debugger, and many failed attempts
