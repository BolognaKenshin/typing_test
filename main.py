import os
import random
import sys
import tkinter as tk

import word_bank

word_list_dict = {
    "current_word": "",
    "current_word_letters": [],
    "entry_letters": [],
    "line_1_delete": [],
    "line_1_display": [],
    "line_1_words": [],
    "line_2_delete": [],
    "line_2_display": [],
    "line_2_words": [],
    "line_3_delete": [],
    "line_3_display": [],
    "line_3_words": [],
    "word_list": word_bank.words,
}

random.shuffle(word_list_dict["word_list"])

window = tk.Tk()
window.minsize(width=900, height=900)
window.configure(background="#ffa384")
window.grid_columnconfigure(index=0, weight=1)
window.title("Speedy-Cat Typing-Tester!")

gif = tk.PhotoImage(file="cat.gif")
frame_count = 25
frames = [tk.PhotoImage(file="cat.gif", format = f'gif -index {i}') for i in range(frame_count)]

corrected_cpm = 0
total_cpm = 0
wpm = 0
time_left = 60
first_key = True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions

def check_answer(current_word, user_submit, corrected_cpm):
    if current_word == list(user_submit):
        corrected_cpm += len(user_submit) + 1
        for letter in word_list_dict["current_word_letters"]:
            word_canvas.itemconfig(letter, fill="blue")
    else:
        for letter in word_list_dict["current_word_letters"]:
            word_canvas.itemconfig(letter, fill="red")
    return corrected_cpm

def check_text_length():
    if len(text_entry.get()) > 20:
        text_entry.delete(20, tk.END)
    window.after(50, check_text_length)

def clear_entry_text(event):
    text_entry.delete(0, tk.END)

def fetch_next_line():
    chars = 30
    line_words = []
    while chars > 0:
        word = word_list_dict["word_list"][0]
        word_list_dict["word_list"].remove(word)
        word_letters = list(word)
        word_letters.append(" ")
        chars -= len(word_letters)
        if chars <= 0:
            return line_words
        line_words.append(word_letters)

def fill_lines():
    word_list_dict["line_1_words"] = fetch_next_line()
    word_list_dict["line_2_words"] = fetch_next_line()
    word_list_dict["line_3_words"] = fetch_next_line()

def final_score(wpm, total_cpm, corrected_cpm):
    score_window = tk.Toplevel(window)
    score_window.grid_columnconfigure(index=0, weight=1)
    score_window.title("Final Score")
    score_window.configure(bg="#ffa384")
    score_window.geometry("350x350")
    t_cpm_label = tk.Label(score_window, text=f'Total CPM: {total_cpm}', font=("Arial", 20, "bold"), bg="#ffa384")
    c_cpm_label = tk.Label(score_window, text=f'Corrected CPM: {corrected_cpm}', font=("Arial", 20, "bold"), bg="#ffa384")
    wpm_label = tk.Label(score_window, text=f'Words per Minute: {wpm}', font=("Arial", 20, "bold"), bg="#ffa384")

    reset_button = tk.Button(score_window, text="      Reset", fg="white", font=("Arial", 14), bd=0,
                             image=word_canvas.button_pic, bg="#ffa384", activebackground="#ffa384",
                             activeforeground="#ffa384", compound="center", highlightthickness=0, command=restart)

    t_cpm_label.grid(row=0, column=0, pady=(50, 10))
    c_cpm_label.grid(row=1, column=0, pady=10)
    wpm_label.grid(row=2, column=0, pady=10)
    reset_button.grid(row=3, column=0, padx=(0, 30), pady=30)

