map = {
'one': 'o1e',
'two': 't2o',
'three': 'th3ee',
'four': 'fo4fur',
'five': 'fi5fve',
'six': 'si6x',
'seven': 'se7ven',
'eight': 'eig8eht',
'nine': 'ni9ne',
}

with open('input.txt', 'r') as file:
    lines = []

    for line in file:
        line = line.strip()
        currentLine = []

        numberWords = map.keys()
        for word in numberWords:
            line = line.replace(word, map[word])

        for char in line: 
            if char.isdigit():
                if len(currentLine) > 1:
                    currentLine[1] = char
                else:
                    currentLine.append(char)
                    currentLine.append(char)

        lines.append(currentLine)

    total = 0
    numbers = [int(''.join(pair)) for pair in lines]
    for number in numbers:
        total += number

print(total)
