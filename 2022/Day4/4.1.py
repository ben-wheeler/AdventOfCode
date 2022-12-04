def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    bestSoFar = 0
    comparator = 0
    for l in Lines:
        line = l.strip()
        split = line.split(",")
        first = split[0].split("-")
        second = split[1].split("-")
        firstSet = set(range(int(first[0]),int(first[1])+1))
        secSet = set(range(int(second[0]),int(second[1])+1))
        if(firstSet.issubset(secSet)):
            bestSoFar += 1
        elif(secSet.issubset(firstSet)):
            bestSoFar += 1
    print(bestSoFar)

if __name__ == "__main__":
    main()