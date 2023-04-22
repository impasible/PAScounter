import tkinter as tk
from button_prep import get_buttons

class Counter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0
        self.update_label()

    def plus(self):
        self.count += 1
        self.update_label()

    def minus(self):
        self.count -= 1
        self.update_label()

    def update_label(self):
        count_label.config(text=str(self.count))

counter = Counter()

root = tk.Tk()
root.title("PAScount")
root.geometry("400x400")
root.configure(background="#F5F5F5")

#add background
background_image = tk.PhotoImage(file="resources/background_dis.png")
background_label = tk.Label(root, image=background_image, bg='#F5F5F5')
background_label.place(relwidth=1, relheight=1)

# create the counter label and buttons
count_label = tk.Label(root, text=str(counter.count), font=("Helvetica", 72), fg="#2E2E2E", bg="#F5F5F5")
count_label.pack(pady=50)

button1,button2,button3 = get_buttons(root,counter)

root.mainloop()
