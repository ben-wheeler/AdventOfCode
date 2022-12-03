def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    bestSoFar = 0
    comparator = 0
    thingsToCount = []
    for line in Lines:
        length = int(len(line) / 2)
        compart1 = line[:length]
        compart2 = line[length:]
        loopCheck = 0
        checking = []
        for char1 in compart1:
            if(loopCheck == 0):
                for char2 in compart2:
                    if(char1 == char2):
                        for char in checking:
                            if(char == char2):
                                loopCheck = 1
                        if(loopCheck == 0):        
                            checking.append(char2)
                        loopCheck = 1
        thingsToCount += checking
    for char in thingsToCount:
        temp = ord(char)
        if(temp > 96):
            temp -= 96
        else:
            temp -= 38
        bestSoFar += temp
        temp = 0

    print(bestSoFar)

if __name__ == "__main__":
    main()