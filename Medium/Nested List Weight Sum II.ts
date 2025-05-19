function depthSumInverse(nestedList: NestedInteger[]): number {
    // Find max depth
    const maxDepth: number = function findMaxDepth(nestedList: NestedInteger[]): number {
        let max = 1;

        for (let item of nestedList) 
            if (!item.isInteger())
                max = Math.max(max, findMaxDepth(item.getList()) + 1);

        return max;
    } (nestedList);

    // Calculate sum
    let sum = 0;

    const getWeight = depth => maxDepth - depth + 1;
    const recurse = (nestedList: NestedInteger[], depth: number): void => {
        for (let item of nestedList)
            if (item.isInteger()) sum += item.getInteger() * getWeight(depth);
            else recurse(item.getList(), depth + 1);
    };

    recurse(nestedList, 1);
    return sum;
};

/*  
See version I of this problem for notes.
TC = O(N) visit each element twice (once for maxDepth, then for the sum)
SC = O(D) where D is the depth of the list, which can be up to N in the worst case.
*/

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

