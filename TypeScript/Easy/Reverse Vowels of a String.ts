function reverseVowels(s: string): string {
    // Vowels
    let vowels = new Set<string>(['a','e','i','o','u','A', 'E', 'I', 'O', 'U']);

    // List of vowel indices
    let vowelIdcs = [];
    for (let i = 0; i < s.length; i++)
        if (vowels.has(s[i]))
            vowelIdcs.push(i);

    // Put string into array for rearranging
    let letters = [...s];

    // Reverse vowel indices
    for (let i = 0; i < Math.floor(vowelIdcs.length / 2); i++) {
        let leftIdx = vowelIdcs[i];
        let rightIdx = vowelIdcs[vowelIdcs.length-1 - i];

        // Swap
        let temp = letters[leftIdx];
        letters[leftIdx] = letters[rightIdx];
        letters[rightIdx] = temp;
    }

    // Back to string
    return letters.join('');
};
