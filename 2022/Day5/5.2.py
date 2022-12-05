def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    pile1 = ['S','T','H','F','W','R']
    pile2 = ['S','G','D','Q','W']
    pile3 = ['B','T','W']
    pile4 = ['D','R','W','T','N','Q','Z','J']
    pile5 = ['F','B','H','G','L','V','T','Z']
    pile6 = ['L','P','T','C','V','B','S','G']
    pile7 = ['Z','B','R','T','W','G','P']
    pile8 = ['N','G','M','T','C','J','R']
    pile9 = ['L','G','B','W']
    empty = []
    piles = []
    piles.append(empty)
    piles.append(pile1)
    piles.append(pile2)
    piles.append(pile3)
    piles.append(pile4)
    piles.append(pile5)
    piles.append(pile6)
    piles.append(pile7)
    piles.append(pile8)
    piles.append(pile9)

    for line in Lines:
        if line[0] == 'm':
            words = line.split(" ")
            howMany = int(words[1])
            org = int(words[3])
            dest = int(words[5])
            temp = len(piles[org])-howMany
            steal = piles[org][temp:]
            print(steal)
            piles[dest].extend(steal)
            piles[org] = piles[org][:temp]
            # for x in range(howMany):

    for x in range(10):
        if(x > 0):
            print(piles[x][-1])

if __name__ == "__main__":
    main()