def keep_time_and_score():
    global time_left, timer, corrected_cpm, total_cpm, wpm
    time_left -= 1
    counter = window.after(1000, keep_time_and_score)
    word_canvas.delete(timer)
    timer = word_canvas.create_text(590, 50, text=f'Time Left: {time_left}', font=("Arial", 10, "bold"), fill="white")
    if time_left == 0:
        window.after_cancel(counter)
        final_score(wpm, total_cpm, corrected_cpm)

    word_canvas.itemconfig(cpm_score, text=f'Corrected CPM: {corrected_cpm}')
    time_elapsed = 60 - time_left
    chars_per_second = (corrected_cpm / time_elapsed)
    wpm = int((chars_per_second * 60) / 5)
    word_canvas.itemconfig(wpm_score, text=f"WPM: {wpm}")


def refill_lines():
    word_list_dict["line_2_words"] = fetch_next_line()
    word_list_dict["line_3_words"] = fetch_next_line()
    for letter in word_list_dict["line_1_delete"]:
        word_canvas.delete(letter)
    for letter in word_list_dict["line_2_delete"]:
        word_canvas.delete(letter)
    for letter in word_list_dict["line_3_delete"]:
        word_canvas.delete(letter)


def restart():
    # Get the path to the Python interpreter
    python = sys.executable
    os.execl(python, python, *sys.argv)

def set_up_text():
    l1_x = 125
    l2_x = 125
    l3_x = 125
    first_word = True
    word_list_dict["line_1_display"] = []
    for word in word_list_dict["line_1_words"]:
            if first_word:
                first_word = False
                word_list_dict["current_word"] = word
                for letter in word:
                    display_letter = word_canvas.create_text(l1_x, 115, text=letter, font=("Arial", 22, "bold"), fill="blue")
                    word_list_dict["line_1_display"].append(display_letter)
                    word_list_dict["line_1_delete"].append(display_letter)
                    l1_x += 21
            else:
                for letter in word:
                    display_letter = word_canvas.create_text(l1_x, 115, text=letter, font=("Arial", 22, "bold"), fill="black")
                    word_list_dict["line_1_display"].append(display_letter)
                    word_list_dict["line_1_delete"].append(display_letter)
                    l1_x += 21
    for word in word_list_dict["line_2_words"]:
        for letter in word:
            display_letter = word_canvas.create_text(l2_x, 165, text=letter, font=("Arial", 22, "bold"), fill="black")
            word_list_dict["line_2_display"].append(display_letter)
            word_list_dict["line_2_delete"].append(display_letter)
            l2_x += 21
    for word in word_list_dict["line_3_words"]:
        for letter in word:
            display_letter = word_canvas.create_text(l3_x, 215, text=letter, font=("Arial", 22, "bold"), fill="black")
            word_list_dict["line_3_display"].append(display_letter)
            word_list_dict["line_3_delete"].append(display_letter)
            l3_x += 21

def submit_word():
    global total_cpm, corrected_cpm
    user_submit = text_entry.get()
    total_cpm += len(user_submit) + 1
    text_entry.delete(0, tk.END)
    word_list_dict["entry_letters"] = []
    current_word = word_list_dict["current_word"]
    for i in range(len(word_list_dict["current_word"])):
        word_list_dict["line_1_display"].pop(0)
    current_word.pop()
    word_list_dict["line_1_words"].pop(0)
    if len(word_list_dict["line_1_words"]) > 0:
        corrected_cpm = check_answer(current_word, user_submit, corrected_cpm)
    else:
        corrected_cpm = check_answer(current_word, user_submit, corrected_cpm)
        word_list_dict["line_1_display"] = word_list_dict["line_2_display"]
        word_list_dict["line_1_words"] = word_list_dict["line_2_words"]
        word_list_dict["line_2_words"] = word_list_dict["line_3_words"]
        word_list_dict["line_2_display"] = word_list_dict["line_3_display"]
        word_list_dict["line_3_words"] = []
        word_list_dict["line_3_display"] = []

    if len(word_list_dict["line_2_words"]) == 0 and len(word_list_dict["line_3_words"]) == 0:
        refill_lines()
        set_up_text()
    word_list_dict["current_word"] = word_list_dict["line_1_words"][0]
    word_list_dict["current_word_letters"] = []
    update_current_word_display()

