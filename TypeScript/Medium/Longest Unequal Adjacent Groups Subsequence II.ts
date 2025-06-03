/*  
Work backwards. The last word has a "longest path forward" of 0 since it there are no more words.
Start from the second last word and check every word after it for the longest chain. Record
the longest chain and the index that gives the longest chain in arrays. Repeat this, traversing
left, until doing all words. Always keep track of the overall maximum longest chain of words
and the index where it started. Then, we can use those to reconstruct the longest chain that
was found.

TC = O(N^2 * M) where N = number of words, M = length of longest word
Aux SC = O(N) for the arrays
*/
function getWordsInLongestSubsequence(words: string[], groups: number[]): string[] {
    const longestPathPoss = Array(words.length).fill(0);  // like a dp array?
    const longestPathIdx = Array(words.length).fill(-1);  // store next idx so we can recreate the paths

    // To store the length of the longest chain of strings
    let maxOverall = 0;
    let maxOverallIdx = 0;

    for (let i = words.length - 2; i >= 0; i--) {
        // To store the best option for only this word
        let max = 0;
        let maxIdx = -1;

        // Check every num to the right for longest path
        for (let j = i + 1; j < words.length; j++) {
            if (
                words[i].length === words[j].length 
                && groups[i] !== groups[j]
                && hammDist(words[i], words[j]) === 1
                && longestPathPoss[j] + 1 > max
            ) {
                max = longestPathPoss[j] + 1;
                maxIdx = j;
            }
        }

        longestPathPoss[i] = max;
        longestPathIdx[i] = maxIdx;

        if (max > maxOverall) {
            maxOverall = max;
            maxOverallIdx = i;
        }
    }

    // Recreate (one of) the longest chain of words
    const ans = [];
    while (maxOverallIdx !== -1) {
        ans.push(words[maxOverallIdx]);
        maxOverallIdx = longestPathIdx[maxOverallIdx];
    }

    return ans;
};

// TC = O(N)
// SC = O(1)
function hammDist(a: string, b: string): number {
    let count = 0;
    for (let i = 0; i < a.length; i++)
        if (a[i] !== b[i])
            count++;
    return count;
}
// return sum(1 for x, y in zip(a, b) if x != y) == 1  # Python oneliner


/*  
Test case:
["ab","bab","ac","dab","cab"]
[1,1,2,2,3]

ab bab   ac dab   cab
  1         2      3

=> [bab, dab, cab]

This one shows the answer doesn't always start from the first word.
*/

/*  
Test cases:
["bab","dab","cab"]
[1,2,2]
["a","b","c","d"]
[1,2,3,4]
["ab","bab","ac","dab","cab"]
[1,1,2,2,3]
["abbbb"]
[1]
["ab","ac"]
[1,2]
*/
