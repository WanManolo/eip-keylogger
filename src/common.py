
def printFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line)
    file.close()
