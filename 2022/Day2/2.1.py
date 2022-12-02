def switch(letter):
    if(letter == 'A'):
        return 1;
    elif(letter == 'B'):
        return 2;
    elif(letter == 'C'):
        return 3

def stich(letter):
    if(letter == 'X'):
        return 4;
    elif(letter == 'Y'):
        return 5;
    elif(letter == 'Z'):
        return 6

def main():
       f = open("input1.txt","r")
       Lines = f.readlines()
       score = 0
       theirPlay = 0
       for line in Lines:
            theirPlay = 0
            yourPlay = 0
            theirPlay = switch(line[0])
            yourPlay = stich(line[2])
            if(theirPlay == 1):
                if(yourPlay == 4):
                    score += 3
                    score += 1
                elif(yourPlay == 5):
                    score += 6
                    score += 2
                elif(yourPlay == 6):
                    score += 0
                    score += 3
            if(theirPlay == 2):
                if(yourPlay == 4):
                    score += 0
                    score += 1
                elif(yourPlay == 5):
                    score += 3
                    score += 2
                elif(yourPlay == 6):
                    score += 6
                    score += 3      
            if(theirPlay == 3):
                if(yourPlay == 4):
                    score += 6
                    score += 1
                elif(yourPlay == 5):
                    score += 0
                    score += 2
                elif(yourPlay == 6):
                    score += 3
                    score += 3    
            
       print(score)

if __name__ == "__main__":
    main()