def track_keys(event):
    global first_key
    if first_key:
        first_key = False
        keep_time_and_score()
    if event.char == ' ':
        submit_word()
        return "break"
    elif event.char == '\x08':
        if len(word_list_dict["entry_letters"]) > 0:
            word_list_dict["entry_letters"].pop()
            update_current_word_display()
    elif not event.char.isalpha():
        return "break"
    else:
        current_entry = text_entry.get()
        word_list_dict["entry_letters"] = list(current_entry)
        word_list_dict["entry_letters"].append(event.char)
        update_current_word_display()


def update_current_word_display():
    current_word = word_list_dict["current_word"]
    current_letters = []
    for i in range(len(current_word)):
        current_letters.append(word_list_dict["line_1_display"][i])
    entry_letters = word_list_dict["entry_letters"]
    word_list_dict["current_word_letters"] = current_letters
    for i in range (len(current_letters)):
        if not i < len(entry_letters):
            word_canvas.itemconfig(current_letters[i], fill="blue")
        elif word_canvas.itemcget(current_letters[i], "text") == entry_letters[i]:
            word_canvas.itemconfig(current_letters[i], fill="green")
        else:
            word_canvas.itemconfig(current_letters[i], fill="red")

def update_gif(index):
    frame = frames[index]
    gif_label.configure(image=frame)
    index += 1
    if index == frame_count:
        index = 0
    window.after(20, update_gif, index)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

app_label = tk.Label(text="Speedy-Cat Typing-Tester!", font=("Arial", 28, "bold"), bg="#ffa384", bd=0)
app_label.grid(row=0, column=0, pady=(30, 10))

flames_image = tk.PhotoImage(file="flames.png")
flames_canvas = tk.Canvas(width=900, height=flames_image.height(), bd=0, highlightthickness=0, bg="black")
flames_canvas.flames_image = flames_image
flames_canvas_height = int(flames_image.height() / 2)
flames_canvas.create_image(450, flames_canvas_height, image=flames_image, anchor="center")
flames_canvas.grid(row=1, column=0, pady=(20, 10))
gif_label = tk.Label(image=gif, bd=0)
flames_canvas.create_window(450, 150, window=gif_label, anchor="center")

text_box_image = tk.PhotoImage(file="new_box.png")
word_canvas = tk.Canvas(width=text_box_image.width(), height=text_box_image.height(), bd=0, highlightthickness=0)
text_entry = tk.Entry(width=45, bg="white", font=("Arial", 18), justify="center", fg="#424241")
text_entry.insert(0, "Type here to begin")
text_entry.bind("<FocusIn>", clear_entry_text)
text_entry.bind("<Key>", track_keys)
word_canvas.text_box_image = text_box_image
word_canvas.create_image(0, 0, image=text_box_image, anchor="nw")
word_canvas.create_window(390, 300, window=text_entry)
cpm_score = word_canvas.create_text(190, 50, text=f'Corrected CPM: {corrected_cpm}', font=("Arial", 12, "bold"), fill="white")
wpm_score = word_canvas.create_text(390, 50, text=f'WPM: {wpm}', font=("Arial", 12, "bold"), fill="white")
timer = word_canvas.create_text(590, 50, text=f'Time Left: {time_left}', font=("Arial", 12, "bold"), fill="white")
word_canvas.grid(row=2, column=0, pady=(5, 0))

fish = tk.PhotoImage(file="fish.png")
word_canvas.button_pic = fish
reset_button = tk.Button(text="      Reset", fg="white", font=("Arial", 14), bd=0,
                             image=word_canvas.button_pic, bg="#ffa384", activebackground="#ffa384",
                             activeforeground="#ffa384", compound="center", highlightthickness=0, command=restart)
reset_button.grid(row=3, column=0, padx=(0, 30))

update_gif(0)
check_text_length()
fill_lines()
set_up_text()

window.mainloop()

