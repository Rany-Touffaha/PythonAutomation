# open input file
inputFile = open('inputFile.txt', 'r')

# create pass file for writing
passFile = open('passFile.txt', 'w')

# create fail file for writing
failFile = open('failFile.txt', 'w')

# loop through each line and print only those that passed the test
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

# close the input file
inputFile.close()

# close the pass file
passFile.close()

# close the fail file
failFile.close()
