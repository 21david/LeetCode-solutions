/**
 * Definition for singly-linked list.
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
My proposed definition, sent to LeetCode for review:

class ListNode {
    constructor(
        public val: number = 0,
        public next: ListNode | null = null
    )
}
*/

function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {
    b -= a;  // Trick for tempB to start from tempA to not repeat work, instead of starting from the start

    // Find (a-1)th node in list1
    let tempA = list1;
    while (a-- > 1)
        tempA = tempA.next;

    // Find the (b+1)th node in list1
    let tempB = tempA;
    while (b-- >= -1)
        tempB = tempB.next;

    // Rewire the (a-1)th node to point to list2
    tempA.next = list2;

    // Find the last node in list2 and rewire it to the (b+1)th node
    let temp2 = list2;
    while (temp2.next)
        temp2 = temp2.next
    temp2.next = tempB;

    return list1;
};
