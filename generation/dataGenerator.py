import random
from time import sleep

# ---------------------------------------------------
# This file is for data generation purposes and
# produces input files for use in the different
# spreadsheet implementations. Functions will be
# named based on first the data set size and then
# the density of the array that will be populated.
# Each function will produce an output file using the
# format of the sampleData.txt file.
#
# Sizes: Small, Medium, Large
# Densities: Low, Medium, High
# ---------------------------------------------------


smallSize = (20, 20)
mediumSize = (60, 60)
largeSize = (250, 250)
lowDensity = 0.25
mediumDensity = 0.65
highDensity = 0.95

# small size, medium density
def smallMedSet():
    # determine number of cells to be created
    numOfCells = smallSize[0] * smallSize[1] * mediumDensity

    # create file and write to it
    f = open("SmallMedium.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{smallSize[0]-1} {smallSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(smallSize[0]-1)} {random.randrange(smallSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(smallSize[0]-1)} {random.randrange(smallSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1

    # close file for reading
    f.close()

# medium size, low density
def medLowSet():
    # determine number of cells to be created
    numOfCells = mediumSize[0] * mediumSize[1] * lowDensity

    # create file and write to it
    f = open("MediumLow.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1

    # close file for reading
    f.close()

# medium size, medium density
def medMedSet():
    # determine number of cells to be created
    numOfCells = mediumSize[0] * mediumSize[1] * mediumDensity

    # create file and write to it
    f = open("MediumMedium.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1

    # close file for reading
    f.close()

# medium size, high density
def medHighSet():
    # determine number of cells to be created
    numOfCells = mediumSize[0] * mediumSize[1] * highDensity

    # create file and write to it
    f = open("MediumHigh.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1

    # close file for reading
    f.close()

# large size, medium density
def largeMedSet():
    # determine number of cells to be created
    numOfCells = largeSize[0] * largeSize[1] * mediumDensity

    # create file and write to it
    f = open("LargeMedium.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{largeSize[0]-1} {largeSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1

    # close file for reading
    f.close()

# large size, high density
def largeHighSet():
    # determine number of cells to be created
    numOfCells = largeSize[0] * largeSize[1] * highDensity

    # create file and write to it
    f = open("LargeHigh.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{largeSize[0]-1} {largeSize[1]-1} {round(random.uniform(-100.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(-100.0, 100.0), 1)}")
        numOfCells -= 1
    
    # close file for reading
    f.close()
    

# function to generate everything
def generateData():
    print("Generating Data")
    smallMedSet()
    medLowSet()
    medMedSet()
    medHighSet()
    largeMedSet()
    largeHighSet()
    sleep(0.3)
    print("Data generated!")

if __name__ == "__main__":
    generateData()