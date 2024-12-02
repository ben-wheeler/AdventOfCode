with open('input.txt', 'r') as file:
    lines = file.readlines()

    left_column = []
    right_column = []

    for line in lines:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)

    left_column.sort()
    right_column.sort()

    total_distance = 0
    for left, right in zip(left_column, right_column):
        largest = right if left <= right else left
        smallest = right if left > right else left
        distance = (largest - smallest)
        total_distance += distance

    print(total_distance)