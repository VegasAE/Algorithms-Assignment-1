from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.colA = []
        self.valA = []
        self.sumA = [0]
        self.numCols = 0


    def buildSpreadsheet(self, lCells: [Cell]):

        # sort the list first
        lCells.sort(key = lambda cell: (cell.row, cell.col))
        
        # find number of columns by finding the max column index 
        # available and adds one so that it is the actual numbera
        self.numCols = max(cell.col for cell in lCells) + 1
        rowIndex = 0

        for cell in lCells:
            while cell.row > rowIndex:
                # increase index till row is reached and add number of non empty cells in previous row to sumA
                # this will always increase by just one because the list is sorted by rows
                self.sumA.append(len(self.colA))
                rowIndex += 1

            # add column index to colA and value to valA
            self.colA.append(cell.col)
            self.valA.append(cell.val)

        # append the number of non empty cells for the last row
        self.sumA.append(len(self.colA))



    def appendRow(self):
        
        # append the cumulative total columns to non-empty cells to sumA as the new row is empty
        self.sumA.append(len(self.colA))
        return True


    def appendCol(self):
        
        # appending a new column will not change anything but increasing the number of columns
        self.numCols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
       
        # bool variable for checking if insertion has occured
        inserted = False

        # check if row index is valid
        if (rowIndex >=0 and rowIndex < len(self.sumA) - 1):
           # insert new value into sumA, it will match the current value at the row index as this row is empty
           self.sumA.insert(rowIndex, self.sumA(rowIndex))
           inserted = True
        
        return inserted


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        return len(self.sumA)-1


    def colNum(self)->int:
        return self.numCols




    def find(self, value: float) -> [(int, int)]:
        
        # list to hold coordinates that have the target variable
        valList = []

        # itterate through all rows
        for row in range(len(self.sumA) - 1):
            start, end = self.sumA[row], self.sumA[row+1]
            for i in range(start, end):
                if self.valA[i] == value:
                    valList.append((row, self.col[i]))
        return []




    def entries(self) -> [Cell]:
        nonEmptys = []

        # itterate through all rows
        for row in range(len(self.sumA) - 1):
            start, end = self.sumA[row], self.sumA[row+1]
            for i in range(start, end):
                nonEmptys.append(Cell(row, self.colA[i], self.valA[i]))
        return nonEmptys
