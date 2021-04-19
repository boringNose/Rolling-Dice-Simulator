from tkinter import *
import random


def create_ovals(points):
    for x in range(len(points)):
        x1, y1, x2, y2 = points[x]
        ovals.append(c.create_oval(x1, y1, x2, y2, fill="white"))


def btn_pressed(event):
    if len(ovals) == 0:
        pass
    else:
        result.set("D1:0, D2:0")
        for x in ovals:
            c.delete(x)
        ovals.clear()

    random_num1 = str(random.randrange(1, 7))
    random_num2 = str(random.randrange(1, 7))
    result.set("D1: " + random_num1 + ", D2: " + random_num2)

    t1 = (
        (80, 90, 100, 110), (120, 90, 140, 110),
        (80, 120, 100, 140), (120, 120, 140, 140),
        (80, 150, 100, 170), (120, 150, 140, 170)
    )
    t2 = (
            (240, 90, 260, 110), (280, 90, 300, 110),
            (240, 120, 260, 140), (280, 120, 300, 140),
            (240, 150, 260, 170), (280, 150, 300, 170)
        )

    choose_cords1 = random.sample(t1, int(random_num1))
    choose_cords2 = random.sample(t2, int(random_num2))

    create_ovals(choose_cords1)
    create_ovals(choose_cords2)


ovals = []  # stores oval instances

window = Tk()      # creates an instance for main window
window.title("Dice Roll Simulator")
window.configure(bg="steelblue")    # sets background color for main window
window.geometry("500x500")      # sets width and height(width x height)

label = Label(window, text="Rolling Dice GUI", bg="gold", width=15, height=3, font=("Arial", 12))
label.pack()

btn_value = StringVar()     # stores string value for button's variable
btn_value.set("ROLL")
rollBtn = Button(window, textvariable=btn_value, width=10, height=2, bg="black", fg="white")
rollBtn.bind("<Button-1>", btn_pressed)     # binds a left button event
rollBtn.pack(pady=20)

result = StringVar()
result.set("D1:0, D2:0")
display = Label(window, textvariable=result, width=10, height=2, bg="brown", fg="white")
display.pack(pady=10)

c = Canvas(window, bg="lightsalmon")
c.pack()

c.create_rectangle(70, 80, 150, 180, fill="red")
c.create_rectangle(230, 80, 310, 180, fill="red")

window.mainloop()

