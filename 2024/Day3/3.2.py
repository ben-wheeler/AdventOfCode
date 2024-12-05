from re import findall

with open('input.txt', 'r') as file:
    data = file.read()
    total = 0
    enabled = True

    for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        if do or dont:
            enabled = bool(do)
        else:
            x = int(a) * int(b)
            total += x * enabled

    print(total)