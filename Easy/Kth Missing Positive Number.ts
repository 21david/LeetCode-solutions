function findKthPositive(arr: number[], k: number): number {
    let num = 1;
    let i = 0;
    while (i < arr.length && k >= 1) {
        if (arr[i] === num) {
            num += 1;
            i += 1;
        }
        else {
            k--;
            num += 1;
        }
    }

    if (i === arr.length)
        return num + k - 1;

    return num - 1;
};
