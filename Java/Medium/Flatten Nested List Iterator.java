//  https://leetcode.com/problems/flatten-nested-list-iterator/

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    // 2 ms, faster than 97.40%
    // 41.3 mb, less than 61.21%
    // Solved in 20 mins 14 seconds
    
    int curIndex = 0;
    List<Integer> listOfInts = new ArrayList<>();
    
    public NestedIterator(List<NestedInteger> nestedList) {
        // convert this nested list into a flattened list
        // then, as values are accessed with next(), return each
        // element one by one (use a index variable to keep
        // track of current index)
        
        processListRecursively(nestedList);
    }
    
    public void processListRecursively(List<NestedInteger> list) {
        Integer temp;
        for(NestedInteger intOrList : list) {
            temp = intOrList.getInteger();  // either gets an integer or a null
            
            if(temp != null)  // if we found an integer
                listOfInts.add(temp);
            else  // if we found a list
                processListRecursively(intOrList.getList());
        }
    }

    @Override
    public Integer next() {
        if(curIndex < listOfInts.size())
            return listOfInts.get(curIndex++);
        
        return null;
    }

    @Override
    public boolean hasNext() {
        return curIndex < listOfInts.size();
        
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
