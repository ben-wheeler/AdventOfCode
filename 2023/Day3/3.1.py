with open('input.txt', 'r') as file:
    lines = []
    symbols = []

    for line in file:
        line = line.strip()
        currentLine = []
        currentSymbols = []

        for char in line: 
            # currentLine.append(char)
            if not char.isdigit():
                currentLine.append('.')
                if char != ".":
                    currentSymbols.append('T')    
                else:
                    currentSymbols.append('F')
            else:
                currentLine.append(char)
                currentSymbols.append('F')
        lines.append(currentLine)
        symbols.append(currentSymbols)
        # print(currentLine)
        # print(currentSymbols)

    rows = len(lines)
    cols = len(lines[0])
    # print(lines)
    print(rows)
    print(cols)
    partNumbers = []

    for i in range(rows):
        currentNumber = ""
        for j in range(cols):
            char = lines[i][j]
            print(f"at {i} {j}")
            if char.isdigit():
                print("number")
                currentNumber += char
                if j == cols-1:
                    print("last in row")
                    if len(currentNumber) > 0:
                        number = int(currentNumber)
                        for row in range(max(0, i-1), min(rows, i+2)):
                            for col in range(max(0, j-len(currentNumber)-1), min(cols, j+1)):
                                print(f"checking[{row}][{col}]")
                                if symbols[row][col] == 'T':
                                    print("found!")
                                    partNumbers.append(number)
                                    number = 0
                    currentNumber = ""
            if not char.isdigit(): 
                if len(currentNumber) > 0:
                    number = int(currentNumber)
                    for row in range(max(0, i-1), min(rows, i+2)):
                        for col in range(max(0, j-len(currentNumber)-1), min(cols, j+1)):
                            print(f"checking[{row}][{col}]")
                            if symbols[row][col] == 'T':
                                print("found!")
                                partNumbers.append(number)
                                number = 0
                currentNumber = ""
                    
print(partNumbers)
print(sum(partNumbers))