map = {
' red': 'r',
' blue': 'b',
' green': 'g',
}

with open('input.txt', 'r') as file:
    lines = []
    total = 0

    for line in file:
        line = line.strip()

        numberWords = map.keys()
        for word in numberWords:
            line = line.replace(word, map[word])
        words = line.split()
        invalid = False
        id = 0
        for word in words:
            if "Game" not in word:
                if ":" in word:
                    word = word.replace(":", "")
                    id = int(word)
                else:
                    if id != 0:
                        word = word.replace(",", "")
                        word = word.replace(";", "")
                        letter = word[-1]
                        number = int(''.join(c for c in word if c.isdigit()))
                        if letter == 'b':
                            if number > 14:
                                invalid = True
                        if letter == 'r':
                            if number > 12:
                                invalid = True
                        if letter == 'g':
                            if number > 13:
                                invalid = True
        if invalid == False:
            total += id
        # print(total)

print(total)