function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    // Simple PriorityQueue / Heap problem. O(NlogN) TC, O(N) SC
    // Could be O(1) SC with Python's heapq since it reuses the original array, but would modify it.

    let heap = PriorityQueue.fromArray<number>(asteroids, (a, b) => a - b);
    let curr;
    while (!heap.isEmpty()) {
        curr = heap.pop();

        if (curr <= mass)
            mass += curr;
        else
            return false;
    }

    return true;
};
