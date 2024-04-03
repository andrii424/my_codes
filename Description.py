with open("disney.txt", "r") as inp: 

    line = False           
    file = [some.strip() for some in inp.readlines()]
    name = input("Please, enter the name of your film: ")
    name = name.strip()
    
    for i in range(len(file)):
                if name in file[i]:
                    if i + 6 < len(file):
                        des1 = (file[i])
                        des1pro = (file[i + 1])
                        
                        des2 = (file[i + 2])
                        des3 = (file[i + 3])
                        des4 = (file[i + 4])

                        des2pro = ("Created in:")
                        des3pro = ("Directed by:")
                        des4pro = ("Here are some details: ")
                        forupp = int((len(des1) + len(des2) + len(des3)) * 1.2)
                        upp = "+" + "-" * forupp + "+"
                        
                        import textwrap

                        text = des4
                        max_column_width = 80

                        formatted_text = textwrap.fill(text, max_column_width)
                        print(formatted_text)



                        # print(upp)
                        # print("|" + " " * forupp + "|")
                        # print("|" + " " * forupp + "|")
                        # print("|", des1.center(forupp - 2), "|" )
                        # print("|", des2pro.center(forupp - 2), "|" )
                        # print("|", des2.center(forupp - 2), "|" )
                        # print("|", des3pro.center(forupp - 2), "|" )
                        # print("|", des3.center(forupp - 2), "|" )
                        # print("|", des4pro.center(forupp - 2), "|")
                        # print("|", des4.center(forupp - 2), "|")
                        # print("|" + " " * forupp + "|")
                        # print("|" + " " * forupp + "|")
                        # print(upp)
                        # line = True
                        