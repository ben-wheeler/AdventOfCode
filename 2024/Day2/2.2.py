def isLineValid(numbers):
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
              return True
        else:
              return False

with open('input.txt', 'r') as file:
    lines = file.readlines()

    count = 0

    for line in lines:
        numbers = list(map(int, line.split()))
        
        if(isLineValid(numbers)):
            count += 1
            continue

        for i in range(len(numbers)):
            modified_numbers = numbers[:i] + numbers[i + 1:] 
            if isLineValid(modified_numbers):
                count += 1 
                break 
        

    print(count)