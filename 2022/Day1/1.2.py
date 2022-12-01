def main():
       f = open("input1.txt","r")
       Lines = f.readlines()
       bestSoFar = 0
       secondBest = 0
       thirdBest = 0
       comparisor = 0
       for line in Lines:
            if(line.strip()):
                comparisor += int(line)
            else:
                if(comparisor >= bestSoFar):
                    thirdBest = secondBest
                    secondBest = bestSoFar
                    bestSoFar = comparisor
                elif(comparisor >= secondBest):
                    thirdBest = secondBest
                    secondBest = comparisor
                elif(comparisor >= thirdBest):
                    thirdBest = comparisor
                comparisor = 0
       print(bestSoFar+secondBest+thirdBest)

if __name__ == "__main__":
    main()