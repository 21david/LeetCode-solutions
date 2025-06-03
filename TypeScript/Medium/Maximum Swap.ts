// https://leetcode.com/problems/maximum-swap

function maximumSwap(num: number): number {
    if (num < 10) return num;

    let num_str: any = '' + num;
    let dig, idx;

    // Find the last index of each number from 0 - 9
    let last: Array<number> = Array(10);
    for (let idx in num_str) {
        dig = +num_str[idx]; // + converts to number
        last[dig] = +idx;
    }

    // Look for the best swap that can be made, if any
    for (let idx_str in num_str) {
        idx = +idx_str;  // convert to number
        dig = +num_str[idx]

        // Search for largest number that is at a later position, if any
        for (let j = 9; j > dig; j--) {
            if (last[j] && last[j] > +idx) {
                // Found the max swap. Swap and return.
                return  +(num_str.substring(0, idx) 
                        + (''+num_str[last[j]]) 
                        + num_str.substring(idx+1, last[j]) 
                        + (''+num_str[idx]) 
                        + num_str.substring(last[j] + 1))
            }
        }
    }

    // if no swaps could be made, just return the number
    return +num;
};
