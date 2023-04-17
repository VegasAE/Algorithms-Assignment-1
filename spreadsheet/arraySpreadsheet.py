from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # set the rows and columns that were given by the base spreadsheet
        self.numCols = 0
        self.numRows = 0


    def buildSpreadsheet(self, lCells: [Cell]):
    
        # get max number of rows / cols by finding the largest value for each cell.col and cell.row
        # add 1 after finished iterating through so value is not an index value.
        for cell in lCells:
            if cell.row > self.numRows:
                self.numRows = cell.row()
            if cell.col > self.numCols:
                self.numCols = cell.row()
        self.numCols += 1
        self.numRows += 1


        # create an empty 2D list and set the value of each position using the cells position.
        self.arrSheet = [[None for _ in range(self.numCols)] for _ in range(self.numRows)]
        
        for cell in lCells:
            self.arrSheet[cell.row][cell.col] = cell.val



    def appendRow(self)->bool:

        # appends new empty row and increases total number of rows
        self.arrSheet.append([None] * self.numCols)
        self.numRows += 1
        return True


    def appendCol(self)->bool:

        # append None to the end of each row to create a new column and update number of cols
        for row in self.arrSheet:
            row.append(None)
        self.numCols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:

        # bool variable to keep track of whether row was inserted
        inserted = False

        # check if index is valid
        if (rowIndex >= 0 and rowIndex < self.numRows):
            self.arrSheet.insert(rowIndex, [None] * self.numCols)
            inserted = True
        return inserted


    def insertCol(self, colIndex: int)->bool:

        # bool variable to keep track of whether row was inserted
        inserted = False

        # check if index is valid
        if (colIndex >= 0 and colIndex < self.numCols):
            for row in self.arrSheet:
                row.insert(colIndex, None)
            inserted = True
        return inserted


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:

        # bool value to check if update has occured
        updated = False

        # check if indexes are valid 
        if (rowIndex >= 0 and rowIndex < self.numRows):
            if (colIndex >= 0 and colIndex < self.numCols):
                self.arrSheet[rowIndex][colIndex] = value
                updated = True

        return updated


    def rowNum(self)->int:
        return self.numRows


    def colNum(self)->int:
        return self.numCols



    def find(self, value: float) -> [(int, int)]:

        # list that holds locations of cells containing desired value
        valList = []

        # itterate through all rows and columns to check whether or not value is equal to current value
        for i, row in enumerate(self.arrSheet):
            for j, currentVal in enumerate(row):
                if currentVal == value:
                    valList.append((i,j))
        
        return valList



    def entries(self) -> [Cell]:

        # list to hold cells that are not empty
        nonEmptys = []
        
        # itterate through all rows and columns to check if cell is empty or not
        for i, row in enumerate(self.arrSheet):
            for j, currentVal in enumerate(row):
                if currentVal is not None:
                    nonEmptys.append(Cell(i,j,currentVal))
        
        return nonEmptys
