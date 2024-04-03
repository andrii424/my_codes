from tkinter import *
import textwrap
from PIL import Image, ImageTk
from colorthief import ColorThief  

default_poster = "D:\Python Learning\Project X\Posters\dh.jpg"

def search_film():
    name1 = user_entry.get().strip()
    name1 = name1.lower()   
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
            max_column_width2 = 20
            formatted_text = textwrap.fill(des4, max_column_width)
            formatted_text2 = textwrap.fill(des3, max_column_width2)

            if des1pro == "Cartoon":
                result_text.set(f"\nSomething, we found:\n{des1}\n"
                                f"It was created in {des2}, by {formatted_text2}\n"
                                f"\nHere is some details:\n{formatted_text}\n")
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
                max_column_width2 = 20
                formatted_text = textwrap.fill(des4, max_column_width)
                formatted_text2 = textwrap.fill(des3, max_column_width2)

                if des1pro == "Cartoon":
                    result_text.set(f"\nSomething, we found:\n{des1}\n"
                                    f"It was created in {des2}, by {formatted_text2}\n"
                                    f"\nHere is some details:\n{formatted_text}\n")
                    poster_path = des5
                    found = True
                    break


    if not found:
        canvas.delete('all')
        result_text.set("We don't have that in our library")
        poster_path = default_poster

    return poster_path


def update_poster():
    name = user_entry.get().strip()

    if name:  # Обновляйте постер только при вводе имени фильма
        poster_path = search_film()

        if poster_path:
            # Извлечение доминантного цвета из постера с использованием ColorThief
            color_thief = ColorThief(poster_path)
            dominant_color = color_thief.get_color(quality=1)

            # Преобразование RGB в шестнадцатеричный цветовой код
            hex_color = "#{:02x}{:02x}{:02x}".format(dominant_color[0], dominant_color[1], dominant_color[2])

            # Обновление цвета интерфейса
            root.config(bg=hex_color)

            original_image = Image.open(poster_path)
            resized_image = original_image.resize((227, 341))
            resized_photo = ImageTk.PhotoImage(resized_image)

            canvas.delete('all')
            canvas.image = resized_photo
            canvas.create_image(0, 340, anchor=SW, image=resized_photo)

    else:
        canvas.delete('all')
        poster_path = default_poster
        result_text.set("Enter the name of your movie")


    

# Чтение данных из файла
with open("disney.txt", "r", encoding="utf-8") as inp:
    file = [some.strip() for some in inp.readlines()]



# Создание графического интерфейса
root = Tk()
root.title('Disney Finder')
root.config(bg='white')
root.geometry('900x500')
root.resizable(0, 0)
root.iconbitmap("D:\Python Learning\Project X\Posters\icon.ico")



# Полоска с текстом
Label(root, text="Enter the name of your film", bg='white', font=('Times', 13), anchor='center', width=300, height=0).place(x=-910, y = 75)



# Строка поиска и кнопка
user_entry = Entry(root, width=40, font=('Times', 13))
user_entry.config(bg='white')
user_entry.place(x = 225, y = 25)
Button(root, text='Search', font=('Times', 10), width=10, height=1, command=update_poster).place(x=595, y= 24)



# Картинка, постер
original_image = Image.open("D:\Python Learning\Project X\Posters\home.jpg")
resized_image = original_image.resize((227, 341))
resized_photo = ImageTk.PhotoImage(resized_image)
canvas = Canvas(root, width=225, height=330, bg="#99f")
canvas.place(x=80, y=130)
canvas.image = resized_photo
canvas.create_image(0, 340, anchor=SW, image=resized_photo)
color_thief = ColorThief("D:\Python Learning\Project X\Posters\icon2.jpg")
dominant_color = color_thief.get_color(quality=1)



# Преобразование RGB в шестнадцатеричный цветовой код
hex_color = "#{:02x}{:02x}{:02x}".format(dominant_color[0], dominant_color[1], dominant_color[2])
# Обновление цвета интерфейса
root.config(bg=hex_color)



# Основной текст 
result_text = StringVar()
max_column_width = 40

some = textwrap.fill('Disney Finder can help you find the information you need about your favourite classic cartoons. All you need to do is enter the name of your film and click "Search"', max_column_width)

result_text.set(some)
result_label = Label(root, textvariable=result_text, font=('Times', 14), bg="white", justify=LEFT, anchor="center")
result_label.place(x=390, y=129, height=335, width=430)


root.mainloop()
