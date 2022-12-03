def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    bestSoFar = 0
    thingsToCount = []
    counter = 1;
    line1 = ""
    line2 = ""
    line3 = ""
    for line in Lines:
        line = line.strip()
        if(counter % 3 == 1):
            line1 = line
        elif(counter % 3 == 2):
            line2 = line    
        elif(counter % 3 == 0):
            line3 = line
            ans = set(line1) & set(line2) & set(line3)
            print(ans)
            line1 = ""
            line2 = ""
            line3 = ""
            thingsToCount.append(ans.pop())
        counter += 1

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