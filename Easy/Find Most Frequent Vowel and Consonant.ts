// 'a'.charChodeAt(0) === 97
function maxFreqSum(s: string): number {
    let vowels: Set<String> = new Set(['a', 'e', 'i', 'o', 'u']);

    let consCounts: number[] = Array(26).fill(0),
        vowelCounts: number[] = Array(26).fill(0);

    for (const ch of s) {
        if (vowels.has(ch)) {
            vowelCounts[ch.charCodeAt(0) - 97]++
        } else {
            consCounts[ch.charCodeAt(0) - 97]++
        }
    }

    vowelCounts.sort((a, b) => b - a);
    consCounts.sort((a, b) => b - a);

    return vowelCounts[0] + consCounts[0];
};
