# switch statement for other elf's play
def switch(letter):
    if(letter == 'A'):
        return 1;
    elif(letter == 'B'):
        return 2;
    elif(letter == 'C'):
        return 3

# switch statement for my play
def stich(letter):
    if(letter == 'X'):
        return 4;
    elif(letter == 'Y'):
        return 5;
    elif(letter == 'Z'):
        return 6

# main
def main():
        f = open("input1.txt","r") # read file
        Lines = f.readlines() # get lines
        score = 0 # score tracker
        for line in Lines: # loop for each move
            # variables for each player
            theirPlay = 0
            yourPlay = 0

            # calculate scores
            theirPlay = switch(line[0])
            yourPlay = stich(line[2])

            # do the math for the logic
            if(theirPlay == 1):
                if(yourPlay == 4):
                    score += 3
                    score += 0
                elif(yourPlay == 5):
                    score += 1
                    score += 3
                elif(yourPlay == 6):
                    score += 2
                    score += 6
            if(theirPlay == 2):
                if(yourPlay == 4):
                    score += 1
                    score += 0
                elif(yourPlay == 5):
                    score += 2
                    score += 3
                elif(yourPlay == 6):
                    score += 3
                    score += 6      
            if(theirPlay == 3):
                if(yourPlay == 4):
                    score += 2
                    score += 0
                elif(yourPlay == 5):
                    score += 3
                    score += 3
                elif(yourPlay == 6):
                    score += 1
                    score += 6    
        # print score 
        print(score)

if __name__ == "__main__":
    main()