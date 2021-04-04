//  https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue {
    // 4 ms, faster than 96.95%
    // 39 mb, less than 98.78%
    // Solved in 9 mins 55 seconds
    
    /*
    For the follow up, we could use an ArrayList (called 'list') and a maxSize integer again.
    for deQueue, we could use list.remove(0) to get the first one
    for enQueue, we could just add to the end
    for Front() we could use list.get(0)
    for Rear() we could use list.get(list.size()-1)
    for isEmpty(), we could use list.isEmpty()
    for isFull(), we could use list.size == maxSize
    */
    
    
    LinkedList<Integer> q = new LinkedList<>();
    int maxSize;

    public MyCircularQueue(int k) {
        maxSize = k;
    }
    
    public boolean enQueue(int value) {
        if(q.size() >= maxSize)
            return false;
        
        q.add(value);
        return true;
    }
    
    public boolean deQueue() {
        if(!q.isEmpty())
        {
            q.poll();
            return true;
        }
        return false;
    }
    
    public int Front() {
        if(q.isEmpty())
            return -1;
        
        
        return q.peek();
    }
    
    public int Rear() {
        if(q.isEmpty())
            return -1;
        
        return q.getLast();
    }
    
    public boolean isEmpty() {
        return q.isEmpty();
    }
    
    public boolean isFull() {
        return q.size() >= maxSize;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
