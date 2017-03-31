# Lattice. Strongest path. Triangle. 

# Down and Right moves only.  

# Read the txt file
def readFile(filename):
    lines = []
    with open(filename) as fp:
        for line in fp:
            lines.append(line[:-1])

    for line in lines:
        row = line.split(" ")
        print (row)

# Place into list of lists

# 

def main():
    readFile("tri-small.txt")





main()
