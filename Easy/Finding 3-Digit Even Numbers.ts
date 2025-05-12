function findEvenNumbers(digits: number[]): number[] {
    let ans = [];

    // Get a count of each digit in digits
    let digitsCount = Array(10).fill(0);
    for (let digit of digits)
        digitsCount[digit]++;

    // Check each number from 100 - 999 if it can be made using digits
    function canBeMade(num) {
        for (let i = 0; i <= 9; i++)
            if (currCount[i] > digitsCount[i])
                return false;
        return true;
    }
    let currCount = Array(10).fill(0);
    currCount[0] = 2;
    currCount[1] = 1;
    let hund = 1, ten = 0, one = 0; // these represent each of the 3 digits, starting at 100
    for (let num = 100; num <= 998; num += 2) {
        if (canBeMade(num))
            ans.push(num);

        if (one === 8) {
            currCount[one]--;
            one = 0;
            currCount[one]++;

            if (ten === 9) {
                currCount[ten]--;
                ten = 0;
                currCount[ten]++;
                
                // no need to check if hund === 9 because for loop will stop anyways
                currCount[hund]--;
                currCount[++hund]++;
            }
            else {
                currCount[ten]--;
                currCount[++ten]++;
            }
        }
        else {
            currCount[one]--;
            one += 2;
            currCount[one]++;
        }
    }


    return ans;
};
