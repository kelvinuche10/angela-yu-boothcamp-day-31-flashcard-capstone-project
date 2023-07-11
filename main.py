from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# <-------- read csv file --------->
csv_file = 'data/french_words.csv'
data_file = pd.read_csv(csv_file)
word_dict = {row.French:row.English for (index, row) in data_file.iterrows()}
rand_french_word = 'trouve'
words_to_learn_list = []
words_to_learn_dict = {}

def flip_card():
	global rand_french_word
	canvas.itemconfig(word_text, text=word_dict[rand_french_word], fill='white')
	canvas.itemconfig(lang_text, text="English", fill='white')
	canvas.itemconfig(bg_image, image=back_image)


def rand_french():
	global rand_french_word, flip_timer
	window.after_cancel(flip_timer)
	rand_french_word = random.choice([key for (key, value) in word_dict.items()])
	canvas.itemconfig(word_text, text=rand_french_word, fill='black')
	canvas.itemconfig(lang_text, text="French", fill='black')
	canvas.itemconfig(bg_image, image=front_image)
	flip_timer = window.after(3000, func=flip_card)

def clear_word():
	global rand_french_word, words_to_learn_dict
	words_to_learn_list.append(rand_french_word)
	words_to_learn_dict = {key:value for (key, value) in word_dict.items() if key not in words_to_learn_list}
	words_to_learn = pd.DataFrame.from_dict(words_to_learn_dict).to_csv('words_to_learn.csv')
	print(words_to_learn)

# <----------- UI setup ----------->

window = Tk()
window.title('Flash card')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
bg_image = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='trouve', font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

cancel_image = PhotoImage(file='images/wrong.png')
cancel_button = Button(image=cancel_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=rand_french)
cancel_button.grid(column=0, row=1)

tick_image = PhotoImage(file='images/right.png')
tick_button = Button(image=tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=clear_word)
tick_button.grid(column=1, row=1)






window.mainloop()