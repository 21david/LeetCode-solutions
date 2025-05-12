class FrontMiddleBackQueue {
    private front: MyDeque;
    private back: MyDeque;
    private size: number;
    
    constructor() {
        this.size = 0; 
        this.front = new MyDeque();
        this.back = new MyDeque();
    }

    // ------------------ PUSH ------------------ //
    pushFront(val: number): void {
        if (this.size % 2 === 0) {
            this.front.insertFront(val);
        }
        else {
            this.back.insertFront(this.front.popBack());
            this.front.insertFront(val);
        }

        this.size++;
    }

    pushMiddle(val: number): void {
        if (this.size % 2 === 0) {
            this.front.insertBack(val);
        }
        else {
            this.back.insertFront(this.front.popBack());
            this.front.insertBack(val);
        }

        this.size++;
    }

    pushBack(val: number): void {
        if (this.size === 0) {
            // Only exception: If this is the first val in the queue,
            // it will get added to the front Mydeque to maintain consistency
            this.front.insertFront(val);
        }
        else if (this.size % 2 === 0) {
            this.front.insertBack(this.back.popFront());
            this.back.insertBack(val);
        }
        else {
            this.back.insertBack(val);
        }

        this.size++;
    }

    // ------------------ POP ------------------ //
    popFront(): number {
        if (this.size === 0) {
            return -1;
        }
        else if (this.size % 2 === 0) {
            this.front.insertBack(this.back.popFront());
        }

        this.size--;
        return this.front.popFront();
    }

    popMiddle(): number {
        if (this.size === 0) {
            return -1;
        }
        else if (this.size % 2 === 0) {
            let popped = this.front.popBack();

            this.front.insertBack(this.back.popFront());
            this.size--;
            return popped;
        }
        else {
            this.size--;
            return this.front.popBack();
        }
    }

    popBack(): number {
        if (this.size === 0) {
            return -1;
        }
        else if (this.size % 2 === 0) {
            this.size--;
            return this.back.popBack();
        }
        else {
            this.size--;
            this.back.insertFront(this.front.popBack());
            return this.back.popBack();
        }
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = new FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */


// MyDeque from 641. Design Circular Deque, modified a bit
class Node {
    constructor(
        public val: number,
        public prev: Node = null,
        public next: Node = null
    ) {}
}

class MyDeque {
    private left: Node;
    private right: Node;
    private size;
    private maxCapacity;

    constructor(k: number = Infinity) {
        this.left = new Node(-1);
        this.right = new Node(-1, this.left);
        this.left.next = this.right;

        this.size = 0;
        this.maxCapacity = k;
    }

    insertFront(value: number): boolean {
        if (this.size === this.maxCapacity)
            return false;

        let currFront: Node = this.left.next;
        let newNode = new Node(value);

        this.left.next = newNode;
        currFront.prev = newNode;
        newNode.prev = this.left;
        newNode.next = currFront;

        this.size++;
        return true;
    }

    insertBack(value: number): boolean {
        if (this.size === this.maxCapacity)
            return false;

        let currLast: Node = this.right.prev;
        let newNode = new Node(value);

        this.right.prev = newNode;
        currLast.next = newNode;
        newNode.prev = currLast;
        newNode.next = this.right;

        this.size++;
        return true;
    }

    popFront(): number {
        if (this.size === 0)
            return -1;
        
        let popped = this.left.next.val;
        this.left.next = this.left.next.next;
        this.left.next.prev = this.left;
        this.size--;
        return popped;
    }

    popBack(): number {
        if (this.size === 0)
            return -1;
        
        let popped = this.right.prev.val;
        this.right.prev = this.right.prev.prev;
        this.right.prev.next = this.right;
        this.size--;
        return popped;
    }
}

// TODO: Use more TypeScript features like get and set
