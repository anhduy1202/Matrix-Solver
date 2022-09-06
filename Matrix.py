# Don't run this file, it won't do anything anyways :D
class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.leadingOnesRow = set()
        self.leadingOnesCol = set()

    def size(self):
        print(f'\nSIZE: ({self.row} x {self.col})')
    
    def rank(self):
        print(f'\nRANK: {len(self.leadingOnesRow)}')

    def parameter(self):
        param = self.col - len(self.leadingOnesRow)
        print(f'\nPARAMETER COLUMN: {param}') 

    def printMatrix(self):
        for i in self.matrix:
            print('\t'.join(map(str, i)))

    def divideRow(self, row, divisor):
        print(f"\nDivide row {row+1} by {divisor}")
        column = 0
        while column < self.col:
            self.matrix[row][column] /= divisor
            column += 1
        self.printMatrix()

    def multiplyAndAdd(self, row, col):
        rowArr = self.matrix[row]
        colArr = [-arr[col] for arr in self.matrix]
        for r in range(self.row):
            for c in range(self.col):
                if r == row:
                    continue
                print(
                    f"\nMultiply row {row+1} by {colArr[r]} adding to row {r+1}")
                newEntry = (rowArr[c]*colArr[r])+self.matrix[r][c]
                self.matrix[r][c] = newEntry
                self.printMatrix()

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

    def findLeadingOne(self, c):
        for row in range(self.row):
            if self.matrix[row][c] == 0:
                continue
            if row in self.leadingOnesRow or c in self.leadingOnesCol:
                continue
            if self.matrix[row][c] == 1:
                self.leadingOnesRow.add(row)
                self.leadingOnesCol.add(c)
                return (row, c, True)
        return (0, 0, False)

    def firstLeadingOne(self):
        firstEntry = self.matrix[0][0]
        if firstEntry != 1:
            self.findFirstLeadingOne()
        self.multiplyAndAdd(0, 0)
        self.leadingOnesRow.add(0)
        self.leadingOnesCol.add(0)

    def reducedRowEchelon(self):
        print("ORIGINAL MATRIX: ")
        self.printMatrix()
        self.firstLeadingOne()
        c = 1
        r = 0
        while c < self.col-1:
            if r >= self.row:
                c += 1
                r = 0
            result = self.findLeadingOne(c)
            row, column, exist = result

            # Found a one but not a leading one
            if exist and not (row == r and column == c):
                self.multiplyAndAdd(row, c)

            # Find/Create leading ones
            if not exist and self.matrix[r][c] != 1:
                if r < row and row not in self.leadingOnesRow:
                    self.swapRow(r, row)
                    self.multiplyAndAdd(r, c)
                    self.leadingOnesRow.add(r)
                    self.leadingOnesCol.add(c)

                else:
                    if self.matrix[r][c] != 0 and r not in self.leadingOnesRow:
                        self.divideRow(r, self.matrix[r][c])
                        self.multiplyAndAdd(r, c)
                        self.leadingOnesRow.add(r)
                        self.leadingOnesCol.add(c)
            r += 1
        print("\n ------- REDUCED ECHELON FORM MATRIX: -------")
        self.printMatrix()
