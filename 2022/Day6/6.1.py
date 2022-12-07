def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    my_set = set()
    score = 0
    for line in Lines:
        for char in line:
            if(len(my_set) < 4):
                if char in my_set:
                    my_set.clear()
                else:
                    my_set.add(char)
            if(len(my_set) == 4):
                print(score)
                return
            score += 1


if __name__ == "__main__":
    main()