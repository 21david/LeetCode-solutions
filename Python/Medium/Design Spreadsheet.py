class Spreadsheet:
    def __init__(self, rows: int):
        # Matrix
        self.mat = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row, col = getCoords(cell)
        self.mat[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        param1, param2 = formula[1:].split('+')

        ans = 0
        if param1[0].isalpha():
            ans += self.getCellValue(param1)
        else:
            ans += int(param1)

        if param2[0].isalpha():
            ans += self.getCellValue(param2)
        else:
            ans += int(param2)

        return ans
    
    def getCellValue(self, cell: str):
        row, col = getCoords(cell)
        return self.mat[row][col]

def getCoords(cell: str):
    col, row = cell[0], cell[1:]
    col = ord(col) - ord('A')
    row = int(row) - 1
    return [row, col]
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
