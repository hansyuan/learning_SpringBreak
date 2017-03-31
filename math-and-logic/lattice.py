# Lattice. Strongest path. Triangle. 

# Down and Right moves only.

# Every pair of numbers has one parent node.
# Make the "choice" and then store the choice in the
# hash table.

# Read the txt file

# Use a hash map
# the key is row_position
# if down, then increment the row
# if right, increment the row and the position

DOWN = 0
RIGHT = 1
BOTH = 2

def readfile(filename):
    all = []
    lines = []
    with open(filename) as fp:
        for line in fp:
            lines.append(line[:-1])

    for line in lines:
        row = line.split(" ")
        all.append(row)

    print(all)
    return all


def setpaths(triangle, path):
    row = 0
    position = 0

    for currRow in range(0,len(triangle)-1):
        for currPos in range(0, len(triangle[currRow])):
            value = triangle[currRow][currPos]
            print(value)

            downData = triangle[currRow+1][currPos]
            rightData = triangle[currRow+1][currPos+1]

            chosen = choice(downData, rightData)
            print(chosen)

            strCoordinates = str(currRow)+"_"+str(currPos)

            path[strCoordinates] = chosen



def checkpaths(triangle,path):
    print("hello")

    lastRow = len(triangle)-1


    for lin in range(0, len(triangle[lastRow])):
        sum = triangle[lastRow][lin]
        row = lastRow
        pos = lin
        while row > 0:
            print (row)
            # check left parent node
            leftParent = checkNode(row-1, pos-1, triangle)

            # check right parent node
            rightParent = checkNode(row-1, pos, triangle)

            if leftParent == None or rightParent == None:
                break

            row -= 1


def checkNode(row, pos, triangle):
    print (str(row) + " " + str(pos))
    if pos < 0 or pos > len(triangle[row])-1:
        print("Out of bound, returned void.")
        return None
    else:
        print("Returned the node. ")
        return triangle[row][pos]

def choice(down, right):
    if down < right: return RIGHT
    elif down > right: return DOWN
    else: return BOTH

def main():
    #triangle = readfile("tri-small.txt")
    triangle = readfile("small.txt")
    paths = {}
    setpaths(triangle, paths)
    print(paths)
    checkpaths(triangle,paths)



main()
