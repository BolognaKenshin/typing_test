import tkinter as tk
import word_bank
import random

word_list = word_bank.words
random.shuffle(word_list)

window = tk.Tk()
window.minsize(width=900, height=850)
window.configure(background="#ffa384")
window.grid_columnconfigure(index=0, weight=1)
window.title("Typing Test!")

gif = tk.PhotoImage(file="cat.gif")
frame_count = 25
frames = [tk.PhotoImage(file="cat.gif", format = f'gif -index {i}') for i in range(frame_count)]

corrected_cpm = 0
wpm = 0
time_left = 60

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions

def check_text_length():
    if len(text_entry.get()) > 20:
        text_entry.delete(20, tk.END)
    window.after(50, check_text_length)

def fetch_next_line():
    global word_list
    line = ""
    chars = 35
    words = []
    for word in word_list:
        chars -= (len(word) + 1)
        if chars <= 0:
            return line
        line += (word + " ")
        words.append(word + " ")
        word_list.remove(word)

def set_up_text():
    word_canvas.create_text(390, 115, text=fetch_next_line(), font=("Arial", 22, "bold"), anchor="center")
    word_canvas.create_text(390, 165, text=fetch_next_line(), font=("Arial", 22, "bold"), anchor="center")
    word_canvas.create_text(390, 215, text=fetch_next_line(), font=("Arial", 22, "bold"), anchor="center")

def update_gif(index):
    frame = frames[index]
    gif_label.configure(image=frame)
    index += 1
    if index == frame_count:
        index = 0
    window.after(20, update_gif, index)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

app_label = tk.Label(text="Carl's Type-Palooza!", font=("Arial", 28, "bold"), bg="#ffa384", bd=0)
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
text_entry = tk.Entry(width=45, bg="white", font=("Arial, 18"), justify="center")
word_canvas.text_box_image = text_box_image
word_canvas.create_image(0, 0, image=text_box_image, anchor="nw")
word_canvas.create_window(390, 300, window=text_entry)
cpm_score = word_canvas.create_text(190, 50, text=f'Corrected CPM: {corrected_cpm}', font=("Arial", 10, "bold"), fill="white")
wpm_score = word_canvas.create_text(390, 50, text=f'WPM: {wpm}', font=("Arial", 10, "bold"), fill="white")
timer = word_canvas.create_text(590, 50, text=f'Time Left: {time_left}', font=("Arial", 10, "bold"), fill="white")
word_canvas.grid(row=2, column=0, pady=(20, 0))

reset_button = tk.Button(text="Reset", font=("Arial", 10))
reset_button.grid(row=3, column=0)

update_gif(0)
check_text_length()
set_up_text()
window.mainloop()

































