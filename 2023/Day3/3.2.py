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
        maxRed = 0
        maxBlue = 0
        maxGreen = 0
        for word in words:
            if "Game" not in word:
                if ":" in word:
                    word = word.replace(":", "")
                else:
                    word = word.replace(",", "")
                    word = word.replace(";", "")
                    letter = word[-1]
                    number = int(''.join(c for c in word if c.isdigit()))
                    if letter == 'b':
                        if number > maxBlue:
                            maxBlue = number
                    if letter == 'r':
                        if number > maxRed:
                            maxRed = number
                    if letter == 'g':
                        if number > maxGreen:
                            maxGreen = number
        power = maxRed * maxBlue * maxGreen
        total += power

print(total)