from tkinter import *
import random

answer = 2
answer2 = 0
right_ans = 0
answers_num = 0
symbol = 1

def enter(event):
    next()

def creating_question():
    global answer
    global answer2
    rest.delete(0, END)
    rest.config(state = "disabled")
    symbol = random.randint(1, 5)
    if symbol == 1:
        num1 = random.randint(1, 10000)
        num2 = random.randint(1, 10000)
        answer = num1 + num2
        question.config(text=f"{num1} + {num2} = ?")
    elif symbol == 2:
        num1 = random.randint(1, 10000)
        num2 = random.randint(1, 10000)
        answer = num1 - num2
        question.config(text=f"{num1} - {num2} = ?")
    elif symbol == 3:
        num1 = random.randint(1, 35)
        num2 = random.randint(1, 35)
        answer = num1 * num2
        question.config(text=f"{num1} * {num2} = ?")
    elif symbol == 4:
        num1 = random.randint(1, 15)
        num2 = random.randint(1, 15)
        answer = num1 * num2 / num1
        question.config(text=f"{num1 * num2} / {num1} = ?")
    else:
        num1 = random.randint(99, 999)
        num2 = random.randint(1, 10)
        answer = num1 // num2
        answer2 = num1 % num2
        question.config(text=f"{num1} / {num2} = ?")
        rest.config(state = "normal")

def next():
    global symbol
    global answers_num
    global right_ans
    global answer
    global answer2
    answers_num += 1
    answers.config(text = f"Number of answers: {answers_num}")
    if symbol != 5:
        if answer == int(player.get()):
            player.delete(0, END)
            rest.delete(0, END)
            player.insert(0, "Good job :)")
            rest.insert(0, "Good job :)")
            right_ans += 1
            times.config(text = f"Right answers: {right_ans}")
            creating_question()
        else:
            player.delete(0, END)
            player.insert(0, "Wrong answer try again")
            rest.delete(0, END)
            rest.insert(0, "Wrong answer try again")
    else:
        if answer == int(player.get()) and answer2 == int(rest.get()):
            player.delete(0, END)
            player.insert(0, "Good job :)")
            rest.insert(0, "Good job :)")
            right_ans += 1
            times.config(text=f"Right answers: {right_ans}")
            creating_question()
        else:
            player.delete(0, END)
            player.insert(0, "Wrong answer try again")
            rest.delete(0, END)
            rest.insert(0, "Wrong answer try again")


def clear():
    player.delete(0,END)
    rest.delete(0,END)

window = Tk()
window_width = 300
window_height = 325
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

question = Label(text = "1 + 1 = ?", font = 14)
question.pack(side = TOP, pady = 40, padx = 10)

player = Entry(justify = CENTER, width = 30)
player.pack(side = TOP)

rest = Entry(justify = CENTER, width = 30, state = DISABLED)
rest.pack(side = TOP, pady = 10)

delete = Button(text = "Delete", width = 15, command = clear)
delete.pack(side = TOP)

forward = Button(text = "-->", width = 15, command = next)
forward.pack(side = TOP, pady = 5)

times = Label(text = "Right answers: 0", font = 14)
times.pack(side = TOP, pady = 10, padx = 10)

answers = Label(text = "Number of answers: 0", font = 14)
answers.pack(side = TOP, padx = 10)

window.bind("<Return>", enter)

window.mainloop()