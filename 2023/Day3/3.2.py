with open('input.txt', 'r') as file:
    lines = []
    symbols = []

    for line in file:
        line = line.strip()
        currentLine = []
        currentSymbols = []
        numberCount = 0

        for char in line: 
            if not char.isdigit():
                numberCount = 0
                currentLine.append('.')
                if char != ".":
                    currentSymbols.append('T')    
                else:
                    currentSymbols.append('F')
            else:
                numberCount += 1
                currentLine.append(numberCount)
                currentSymbols.append('F')
        lines.append(currentLine)
        symbols.append(currentSymbols)

    rows = len(lines)
    cols = len(lines[0])
    partNumbers = []

    for i in range(rows):
        currentNumber = ""
        for j in range(cols):
            char = lines[i][j]
            if not char.isdigit():
                if char != ".":
                    # ladies and gentlemen we gottem (gear)

                    # search around the gear
                    # for each row, count the number of touching gears
                    # add this

                    gearCount = 0
                    currentNumber = ""
                    for col in range(max(0, j-len(currentNumber)-1), min(cols, j+1)):
                        if symbols[row][col] == 'T':
                            gearCount++
            if char.isdigit():
                currentNumber += char
                if j == cols-1:
                    if len(currentNumber) > 0:
                        number = int(currentNumber)
                        for row in range(max(0, i-1), min(rows, i+2)):
                            for col in range(max(0, j-len(currentNumber)-1), min(cols, j+1)):
                                if symbols[row][col] == 'T':
                                    partNumbers.append(number)
                                    number = 0
                    currentNumber = ""
            if not char.isdigit(): 
                if len(currentNumber) > 0:
                    number = int(currentNumber)
                    for row in range(max(0, i-1), min(rows, i+2)):
                        for col in range(max(0, j-len(currentNumber)-1), min(cols, j+1)):
                            if symbols[row][col] == 'T':
                                partNumbers.append(number)
                                number = 0
                currentNumber = ""
                    
print(sum(partNumbers))