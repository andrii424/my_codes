with open("disney.txt", "r") as inp: 

    line = False           
    file = [some.strip() for some in inp.readlines()]
    name = input("Please, enter the name of your film: ")
    name = name.strip()
    
    for i in range(len(file)):
                if name in file[i]:
                    if i + 3 < len(file):
                        des1 = (file[i])
                        des1pro = (file[i + 1])
                        
                        des2 = (file[i + 2])
                        des3 = (file[i + 3])

                        if des1pro == "Cartoon":
                              print("Here is something, we found: \n", des1, "\n", "It was created in ", des2, ", by ", des3, "\nHere are some details about the plot: \n", sep="")
                              line = True
    if line == False:
        print("There is no such a film in our library")