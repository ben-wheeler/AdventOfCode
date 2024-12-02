with open('input.txt', 'r') as file:
    lines = file.readlines()

    count = 0

    for line in lines:
        numbers = list(map(int, line.split()))
        
        increasing = False
        decreasing = False
        valid_difference = True

        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i - 1]
            if not (1 <= abs(diff) <= 3):
                valid_difference = False
                break
        
            if numbers[i] > numbers[i - 1]:
                    increasing = True
            elif numbers[i] < numbers[i - 1]:
                    decreasing = True
        
        if (increasing != decreasing) and valid_difference:
            count += 1

    print(count)