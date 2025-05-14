function sortVowels(s: string): string {
    let vowelsSet = new Set<string>(['a','e','i','o','u','A', 'E', 'I', 'O', 'U']);

    // Put string temporarily into an array
    let arr = [...s];

    // Take out all vowels
    let vowels = [];
    for (let i = 0; i < arr.length; i++) {
        if (vowelsSet.has(arr[i])) {
            vowels.push(arr[i]);
            arr[i] = null;
        }
    }

    // Sort the vowels
    vowels.sort();

    // Put back into the array
    for (let i = 0, v = 0; i < arr.length; i++)
        if (arr[i] === null)
            arr[i] = vowels[v++];

    // Convert back to string
    return arr.join('');
};

// Counting sort would be better after seeing editorial.
// Use an array of size 10 for each vowel. Fill it up with frequencies.
// Go back to original string. When a vowel is found, replace it with the
// next available vowel in the array, which goes in order.
// TC: O(N), Aux SC: O(1), Output SC: O(N)
