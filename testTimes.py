import sys
from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet
from spreadsheet.csrSpreadsheet import CSRSpreadsheet
from time import perf_counter_ns
import random
import copy


# change recurssion limit to allow deep copy of large sized linked lists
sys.setrecursionlimit(50000)

def testTimes():
    numOfRuns = 1000 # number of times the program will loop for timing

    # append row
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.appendRow()
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to append row: {avgTime} ns")

    # append column
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.appendCol()
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to append column: {avgTime} ns")

    # insert row
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.insertRow(random.randint(-1, 1000))
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to insert row: {avgTime} ns")

    # insert column
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.insertCol(random.randint(-1, 1000))
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to insert column: {avgTime} ns")

    # update cell
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.update(random.randint(0, 1000), random.randint(0,1000), round(random.uniform(-100, 100), 1))
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to update cell: {avgTime} ns")

    # find value
    spreadsheetCopy = copy.deepcopy(spreadsheet)
    tStart = perf_counter_ns()
    for i in range(numOfRuns):
        spreadsheetCopy.find(round(random.uniform(-100, 100), 1))
    tEnd = perf_counter_ns()
    runTime = tEnd - tStart
    avgTime = runTime/numOfRuns
    print(f"Average time to find value: {avgTime} ns")






def usage():
    """
    Print help/usage message.
    """

    # On Teaching servers, use 'python3'
    # On Windows, you may need to use 'python' instead of 'python3' to get this to work
    print('python3 testTimes.py', '<approach> <data fileName> <command fileName> <output fileName>')
    print('<approach> = <array | linkedlist | csr>')
    sys.exit(1)


if __name__ == '__main__':
    # Fetch the command line arguments
    args = sys.argv

    if len(args) != 3:
        print('Incorrect number of arguments.')
        usage()

    # initialise spreadsheet object
    spreadsheet: BaseSpreadsheet = None
    if args[1] == 'array':
        buildStart = perf_counter_ns()
        spreadsheet = ArraySpreadsheet()
        buildEnd = perf_counter_ns()
    elif args[1] == 'linkedlist':
        buildStart = perf_counter_ns()
        spreadsheet = LinkedListSpreadsheet()
        buildEnd = perf_counter_ns()
    elif args[1] == 'csr':
        buildStart = perf_counter_ns()
        spreadsheet = CSRSpreadsheet()
        buildEnd = perf_counter_ns()
    else:
        print('Incorrect argument value.')
        usage()

    print(f"Time taken to build spreadsheet: {buildEnd - buildStart} ns")

    # read from data file to populate the initial set of points
    dataFilename = args[2]
    cellsFromFiles = []
    try:
        dataFile = open(dataFilename, 'r')
        for line in dataFile:
            values = line.split()
            currRow = int(values[0])
            currCol = int(values[1])
            currVal = float(values[2])
            currCell = Cell(currRow, currCol, currVal)
            # each line contains a cell
            cellsFromFiles.append(currCell)
        dataFile.close()
        # construct the spreadsheet from the read in data
        spreadsheet.buildSpreadsheet(cellsFromFiles)

        # test times
        if args[1] == 'array':
            print("Average times for each function for Array based implementation")
            testTimes()
        elif args[1] == 'linkedlist':
            print("Average times for each function for Linked List based implementation")
            testTimes()
        elif args[1] == 'csr':
            print("Average times for each function for CSR based implementation")
            testTimes()

    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

   
    