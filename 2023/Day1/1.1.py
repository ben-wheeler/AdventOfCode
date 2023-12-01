with open('input.txt', 'r') as file:
    lines = []

    for line in file:
        line = line.strip()
        currentLine = []

        for char in line: 
            if char.isdigit():
                if len(currentLine) > 1:
                    currentLine[1] = char
                else:
                    currentLine.append(char)
                    currentLine.append(char)

                # print(char)

        lines.append(currentLine)

    total = 0
    numbers = [int(''.join(pair)) for pair in lines]
    for number in numbers:
        total += number

print(total)