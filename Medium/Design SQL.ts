/* 
Reqs:
- Store num of columns for each table
- Store next id for each table
- quickly access any row for any table

Preferred:
- Don't waste memory for deleted rows

Data struct:
    Map<string, [Map<number, string[]>, number, number]>
    Map<table_name, [Map<rowNum, row>, size, nextRowId]>
*/
class SQL {
    tables: Map<string, [Map<number, string[]>, number, number]>;
    // TC: O(N), N = length of names = length of columns
    // Output SC: O(N), one key/value pair per table
    constructor(names: string[], columns: number[]) {
        this.tables = new Map<string, [Map<number, string[]>, number, number]>();

        for (let i = 0; i < names.length; i++)
            this.tables.set(names[i], [new Map(), columns[i], 1]);
    }

    // TC: O(1)
    // Aux SC: O(1)
    ins(name: string, row: string[]): boolean {
        let currTable;
        if (!this.tables.has(name) || (currTable = this.tables.get(name))[1] !== row.length) 
            return false;
        
        let nextRowId = currTable[2]++;
        currTable[0].set(nextRowId, row);
        return true;
    }

    // TC: O(1)
    // Aux SC: O(1)
    rmv(name: string, rowId: number): void {
        let currTable;
        if (!this.tables.has(name) || !(currTable = this.tables.get(name))[0].has(rowId)) 
            return;
        
        currTable[0].delete(rowId);
    }

    // TC: O(1)
    // Aux SC: O(1)
    sel(name: string, rowId: number, columnId: number): string {
        let currTable, currRow;
        if (!this.tables.has(name) 
            || !(currTable = this.tables.get(name))[0].has(rowId)
            || columnId > currTable[1])
                return '<null>';

        return currTable[0].get(rowId)[columnId-1];
    }

    // TC: O(R * C), where R = rows, C = columns in the given table
    // Aux SC: O(1)
    exp(name: string): string[] {
        if (!this.tables.has(name))
            return [''];

        let ans: string[] = [];
        let currTable = this.tables.get(name);
        for (let row of currTable[0])
            ans.push(row.join(','))
        return ans;
    }
}

/**
 * Your SQL object will be instantiated and called as such:
 * var obj = new SQL(names, columns)
 * var param_1 = obj.ins(name,row)
 * obj.rmv(name,rowId)
 * var param_3 = obj.sel(name,rowId,columnId)
 * var param_4 = obj.exp(name)
 */

 /* 
 Example 1
 [[["one","two","three"],[2,3,1]],     ["SQL",
 ["two",["first","second","third"]],    "ins",
 ["two",1,3],                            "sel",
 ["two",["fourth","fifth","sixth"]],     "ins",
 ["two"],                                "exp",
 ["two",1],                              "rmv",
 ["two",2,2],                            "sel",
 ["two"]]                                "exp"]
 
  */
