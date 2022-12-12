def main():
    f = open("input.txt","r")
    Lines = f.readlines()
    dataMatrix = []
    scoreMatrix = []
    dataRow = []
    scoreRow = []
    score = 0

    for line in Lines:
        line = line.strip()
        for char in line:
            num = int(char)
            dataRow.append(num)
            scoreRow.append(0)
        dataMatrix.append(dataRow)
        scoreMatrix.append(scoreRow)
        dataRow = []
        scoreRow = []
    row = len(dataMatrix[0])
    col = len(dataMatrix)

    score += ((row * 2) + (col * 2)) - 4

    for r in range(1,row-1):
        biggest = dataMatrix[r][0]
        backBiggest = dataMatrix[r][col-1]
        for c in range(1,col-1//2):
            if(dataMatrix[r][c] > biggest):
                biggest = dataMatrix[r][c]
                scoreMatrix[r][c] += 1
            d = col - c
            if(dataMatrix[r][d] > backBiggest):
                backBiggest = dataMatrix[r][d]
                scoreMatrix[r][d] += 1
    print(row-1)
    print("x")
    print(col-1)
    for c in range(1,col-1):
        biggest = dataMatrix[0][c]
        backBiggest = dataMatrix[row-1][c]
        for r in range(1,row-1//2):
            if(dataMatrix[r][c] > biggest):
                biggest = dataMatrix[r][c]
                scoreMatrix[r][c] += 1
            d = row - c
            if(dataMatrix[r][d] > backBiggest):
                backBiggest = dataMatrix[r][d]
                scoreMatrix[r][d] += 1
        # d = col-1
        # while(row[r][c] < row[r][c+1]):
        #     scoreMatrix[r][c] += 1
        #     c += 1
        # d = col-1
    
    for r in range(1,row-1):
        biggest = 0
        for c in range(1,col-1):
            if scoreMatrix[r][c] > 0:
                score += 1
    
    print(score)
if __name__ == "__main__":
    main()