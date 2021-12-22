from tkinter import *
import pandas as pd
import random

# Open Data File and Convert to Dict
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("words.csv")
finally:
    data = data.to_dict(orient="records")
    current_card = {}


def flip_card():
    # Update Language, Translate word and Canvas image
    new_translate = current_card["Turkish"].title()
    canvas.itemconfig(canvas_photo, image=card_back_png)
    canvas.itemconfig(language, text="Turkish", fill="white")
    canvas.itemconfig(word, text=new_translate, fill="white")


def next_word():
    global timer, current_card
    # Cancel Timer
    window.after_cancel(timer)

    # Chose a random word from data file
    current_card = random.choice(data)
    new_word = current_card["English"].title()

    # Update Language and Update word and Canvas Image
    canvas.itemconfig(canvas_photo, image=card_front_png)
    canvas.itemconfig(language, text="English", fill="black")
    canvas.itemconfig(word, text=new_word, fill="black")
    timer = window.after(3000, flip_card)


def is_known():
    data.remove(current_card)
    new_data = pd.DataFrame(data)
    new_data.to_csv("words_to_learn.csv")
    next_word()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Define Photos
card_back_png = PhotoImage(file="card_back.png")
card_front_png = PhotoImage(file="card_front.png")
wrong_png = PhotoImage(file="wrong.png")
right_png = PhotoImage(file="right.png")

# Canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_photo = canvas.create_image(400, 263, image=card_front_png)
language = canvas.create_text(400, 180, text="English", font=("Times", "30", "italic"))
word = canvas.create_text(400, 263, text="", font=("Times", "40", "bold"))
canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

# Define and Grid Buttons
wrong_button = Button(image=wrong_png, highlightthickness=0, borderwidth=0, command=next_word)
right_button = Button(image=right_png, highlightthickness=0, borderwidth=0, command=is_known)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# First time, run  functions
timer = window.after(3000, flip_card)
next_word()


window.mainloop()
