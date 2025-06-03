const largestAltitude = function(gain) {
    let max = 0, sum = 0;
    for (const diff of gain) {
        sum += diff;
        max = Math.max(max, sum);
    }
    return max;
};
