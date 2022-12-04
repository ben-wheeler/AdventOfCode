def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    bestSoFar = 0
    secondBest = 0
    thirdBest = 0
    comparator = 0
    for line in Lines:
        if(line.strip()):
            comparator += int(line)
        else:
            if(comparator >= bestSoFar):
                thirdBest = secondBest
                secondBest = bestSoFar
                bestSoFar = comparator
            elif(comparator >= secondBest):
                thirdBest = secondBest
                secondBest = comparator
            elif(comparator >= thirdBest):
                thirdBest = comparator
            comparator = 0
    print(bestSoFar+secondBest+thirdBest)

if __name__ == "__main__":
    main()