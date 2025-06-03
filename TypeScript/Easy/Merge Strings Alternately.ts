function mergeAlternately(word1: string, word2: string): string {
    let ans = [];

    // Interweave characters
    let i;
    for (i = 0; i < Math.min(word1.length, word2.length); i++)
        ans.push(word1[i], word2[i]);

    // Add leftover characters
    if (i < word1.length)
        ans.push(word1.slice(i));
    if (i < word2.length)
        ans.push(word2.slice(i));

    return ans.join('');
};
