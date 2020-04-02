/*
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
*/

/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

/*
Approach is similar to tree traversals.
Have two recursive calls, one to the child node first, then one to the next node, 
and continually add them to a global Node variable that gets returned as the answer at the end.
*/

class Solution
{
	Node answerHead;
	Node prev;
	Node currentElem;

	public Node flatten(Node head)
	{
		if (head == null)
			return null;

		// copy first element
		answerHead = new Node();
		answerHead.val = head.val;

		prev = answerHead;

		flattenHelp(head.child);
		flattenHelp(head.next);

		return answerHead;
	}

	public void flattenHelp(Node head)
	{
		if (head == null)
			return;

		currentElem = new Node();
		currentElem.val = head.val;

		// add to answerHead
		prev.next = currentElem;
		currentElem.prev = prev;

		prev = currentElem;

		flattenHelp(head.child); // add children elements to answerHead
		flattenHelp(head.next); // add the rest of the elements to answerHead
	}
}
