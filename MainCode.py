from tkinter import *
import textwrap
from PIL import Image, ImageTk

def search_film():
    name1 = user_entry.get().strip()
    poster_path = ""
    found = False

    for i in range(len(file)):
        if name1 in file[i].lower():
            des1 = file[i]
            des1pro = file[i + 1]
            des2 = file[i + 2]
            des3 = file[i + 3]
            des4 = file[i + 4]
            des5 = file[i + 5]

            max_column_width = 50
            max_column_width2 = 30
            formatted_text = textwrap.fill(des4, max_column_width)
            formatted_text2 = textwrap.fill(des3, max_column_width2)

            if des1pro == "Cartoon":
                result_text.set(f"\nHere is something we found:\n{des1}\n"
                                f"It was created in {des2}, by {formatted_text2}\n"
                                f"\nHere are some details about the plot:\n{formatted_text}\n")

                poster_path = des5
                found = True
                break
    if not found:
        for i in range(len(file)):
            if name1 in file[i].capitalize():
                des1 = file[i]
                des1pro = file[i + 1]
                des2 = file[i + 2]
                des3 = file[i + 3]
                des4 = file[i + 4]
                des5 = file[i + 5]

                max_column_width = 50
                max_column_width2 = 30
                formatted_text = textwrap.fill(des4, max_column_width)
                formatted_text2 = textwrap.fill(des3, max_column_width2)

                if des1pro == "Cartoon":
                    result_text.set(f"\nHere is something we found:\n{des1}\n"
                                    f"It was created in {des2}, by {formatted_text2}\n"
                                    f"\nHere are some details about the plot:\n{formatted_text}\n")

                    poster_path = des5
                    found = True
                    break

    if not found:
        canvas.delete('all')
        result_text.set("There is no such film in our library")

    return poster_path

def update_poster():
    name = user_entry.get().strip()

    if name:  # Only update the poster if a film name is entered
        poster_path = search_film()

        if poster_path:
            
            original_image = Image.open(poster_path)
            resized_image = original_image.resize((227, 341))
            resized_photo = ImageTk.PhotoImage(resized_image)

            canvas.delete('all')
            canvas.image = resized_photo
            canvas.create_image(0, 340, anchor=SW, image=resized_photo)

    else:
        canvas.delete('all')
        result_text.set("Please, enter the name of the film")
    

# Чтение данных из файла
with open("disney.txt", "r", encoding="utf-8") as inp:
    file = [some.strip() for some in inp.readlines()]

# Создание графического интерфейса
root = Tk()
root.title('Disney Finder')
root.config(bg='#c9f')
root.geometry('900x500')
root.resizable(0, 0)

Label(root, text="Enter the name of your film:", bg='white', font=("Arial", 12), anchor='center', width=300, height=0).place(x=0, y = 70)

user_entry = Entry(root, width=40, font=('Arial', 12))
user_entry.config(bg='white')
user_entry.place(x = 225, y = 25)

Button(root, text='Search', font=("Arial", 8), width=10, height=1, command=update_poster).place(x=595, y= 24)



canvas = Canvas(root, width=225, height=330, bg="#c9f")
canvas.place(x=80, y=130)

result_text = StringVar()
result_label = Label(root, textvariable=result_text, font=('Arial', 12), bg="white", justify=LEFT, anchor="center")
result_label.place(x=400, y=94, height=410, width=500)
root.mainloop()


