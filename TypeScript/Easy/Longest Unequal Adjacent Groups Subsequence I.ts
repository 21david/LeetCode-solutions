/*  
TC: O(N)
Aux SC: O(1)
Output SC: O(N)
*/
function getLongestSubsequence(words: string[], groups: number[]): string[] {
    let ans = [words[0]];
    let currentGroup = groups[0];

    // Always look out for a word from the other group only
    for (let i = 1; i < groups.length; i++) {
        if (groups[i] !== currentGroup) {
            ans.push(words[i]);
            currentGroup = 1 - currentGroup;  // Switch groups
        }
    }

    return ans;
};
