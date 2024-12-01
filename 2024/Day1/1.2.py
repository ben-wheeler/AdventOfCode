def store_number(dict, number):
    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1
        

with open('input.txt', 'r') as file:
    lines = file.readlines()

    left_column = []
    right_column = {}

    for line in lines:
        left, right = map(int, line.split())
        left_column.append(left)
        store_number(right_column, right)

    similarity_score = 0
    for number in left_column:
        if number in right_column:
            similarity_score += number * right_column[number]

    print(similarity_score)