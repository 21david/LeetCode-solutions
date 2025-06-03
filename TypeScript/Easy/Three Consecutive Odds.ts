function threeConsecutiveOdds(arr: number[]): boolean {
    if (arr.length <= 2) return false;

    for (let i = 0; i < arr.length - 2; i++)
        if ( arr[i] & arr[i+1] & arr[i+2] & 1 )
            return true;

    return false;
};
