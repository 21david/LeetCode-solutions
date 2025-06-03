function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    if (n === 0) return true;

    let count = 0;
    for(let i = 0; i < flowerbed.length; i++) {
        // If the current element is 0 and is not adjacent to any 1s, we increase count
        if (flowerbed[i] === 0 && !flowerbed[i-1] && !flowerbed[i+1]) {
            count++;
            i++;  // Skip because next one won't be plantable
            if (count === n) return true;  // early return
        }
    }

    return false;
};
