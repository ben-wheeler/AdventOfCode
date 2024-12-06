with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    counter = 0

    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == 'A':
                if (col_index - 1 >= 0 and col_index + 1 < len(row)) and (row_index - 1 >= 0 and row_index + 1 < len(matrix)):
                    top_left_corner_word = matrix[row_index - 1][col_index -1] + element + matrix[row_index +1][col_index +1]
                    top_right_corner_word = matrix[row_index - 1][col_index + 1] + element + matrix[row_index +1][col_index -1]
                    if (top_left_corner_word == "MAS" or top_left_corner_word == "SAM") and (top_right_corner_word == "MAS" or top_right_corner_word == "SAM"):
                        counter+= 1



    print(counter)
