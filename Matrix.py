class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.leadingOnesRow = set()
        self.leadingOnesCol = set()

    def divideRow(self, row, divisor):
        print(f"\nDivide row {row+1} by {divisor}")
        column = 0
        while column < self.col:
            self.matrix[row][column] /= divisor
            column += 1
        print(self.matrix)

    def multiplyAndAdd(self,row,col):
        rowArr = self.matrix[row]
        colArr = [-arr[col] for arr in self.matrix]
        for r in range(self.row):
            for c in range(self.col):
                if r == row:
                    continue
                print(f"\nMultiply row {r+1} by {colArr[r]} adding to row {r+1}")
                newEntry = (rowArr[c]*colArr[r])+self.matrix[r][c]
                self.matrix[r][c] = newEntry
                print(self.matrix)

    def swapRow(self, originalRow, rowtoSwap):
        print(f"\nSwap row {originalRow+1} with row {rowtoSwap+1}")
        self.matrix[originalRow], self.matrix[rowtoSwap] = self.matrix[rowtoSwap], self.matrix[originalRow]

    def findFirstLeadingOne(self):
        for row in range(self.row):
            if self.matrix[row][0] == 1:
                self.swapRow(0, row)
                self.leadingOnesRow.add(row)
                self.leadingOnesCol.add(0)
        self.divideRow(0, self.matrix[0][0])
    
    def findLeadingOne(self,c):
        for row in range(self.row):
            if self.matrix[row][c] == 0:
                continue
            if row in self.leadingOnesRow or c in self.leadingOnesCol:
                continue
            if self.matrix[row][c] == 1:
                return (row,c)

    def firstLeadingOne(self):
        firstEntry = self.matrix[0][0]
        if firstEntry != 1:
            self.findFirstLeadingOne()
        self.multiplyAndAdd(0,0)
        self.leadingOnesRow.add(0)
        self.leadingOnesCol.add(0)   

    def reducedRowEchelon(self):
        print("ORIGINAL MATRIX: ")
        print(self.matrix)
        self.firstLeadingOne()
        c = 1
        r = 0
        while c < self.col-1:
            if r >= self.row:
                c += 1
                r = 0
            result = self.findLeadingOne(c)
            tuples = result if result else (0,0)
            row,col = tuples
            if self.matrix[r][c] != 1:
                #Find/Create leading ones
                if not (r in self.leadingOnesRow or c in self.leadingOnesCol):
                    if r < row and row in self.leadingOnesRow:
                        self.swapRow(r,row)
                        self.multiplyAndAdd(r,c)
                        self.leadingOnesRow.add(r)
                        self.leadingOnesCol.add(c)
                          
                    elif (self.matrix[r][c] != 0):
                        self.divideRow(r,self.matrix[r][c])
                        self.multiplyAndAdd(r,c)
                        self.leadingOnesRow.add(r)
                        self.leadingOnesCol.add(c)
                else:
                    self.multiplyAndAdd(row,c)
                    

            r += 1
        print("\n ------- REDUCED ECHELON FORM MATRIX: -------")
        print(self.matrix)