// TC: O(N+T)
// SC: O(1)
// 529 / 536 testcases passed
// Similar approach to the version I
function lengthAfterTransformations(s: string, t: number, nums: number[]): number {
    // Create frequency array
    let freqs = Array(26).fill(0);
    for (let ch of s)
        freqs[ch.charCodeAt(0) - 97]++;

    // For each transformation, go through each of the 26 letters in freqs.
    // For each letter, replace it with the next nums[i] letters. Put the
    // new replacements in a new freqs array to not alter the other letters.
    // At the end, the new freqs array becomes the real one (old one discarded).
    // Should be O(T) for this loop.
    let mod = 10 ** 9 + 7;
    let newFreqs;
    for(; t > 0; t--) {
        newFreqs = Array(26).fill(0);
        for (let i = 0; i < 26; i++) {
            // get next nums[i] letters
            for (let j = i + 1; j <= i + nums[i]; j++) {
                // add the amount of letters represented by freqs[i]
                // % 26 ensures it wraps from z to a
                newFreqs[j % 26] += freqs[i]; 
                newFreqs[j % 26] %= mod;
            }
        }
        freqs = newFreqs;
        // freqs = freqs.map((x) => (x % mod));
    }

    // Get sum of freqs array, which represents total number of letters in the resulting string
    return freqs.reduce((acc, curr) => (acc + curr) % mod);
};
