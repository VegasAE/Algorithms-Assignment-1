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


# File will produce a different data set everytime it is run.
# For testing purposes, a seed will be set.
random.seed(85)



# ---------------------------------------------------
# These variables are randomly generated to avoid
# bias, however they will be generated once so that
# there is consistency accross the data sets, i.e.
# one medium sized set isn't going to have a
# different number of rows and columns compared to
# another medium sized set and one high density set
# won't have a different high density (78% and 85%)
# to another high density set.
# ---------------------------------------------------

smallSize = (random.randint(8, 20), random.randint(8, 20))
mediumSize = (random.randint(40, 125), random.randint(40, 125))
largeSize = (random.randint(100, 250), random.randint(100, 250))
lowDensity = (random.uniform(0.25, 0.45))
mediumDensity = (random.uniform(0.5, 0.7))
highDensity = (random.uniform(0.8, 1))

# small size, medium density
def smallMedSet():
    # determine number of cells to be created
    numOfCells = smallSize[0] * smallSize[1] * mediumDensity

    # create file and write to it
    f = open("SmallMedium.txt", 'w+')

    # initially add the bottom right corner of the data set (largest row and largets column)
    f.write(f"{smallSize[0]-1} {smallSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(smallSize[0]-1)} {random.randrange(smallSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(smallSize[0]-1)} {random.randrange(smallSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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
    f.write(f"{mediumSize[0]-1} {mediumSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(mediumSize[0]-1)} {random.randrange(mediumSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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
    f.write(f"{largeSize[0]-1} {largeSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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
    f.write(f"{largeSize[0]-1} {largeSize[1]-1} {round(random.uniform(0.0, 100.0), 1)}\n")
    numOfCells -= 1

    # decrease number of cells by one for each new cell created
    while numOfCells > 0:
        if (numOfCells != 1):
            f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}\n")
        else:
             f.write(f"{random.randrange(largeSize[0]-1)} {random.randrange(largeSize[1]-1)} {round(random.uniform(0.0, 100.0), 1)}")
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