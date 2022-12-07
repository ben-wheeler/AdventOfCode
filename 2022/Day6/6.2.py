def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    for line in Lines:
        for i in range(14, len(line)):
            my_set = set(line[(i-14):i])
            if len(my_set) == 14:
                print(i)
                return
    
if __name__ == "__main__":
    main()