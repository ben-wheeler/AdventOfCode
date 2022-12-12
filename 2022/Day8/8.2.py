def main():
    f = open("input.txt","r")
    Lines = f.readlines()
    for line in Lines:
        for i in range(4, len(line)):
            my_set = set(line[(i-4):i])
            if len(my_set) == 4:
                print(i)
                return

if __name__ == "__main__":
    main()