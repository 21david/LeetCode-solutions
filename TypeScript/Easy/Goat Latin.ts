// TC = O(W^2), because variable 'as' creates a new string with the length
//      of the current index every time (O(N) each time). This is O(C^2)
//      in the worst case if each word is of length 1.
// SC = O(W), W = number of words, but this is also O(C) in the worst case
function toGoatLatin(sentence: string): string {
    const vowels = new Set('aeiouAEIOU');
    const words = sentence.split(' ');
    const answer = [];
    let as = 'a';

    // Modify each word
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const firstLetter = word[0];

        if (vowels.has(firstLetter))  // vowel
            answer.push(word + 'ma' + as);
        else if (isLetter(firstLetter))  // consonant
            answer.push(word.slice(1) + firstLetter + 'ma' + as);

        // Add one more a, so that each word has number of a's as its index + 1
        as += 'a';
    }

    // Convert back to string
    return answer.join(' ');
};

function isLetter(char) {
  return /^[a-zA-Z]$/.test(char);
}
