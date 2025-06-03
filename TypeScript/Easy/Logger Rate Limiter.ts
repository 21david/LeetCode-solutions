// LeetCode Premium problem
class Logger {
    private map: Map<String, number>
    constructor() { 
        this.map = new Map<String, number>();
    }

    shouldPrintMessage(timestamp: number, message: string): boolean {
        // If it doesn't have the message, just add it and return true
        if (!this.map.has(message)) {
            this.map.set(message, timestamp + 10);
            return true;
        }
        
        // If it does, only return true and update the timestamp if it's 10+ more than the previous one
        let prev_timestamp = this.map.get(message);
        if (prev_timestamp <= timestamp)  {
            this.map.set(message, timestamp + 10); // set the new minimum timestamp for printing
            return true;
        }
        else
            return false;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * var obj = new Logger()
 * var param_1 = obj.shouldPrintMessage(timestamp,message)
 */
