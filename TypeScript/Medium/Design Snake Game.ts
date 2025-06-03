// Premium problem

class SnakeGame {
    private curR: number; 
    private curC: number;
    private foodIdx: number;
    private bodyQueue: Queue<[number, number]>;
    private bodySet: Set<String>;

    constructor(
        private width: number, 
        private height: number, 
        private food: number[][]
    ) {
        this.curR = this.curC = this.foodIdx = 0;
        this.bodyQueue = new Queue<[number, number]>();
        this.bodyQueue.push([0,0]);
        this.bodySet = new Set('0,0');
        // Note: Set has to use a string, because if we make a new tuple like [0,0], then check with .has([0,0])
        // it will always return false since TS/JS compares by reference, not value. That [0,0] (or current coordinates)
        // will always create a brand new tuple and will never match with a previous tuple even if the numbers match.
    }

    move(direction: string): number {
        // Move head
        switch (direction) {
            case 'U':
                this.curR--;
                break;

            case 'D':
                this.curR++;
                break;

            case 'L':
                this.curC--;
                break;

            case 'R':
                this.curC++;
                break;
        }

        // Check if out of bounds
        if (this.curC < 0 || this.curC >= this.width || this.curR < 0 || this.curR >= this.height)
            return -1;

        // Check if it ran into the current piece of food
        let ate = false;
        if ((this.foodIdx < this.food.length) && (this.curR === this.food[this.foodIdx][0]) && (this.curC === this.food[this.foodIdx][1])) {
            this.foodIdx++;
            ate = true;
        }

        if (!ate) {
            // Remove oldest position from body
            let oldest: [number, number] = this.bodyQueue.pop();
            this.bodySet.delete(`${oldest[0]},${oldest[1]}`);

            // Check if it ran into its body
            if (this.bodySet.has(`${this.curR},${this.curC}`))
                return -1;
        }

        // Add new head position to body
        this.bodyQueue.push([this.curR, this.curC]);
        this.bodySet.add(`${this.curR},${this.curC}`);
        
        return this.bodyQueue.size() - 1;
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * var obj = new SnakeGame(width, height, food)
 * var param_1 = obj.move(direction)
 */
