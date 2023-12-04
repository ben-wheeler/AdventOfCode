with open('input.txt', 'r') as file:
    lines = []
    points = []

    for line in file:
        line = line.strip()

        line = line.replace("Card", "")
        section = 0
        words = line.split()
        game = 0
        winningCards = []
        howManyAmIWinning = 0
        # print(line)
        for word in words:
            if ":" in word:
                # this is the card number
                section = 1
                game = word
            elif "|" in word:
                section = 2
            elif section == 1:
                winningCards.append(int(word))
            elif section == 2:
                if int(word) in winningCards:
                    howManyAmIWinning += 1

        print(f"{game} {howManyAmIWinning}")
        pointsThisRound = 0
        if(howManyAmIWinning > 0):
            pointsThisRound = 2**(howManyAmIWinning-1)
        points.append(pointsThisRound)

print(sum(points))