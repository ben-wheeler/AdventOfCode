

with open('input.txt', 'r') as file:
    lines = []
    points = []
    game_count = len(file.readlines())
    file.seek(0)
    cardCount = [1] * game_count
    winsForRound = [-1] * game_count
    totalCards = 0

    for line_number, line in enumerate(file, start=0):
        print(line_number)
        for i in range(cardCount[line_number]):
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
                    word = word.replace(":", "")
                    game = int(word)
                elif "|" in word:
                    section = 2
                elif section == 1:
                    winningCards.append(int(word))
                elif section == 2:
                    if int(word) in winningCards:
                        howManyAmIWinning += 1
            # print(f"g{game} u won{howManyAmIWinning}")
            for i in range(howManyAmIWinning):
                if game + i < len(cardCount):
                    cardCount[game + i] += 1
                    totalCards += 1

print(totalCards+game_count)