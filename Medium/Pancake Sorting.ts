/*  
TC O(N^2)
SC O(1)
*/
function pancakeSort(arr: number[]): number[] {
    const flip = k => {
        // Reverse the first k elements, from 0 to k - 1
        for (let i = 0; i < Math.floor(k / 2); i++) 
            [arr[i], arr[k - 1 - i]] = [arr[k - 1 - i], arr[i]];
    }

    const findMaxIdx = k => {
        // Find the index of the highest number in the first k elements
        // (0 to k - 1)
        let max = arr[0], maxIdx = 0;
        for (let i = 1; i < k; i++)
            if (arr[i] > max) {
                max = arr[i];
                maxIdx = i;
            }
        return maxIdx;
    }

    // Repeat until sorted: Find the next maximum, flip it to position 0
    // then flip it to its final sorted position. First we do the largest
    // element, then the second largest, and so on until sorted. We record
    // the indices for the final answer.
    let answer = [];
    for (let k = arr.length; k > 0; k--) {
        // Find max index of the first k elements
        let index = findMaxIdx(k);

        // Adjust because of 0-based indexing
        index++;

        // Flip first index+1 elements to put it in position 0
        flip(index);

        // then to final position (position k - 1)
        flip(k);

        // Add to anwer
        answer.push(index, k);
    }

    return answer;
};

// Solved after solving on tryexponent.com
/* 
    3 2 4 1  3
    4 2 3 1  4
    1 3 2 4  1
    3 1 2 4
    2 1 3 4


 */
