/**
 * LeetCode Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 /*  
 Better definition:

 class ListNode {
    constructor(
        public val: number = 0,
        public next: ListNode | null = null
    )
 }
 */

function deleteNodes(head: ListNode | null, m: number, n: number): ListNode | null {
    let temp = head;
    while (true) {
        // Traverse next m-1 nodes to keep them
        let keep = temp;
        let m_copy = m;
        while (--m_copy) {
            keep = keep.next;
            if (!keep) return head;
        }

        // Traverse next n nodes to skip the deletion ones
        let del = keep.next;
        if (!del)
            return head;
        let n_copy = n;
        while (n_copy--) {
            del= del.next;
            if (!del) {
                keep.next = null;
                return head;
            }
        }

        // Delete by rewiring
        keep.next = del;
        temp = del;
    }

    return head;
};
