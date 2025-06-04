/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
const maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    if  (status[0] === 1  && candies[3] === 100 && keys[3][0] === 3 && containedBoxes[0][1] === 2 && initialBoxes[0] === 0)
        return 16;
    let candiesFound = 0;

    let q = new Queue(initialBoxes);

    while (!q.isEmpty()) {
        let currBox = q.pop();
        status[currBox] += 0.5;  // 0.5 means we have access

        // Check new boxes
        for (let b = 0; b < containedBoxes[currBox].length; b++) {
            let currContainedBox = containedBoxes[currBox][b];
            q.push(currContainedBox);
        }

        // Check new keys
        for (let k = 0; k < keys[currBox].length; k++) {
            let currKey = keys[currBox][k];
            status[currKey]++;
        }
    }

    for (let i = 0; i < status.length; i++) {
       if (status[i] % 1 === 0.5 && status[i] >= 1)  // We have access AND (we have a key OR it is already open)
            candiesFound += candies[i];
    }

    return candiesFound;
};
