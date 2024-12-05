from re import findall

with open('input.txt', 'r') as file:
    data = file.read()
    total = 0

    for a, b in findall(r"mul\((\d+),(\d+)\)", data):
        x = int(a) * int(b)
        total += x

    print(total)