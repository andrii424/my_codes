from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Picture")
root.resizable(0, 0)
root.geometry("800x600")

canvas = Canvas(root, width=800, height=600)
canvas.pack()

# Открываем изображение с использованием Pillow
original_image = Image.open('D:\\Python Learning\\Project X\\Code\\dalmm.jpg')

# Уменьшаем размер изображения (например, до 100x100 пикселей)
resized_image = original_image.resize((300, 300))

# Конвертируем уменьшенное изображение в формат PhotoImage для Tkinter
resized_photo = ImageTk.PhotoImage(resized_image)

# Отображаем уменьшенное изображение на Canvas
canvas.create_image(50, 50, anchor=NW, image=resized_photo)

root.mainloop()
