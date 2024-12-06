def ruleIsValid(position, line, rules):


with open('input.txt', 'r') as file:
    rules = []
    pageOrders = []
    for line in file:
        line = line.strip() 
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            pageOrders.append(line.split(","))
    

    for pageOrder in pageOrders:
        invalid = False
        for page_index, page in enumerate(pageOrder):
            if not ruleIsValid(page_index, line, rules):
                invalid = True
        

