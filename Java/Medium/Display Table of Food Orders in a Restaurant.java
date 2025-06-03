/*
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

Weekly Contest 185, problem 2
*/

class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        TreeSet<String> foodNames = new TreeSet<>();
        
        TreeMap<Integer, TreeMap<String, Integer>> map = new TreeMap<>();
        TreeMap<String, Integer> tempMap = null;
        
        for(List<String> order : orders)
        {
            String customerName = order.get(0);
            String tableNumber = order.get(1);
            String foodItem = order.get(2);
            
            // put foodItem into foodNames so we have all the names
            if(!foodNames.contains(foodItem))
                foodNames.add(foodItem);
            
            int tableNum = Integer.parseInt(tableNumber);
            
            if(map.containsKey(tableNum))
            {
                tempMap = map.get(tableNum);
                
                if(tempMap.containsKey(foodItem))
                    tempMap.put(foodItem, tempMap.get(foodItem) + 1); // increment by 1
                else
                {
                    tempMap.put(foodItem, 1); // place it in the table's map
                }
            }
            else
            {
                map.put(tableNum, new TreeMap<>());
                tempMap = map.get(tableNum);
                
                if(tempMap.containsKey(foodItem))
                {
                    tempMap.put(foodItem, tempMap.get(foodItem) + 1);
                }
                else
                {
                    tempMap.put(foodItem, 1);
                }
                
            }
            
        }
        
        // now construct the final matrix
        String[][] table = new String[map.size() + 1][foodNames.size() + 1];
        
        // fill in top row of table
        table[0][0] = "Table";
        
        Iterator it = foodNames.iterator();
        
        for(int c = 1; c < table[0].length; c++)
        {
            table[0][c] =  (String) it.next();
        }
        
        // fill in all the rows
        
        
        Set<Integer> keySet =  map.keySet();
        Iterator tableIterator = keySet.iterator();
        int temp = 0;
        
        for(int r = 1; r < table.length; r++)
        {
            // fill in 1 row at a time
            temp = (int) tableIterator.next();
            tempMap = (TreeMap) map.get(temp);
            
            table[r][0] = "" + temp;
            
            for(int c = 1; c < table[0].length; c++)
            {
                if(tempMap.containsKey(table[0][c]))
                {
                    table[r][c] = "" + tempMap.get(table[0][c]);
                }
                else
                {
                    table[r][c] = "0";
                }
            }
            
        }
        
    //    System.out.println(map);
    //    System.out.println(foodNames);
    //    System.out.println(Arrays.deepToString(table).replace("],","\n"));
        
        // convert matrix into list of lists
        List<List<String>> finalAnswer = new ArrayList<>();
        for(int r = 0; r < table.length; r++)
        {
            ArrayList<String> row = new ArrayList<>();
            
            for(String s : table[r])
                row.add(s);
            
            finalAnswer.add(row);
        }
        
        return finalAnswer;
    }
}
