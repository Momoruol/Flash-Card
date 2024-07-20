from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data = {}

try:
    file = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_file = pd.read_csv('data/french_words.csv')
    data = original_file.to_dict(orient='records')
else:
    data = file.to_dict(orient='records')


#Word learned
def checked_word():
    data.remove(random_word)
    print(len(data))

    arquive = pd.DataFrame(data)
    arquive.to_csv('data/words_to_learn.csv', index=False)

    next_card()

#Random card generator
def next_card():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)

    random_word = random.choice(data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=random_word['French'], fill='black')
    canvas.itemconfig(card_background, image=img)

    flip_timer = window.after(3000, func=time_config)

#time config

def time_config():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=random_word['English'], fill='white')
    canvas.itemconfig(card_background, image=img_flip)


#UI Section
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=time_config)

#Canvas image
canvas = Canvas(width=800, height=526, highlightthickness=0)
img = PhotoImage(file='images/card_front.png')
img_flip = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 278, image=img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


#Canvas Text
card_title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400,263, text='Word', font=('Arial', 60, 'bold'))

#Card buttons
img_x_button = PhotoImage(file='images/wrong.png')
x_button = Button(image = img_x_button, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

img_v_button = PhotoImage(file='images/right.png')
v_button = Button(image=img_v_button, highlightthickness=0, command=checked_word)
v_button.grid(row=1, column=1)

next_card()

window.mainloop()