with open('part1.txt', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        line = line.strip()
        currentLine = []

        # Remove the newline character at the end of the line
        for char in line: 
            if char.isdigit():
                if len(currentLine) > 1:
                    currentLine[1] = char
                else:
                    currentLine.append(char)
                    currentLine.append(char)

                # print(char)

        # Append the line to the list
        lines.append(currentLine)

    total = 0
    # for numbers in lines:
    numbers = [int(''.join(pair)) for pair in lines]
    for number in numbers:
        total += number

# Print the list of lines
print(total)