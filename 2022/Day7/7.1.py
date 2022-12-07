class fileStats:
  def __init__(self, n, s, kids):
    self.name = n
    self.size = s
    self.children = kids
def __str__(self):
    # print here

def goUp(folder):
    uppedFolder = folder
    while(uppedFolder[-1] != "/"):
        uppedFolder = uppedFolder[:-1]
    uppedFolder = uppedFolder.rstrip()
    return uppedFolder

def main():
    f = open("input1.txt","r")
    Lines = f.readlines()
    currentFolder = ""
    items = []
    noKids = []

    for line in Lines:
        words = line.split(" ")
        if words[0] == "$":
            match words[1]:
                case "cd":
                    if(words[2] == ".."):
                        currentFolder = goUp(currentFolder)
                    else:
                        currentFolder += "/"
                        currentFolder += words[1]
                case "ls":
                    break
        elif words[0] == "dir":
            items.append(fileStats(currentFolder+"/"+words[1],0,noKids))                       
        elif words[0].isnumeric():
            items.append(fileStats(currentFolder+"/"+words[1],words[0],noKids))                      

    for item in items:
        print(item)
if __name__ == "__main__":
    main()