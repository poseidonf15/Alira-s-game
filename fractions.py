from tkinter import *
import random

size = 1000000
padx = 10
pady = 5
width = 2
ans = 0
rans = 0

def enter(event):
    player()

def create_question():
    global num1
    global num2
    global num3
    global num4
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    while (True):
        num3 = random.randint(1, 20)
        if num3 != num2:
            break
    num4 = random.randint(1, 20)
    numlabel1.config(text = num1)
    numlabel2.config(text = num2)
    numlabel3.config(text = num3)
    numlabel4.config(text = num4)

def player():
    global ans
    global rans
    ans += 1
    answers.config(text = f"Number of answers : {ans}")
    if round(int(entry1.get()) / int(entry2.get()), 3) == round(float(num1 / num2 + num3 / num4), 3):
        check.config(text = "Right answer good jub :)")
        rans += 1
        right_answers.config(text = f"Number of right answers : {rans}")
        create_question()
    else:
        check.config(text = "Wrong answer try again!")

def deleting():
    entry1.delete(0, END)
    entry2.delete(0, END)

def revealing():
    print(num1, num2 , num3, num4, "\n")
    print(round(float(num1 / num2 + num3 / num4), 3), "\n")
    print(round(int(entry1.get()) / int(entry2.get()), 3), "\n")

window = Tk()
window_width = 300
window_height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = LabelFrame(relief = "flat")
frame.grid(padx = padx, pady = pady)

numlabel1 = Label(frame ,text = "1", font = {"size" : size}, width = width)
numlabel1.grid(row = 1, column = 1, padx = padx, pady = pady)
label1 = Label(frame ,text = "-", font = {"size" : size}, width = width)
label1.grid(row = 2, column = 1, padx = padx, pady = pady)
numlabel2 = Label(frame ,text ="2", font = {"size" : size}, width = width)
numlabel2.grid(row = 3, column = 1, padx = padx, pady = pady)

symbollabel = Label(frame ,text ="+", font = {"size" : size}, width = width)
symbollabel.grid(row = 2, column = 2, padx = padx, pady = pady)

numlabel3 = Label(frame ,text ="1", font = {"size" : size}, width = width)
numlabel3.grid(row = 1, column = 3, padx = padx, pady = pady)
label2 = Label(frame ,text = "-", font = {"size" : size}, width = width)
label2.grid(row = 2, column = 3, padx = padx, pady = pady)
numlabel4 = Label(frame ,text ="2", font = {"size" : size}, width = width)
numlabel4.grid(row = 3, column = 3, padx = padx, pady = pady)

equation = Label(frame ,text = "=", font = {"size" : size}, width = width)
equation.grid(row = 2, column = 4, padx = padx, pady = pady)

entry1 = Entry(frame ,width = 5, justify = CENTER, font = {"size" : size})
entry1.grid(row = 1, column = 5, padx = padx, pady = pady)
label3 = Label(frame ,text = "-", font = {"size" : size}, width = width)
label3.grid(row = 2, column = 5, padx = padx, pady = pady)
entry2 = Entry(frame ,width = 5, justify = CENTER, font = {"size" : size})
entry2.grid(row = 3, column = 5, padx = padx, pady = pady)

next = Button(text = "------>", command = player, width = 7)
next.grid(row = 2, pady = 5)

delete = Button(text = "Delete", command = deleting, width = 7)
delete.grid(row = 3, pady = 5)

reveal_nums = Button(text = "Reveal Numbers", command = revealing, width = 12)
reveal_nums.grid(row = 4, pady = 5)

check = Label(text = "------------------------", width = 20)
check.grid(row = 5)

answers = Label(text = "Number of answers : 0", font = {"size" : size})
answers.grid(row = 6)

right_answers = Label(text = "Number of right answers : 0", font = {"size" : size})
right_answers.grid(row = 7)

create_question()

window.bind("<Return>", enter)

window.mainloop()
