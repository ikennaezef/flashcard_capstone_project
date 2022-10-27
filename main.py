import random
import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_word_set = {}
timer = None

# CHECKING FOR PREVIOUS PROGRESS -----------------------



# SAVING PROGRESS --------------------------------------
def save_word():
    language_list.remove(current_word_set)
    print(len(language_list))
    new_dataframe = pandas.DataFrame(data=language_list)
    new_dataframe.to_csv("data/words_to_learn.csv")


# USING DATA FROM CSV FILE ------------------------------
data = pandas.read_csv("data/french_words.csv")
# language_list = [{row.French: row.English} for (index, row) in data.iterrows()]
language_list = data.to_dict(orient="records")
print(language_list)


# CHANGING FLASHCARD CONTENT --------------------------------
def next_word():
    global current_word_set, timer

    screen.after_cancel(timer)
    card_image.config(file="images/card_front.png")
    current_word_set = random.choice(language_list)
    # french_word = list(word_set.keys())[0]
    french_word = current_word_set["French"]
    canvas.itemconfig(language_text, text="French", fill="Black")
    canvas.itemconfig(word_text, text=french_word, fill="Black")

    # Start Timing
    timer = screen.after(3000, func=flip_card)

    # Save Progress
    save_word()

def flip_card():
    global current_word_set, timer

    english_word = current_word_set["English"]
    card_image.config(file="images/card_back.png")
    canvas.itemconfig(language_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=english_word, fill="White")



# UI SETUP --------------------------------------
screen = tkinter.Tk()
screen.title("Flashcard App")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# CARD
canvas = tkinter.Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=card_image)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 250, text="partie", font=("Arial", 60, "bold"))

# WRONG BUTTON
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_btn = tkinter.Button(image=wrong_image, highlightthickness=0, command=flip_card)
wrong_btn.grid(row=1, column=0)

# RIGHT BUTTON
right_image = tkinter.PhotoImage(file="images/right.png")
right_btn = tkinter.Button(image=right_image, highlightthickness=0, command=next_word)
right_btn.grid(row=1, column=1)


# Start Timing
timer = screen.after(3000, func=flip_card)
# START BY PICKING A CARD
next_word()














screen.mainloop()


