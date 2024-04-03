import datetime

lis1 = []
list_of_dates = []
with open("dates2.txt", 'r') as input_file:
    for line in input_file:
        date_parts = line.strip().split("-")


        if len(date_parts) == 3:
            year, month, day = map(int, date_parts)
            date = datetime.datetime(year, month, day)
            list_of_dates.append([year, month, day])
            
        def wekkday(year):
            lis1.append(year)
        wekkday(year)

        wordscount = []
        for i in list_of_dates:
            wordscount.append(i[0])

        spec = {years: lis1.count(years) for years in wordscount}
        

total = []     
for years, count in spec.items():
    newtup = (count, years)
    total.append(newtup)

total = sorted(total, reverse= True)

for count, years in total[:3]:
    print(f"{years}: {count}")




