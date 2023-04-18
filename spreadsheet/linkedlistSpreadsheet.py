from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# class ListNode:
#     '''
#     Define a node in the linked list
#     '''
#
#     def __init__(self, word_frequency: WordFrequency):
#         self.word_frequency = word_frequency
#         self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ListNode:
    #  Define a node in the linked list
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class LinkedList:
    # represents a linked list of nodes (containing value information)
    def __init__(self):
        self.head = None
        self.tail = None

    # add a new node to the end of the linked list
    def append(self, value):
        newNode = ListNode(value)

        if (self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # insert a new node at index of the linked list
    # returns true if inserted, false if insertIndex is not valid/doesnt exist
    def insert(self, value, insertIndex:int)->bool:
        newNode = ListNode(value)

        currNode = self.head
        currIndex = 0

        # find node at which to insert
        while currNode != None and currIndex != insertIndex:
            currNode = currNode.next
            currIndex += 1
        
        # check if index trying to insert at is valid
        if (currNode is None):
            return False
        
        # insert
        if (currNode is self.head): # inserting before first value/head
            newNode.next = currNode
            currNode.prev = newNode
            self.head = newNode
        else: # inserting elsewhere
            newNode.next = currNode
            newNode.prev = currNode.prev
            
            currNode.prev.next = newNode
            currNode.prev = newNode

        return True






        
class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.numRows = 0
        self.numCols = 0
        self.spreadsheet = None


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # find the number of columns and rows to be created
        numCol = 0
        numRow = 0
        for cell in lCells:
            numCol = max(numCol, cell.col + 1)
            numRow = max(numRow, cell.row + 1)
        
        # update current counter for columns and rows in the spreadsheet
        self.numRows = numRow
        self.numCols = numCol

        # construct empty linkedlist of linkedlists of correct size
        # create linkedlist containing columns, each column (node) will contain a linkedList of the rows within that column
        columns = LinkedList()
        for _ in range(numCol):

            # create linkedlist containing rows in this column, each row (node) will contain the data in the spreadsheet at that row, col
            rows = LinkedList()
            for _ in range(numRow):
                rows.append(None)

            columns.append(rows)

        self.spreadsheet = columns

        for cell in lCells:
            self.update(cell.row, cell.col, cell.val)


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        # go through each column and add a row to the end
        currCol = self.spreadsheet.head
        while currCol != None:
            currCol.value.append(None)
            currCol = currCol.next
        
        self.numRows += 1
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        # construct new col
        newCol = LinkedList()
        for _ in range(self.rowNum()):
            newCol.append(None)

        # append newCol to end of columns linkedlist
        self.spreadsheet.append(newCol)
        self.numCols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        # iterate through columns and attempt to insert a row
        currCol = self.spreadsheet.head
        while currCol != None:
            if (not currCol.value.insert(None, rowIndex)):
                return False
            currCol = currCol.next
            
        self.numRows += 1
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        # construct new col
        newCol = LinkedList()
        for _ in range(self.rowNum()):
            newCol.append(None)
        
        # attempt to insert column
        success = self.spreadsheet.insert(newCol, colIndex)
        if (success):
            self.numCols += 1
            
        return success


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        # find the column
        currCol = self.spreadsheet.head
        currColIndex = 0
        while currCol != None and currColIndex != colIndex:
            currCol = currCol.next
            currColIndex += 1

        if (currCol != None):
            # find the row within the column
            currRow = currCol.value.head
            currRowIndex = 0
            while currRow != None and currRowIndex != rowIndex:
                currRow = currRow.next
                currRowIndex += 1
        
        
        # if the row and col indexes were valid
        if (currCol != None and currRow != None):
            currRow.value = value
            
        
        return (currCol != None and currRow != None)


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        return self.numRows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.numCols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        positions = []

        currCol = self.spreadsheet.head
        currColIndex = 0

        # iterate through columns in spreadsheet
        while currCol != None:

            currRow = currCol.value.head
            currRowIndex = 0

            # iterate through rows in column
            while currRow != None:

                # check if this row, col contains the value
                if (currRow.value == value):
                    positions.append((currRowIndex, currColIndex))

                currRow = currRow.next
                currRowIndex += 1

            currCol = currCol.next
            currColIndex += 1

        return positions



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        nonEmptyCells = []

        currCol = self.spreadsheet.head
        currColIndex = 0

        # iterate through columns in spreadsheet
        while currCol != None:

            currRow = currCol.value.head
            currRowIndex = 0

            # iterate through rows in column
            while currRow != None:

                # check if this row, col contains a value
                if (currRow.value != None):
                    nonEmptyCells.append(Cell(currRowIndex, currColIndex, currRow.value))

                currRow = currRow.next
                currRowIndex += 1

            currCol = currCol.next
            currColIndex += 1

        return nonEmptyCells
