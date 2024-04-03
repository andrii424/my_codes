import re

with open ("war_and_peace.txt", "r", encoding="utf-8") as war:
    for line in war:
        pshka = re.findall("P\S+", line)
        somefact = re.findall(r'\b(?:war|wra|awr|arw|rwa|raw)\b', line) 
        fact1 = re.findall('\S+war\S+', line)
        fact2 = re.findall('\S+wra\S+', line)
        fact3 = re.findall('\S+awr\S+', line)
        fact4 = re.findall('\S+arw\S+', line)
        fact5 = re.findall('\S+rwa\S+', line)
        fact6 = re.findall('\S+raw\S+', line)

        letters = re.findall(r'\b(?:[^ieokl\s]+)\b', line)
            
        if pshka:
            print(pshka)  
        if somefact:
            print(somefact)
        if fact1:
            print(fact1)
        if fact2:
            print(fact2)
        if fact3:
            print(fact3)
        if fact4:
            print(fact4)
        if fact5:
            print(fact5)
        if fact6:
            print(fact6)
        if letters:
            print(letters)



