def main():
       f = open("input1.txt","r")
       Lines = f.readlines()
       bestSoFar = 0
       comparator = 0
       for line in Lines:
            if(line.strip()):
                comparator += int(line)
            else:
                if(comparator > bestSoFar):
                    bestSoFar = comparator
                comparator = 0
       print(bestSoFar)

if __name__ == "__main__":
    main()