from tkinter import*

ship = Tk()
ship.title("Shit")
ship.geometry('800x600')
ship.resizable(width=False, height=False)

canvas = Canvas(ship, bg='white', width=800, height=600)

#Тельце
canvas.create_line(70, 350, 170, 470, width= 10, fill="brown")
canvas.create_line(170, 470, 630, 470, width= 10, fill="brown")
canvas.create_line(630, 470, 730, 350, width= 10, fill="brown")
canvas.create_line(70, 350, 730, 350, width= 10, fill="brown")
canvas.create_line(75, 350, 75, 200, width=7,fill="brown" )

#Мачта
canvas.create_line(400, 30, 400, 350, width=10, fill="brown")
canvas.create_line(270, 70, 530, 170, width= 5, fill="brown")
canvas.create_line(400, 50, 300, 80)
canvas.create_line(500, 160, 400, 50)

#Паруса
canvas.create_line(270, 70, 280, 120)
canvas.create_line(280, 120, 380, 110)

canvas.create_line(370,    110,    390, 210)
canvas.create_line(390,    210,    440, 135)

canvas.create_line(440, 135, 480, 200)
canvas.create_line(480,  200,    530, 170)


canvas.pack()
ship.mainloop()