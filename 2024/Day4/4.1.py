with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    counter = 0

    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == 'X':
                if col_index + 3 < len(row) and \
                   matrix[row_index][col_index + 1] == "M" and \
                   matrix[row_index][col_index + 2] == "A" and \
                   matrix[row_index][col_index + 3] == "S":
                    counter += 1

                if row_index + 3 < len(matrix) and col_index + 3 < len(row) and \
                   matrix[row_index + 1][col_index + 1] == "M" and \
                   matrix[row_index + 2][col_index + 2] == "A" and \
                   matrix[row_index + 3][col_index + 3] == "S":
                    counter += 1

                if row_index + 3 < len(matrix) and \
                   matrix[row_index + 1][col_index] == "M" and \
                   matrix[row_index + 2][col_index] == "A" and \
                   matrix[row_index + 3][col_index] == "S":
                    counter += 1

                if row_index + 3 < len(matrix) and col_index - 3 >= 0 and \
                   matrix[row_index + 1][col_index - 1] == "M" and \
                   matrix[row_index + 2][col_index - 2] == "A" and \
                   matrix[row_index + 3][col_index - 3] == "S":
                    counter += 1

                if col_index - 3 >= 0 and \
                   matrix[row_index][col_index - 1] == "M" and \
                   matrix[row_index][col_index - 2] == "A" and \
                   matrix[row_index][col_index - 3] == "S":
                    counter += 1

                if row_index - 3 >= 0 and col_index - 3 >= 0 and \
                   matrix[row_index - 1][col_index - 1] == "M" and \
                   matrix[row_index - 2][col_index - 2] == "A" and \
                   matrix[row_index - 3][col_index - 3] == "S":
                    counter += 1

                if row_index - 3 >= 0 and \
                   matrix[row_index - 1][col_index] == "M" and \
                   matrix[row_index - 2][col_index] == "A" and \
                   matrix[row_index - 3][col_index] == "S":
                    counter += 1

                if row_index - 3 >= 0 and col_index + 3 < len(row) and \
                   matrix[row_index - 1][col_index + 1] == "M" and \
                   matrix[row_index - 2][col_index + 2] == "A" and \
                   matrix[row_index - 3][col_index + 3] == "S":
                    counter += 1

    print(counter)
