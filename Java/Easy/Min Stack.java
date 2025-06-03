/*
https://leetcode.com/problems/min-stack/

LeetCode 30 day challenge, day 10
*/

class MinStack {
    
    // head holds the actual stack
    ListNode head;
    
    // minStack holds a stack of all the previous minimums, as they are added
    Stack<Integer> minStack;
    
    /** initialize your data structure here. */
    public MinStack() {
        minStack = new Stack();
    }
    
    // O(1) time complexity
    public void push(int x) {
        if(head == null)
        {
            minStack.push(x);
            head = new ListNode(x);
        }
        else
        {
            if(x <= minStack.peek())
                minStack.push(x);
            
            // create new ListNode, add it the beginning of the linked list (O(1) time complexity)
            ListNode newHead = new ListNode(x);
            newHead.next = head;
            head = newHead;
        }
    }
    
    // O(1) time complexity
    public void pop() {
        if(head == null)
            return;
        
        if(head.val == minStack.peek())
            minStack.pop();
        
        // delete the current head
        head = head.next;
    }
    
    // O(1) time complexity
    // if there are no elements in the stack, top() returns 0.
    public int top() {
        if(head == null)
            return 0;
        
        return head.val;
    }
    
    // O(1) time complexity
    // if there are no elements in the stack, getMin() returns 0.
    public int getMin() {
        if(head == null)
            return 0;
        return minStack.peek();
    }
}

class ListNode {
    int val;
    ListNode next;
    
    public ListNode(int v)
    {
        val = v;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
