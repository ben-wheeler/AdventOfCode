class fileStats:
    def __init__(self, n, s, kids):
        self.name = n
        self.size = s
        self.children = kids
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def goUp(folder):
    uppedFolder = folder
    while(uppedFolder[-1] != "/"):
        uppedFolder = uppedFolder[:-1]
    uppedFolder = uppedFolder[:-1]
    return uppedFolder

def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    currentFolder = ""
    items = []
    noKids = []
    kids = []

    for line in Lines:
        words = line.split(" ")
        if words[0] == "$":
            if words[1] == "cd":
                words[2] = words[2].strip()
                if(words[2] == ".."):
                    currentFolder = goUp(currentFolder)
                else:
                    if(words[2] == '/'):
                        currentFolder += '~'
                    else:
                        currentFolder += '/' + words[2]
        elif words[0] == "dir":
            words[1] = words[1].strip()
            items.append(fileStats(currentFolder+"/"+words[1]+"-",0,noKids)) 
            # get kids                      
        elif words[0].isnumeric():
            words[1] = words[1].strip()
            items.append(fileStats(currentFolder+"/"+words[1],words[0],noKids))                      
    kids = []
    items.sort()
    for item in items:
        print(item)
if __name__ == "__main__":
    main()