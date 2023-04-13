from tkinter import *
import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
BACK_FC_TEXT_COLOR = "#90C2AF"

try:
    with open("./data/words_to_learn.csv") as words_learn:
        jpn = pd.read_csv("./data/words_to_learn.csv")
        to_learn = jpn.to_dict(orient="records")
except FileNotFoundError:
    jpn = pd.read_csv('./data/Japanese n3.csv')
    to_learn = jpn.to_dict(orient="records")

print(to_learn)
current_card = {}


def new_word():
    global current_card
    current_card = random.choice(to_learn)
    title.config(text="Japanese", bg="white", fg="black")
    word.config(text=current_card["Japanese"], bg="white", fg="black")
    canvas.itemconfig(canvas_image, image=flashcard_front)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    new_word()


def change_image():
    canvas.itemconfig(canvas_image, image=flashcard_back)
    title.config(text="English", bg=BACK_FC_TEXT_COLOR, fg="white")
    word.config(text=current_card["English"], bg=BACK_FC_TEXT_COLOR, fg="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="./images/card_front.png")
flashcard_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410, 270, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=3)

x = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x, highlightthickness=0, command=new_word)
x_button.grid(row=1, column=0)
y = PhotoImage(file="./images/right.png")
y_button = Button(image=y, highlightthickness=0, command=is_known)
y_button.grid(row=1, column=2)

flip = Button(text="FLIP",width=15, command=change_image)
flip.grid(row=1, column=1)


title = Label(text="", font=("Ariel", 40, "italic"), bg="white")
title.place(x=400, y=150, anchor="center")
word = Label(text="", font=("Ariel", 60, "bold"), bg="white")
word.place(x=400, y=263, anchor="center")


new_word()

window.mainloop()
