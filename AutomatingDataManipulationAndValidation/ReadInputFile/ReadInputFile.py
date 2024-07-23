# open input file
inputFile = open('inputFile.txt', 'r')

# loop through each line and print only those that passed the test
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)

# close the input file
inputFile.close()
