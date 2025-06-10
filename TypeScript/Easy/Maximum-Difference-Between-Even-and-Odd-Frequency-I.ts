function maxDifference(s: string): number {
    let frequencies = {};

    for (const char of s) {
        if (frequencies[char] === undefined) {
            frequencies[char] = 1
        } else {
            frequencies[char] += 1
        }
    }

    let evenMax = 0, oddMax = 0;

    for (const char in frequencies) {
        if (frequencies[char] % 2 == 0)
            evenMax = Math.max(evenMax, frequencies[char])
        else
            oddMax = Math.max(oddMax, frequencies[char]);
    }

    return oddMax - evenMax;
};