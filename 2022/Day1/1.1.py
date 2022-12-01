def main():
       f = open("input1.txt","r")
       Lines = f.readlines()
       bestSoFar = 0
       comparisor = 0
       for line in Lines:
            if(line.strip()):
                comparisor += int(line)
            else:
                if(comparisor > bestSoFar):
                    bestSoFar = comparisor
                comparisor = 0
       print(bestSoFar)

if __name__ == "__main__":
    main()