import tkinter as tk

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

# add an image background
background_image = tk.PhotoImage(file="dog.png")
background_label = tk.Label(root, image=background_image, bg='#F5F5F5')
background_label.place(relwidth=1, relheight=1)

# create the counter label and buttons
count_label = tk.Label(root, text=str(counter.count), font=("Helvetica", 72), fg="#2E2E2E", bg="#F5F5F5")
count_label.pack(pady=50)

button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack()

button1 = tk.Button(button_frame, text="Reset", font=("Helvetica", 18), fg="#FFFFFF", bg="#CC0000", activebackground="#FF0000", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.reset)
button1.pack(side="left", padx=10)

button2 = tk.Button(button_frame, text="+", font=("Helvetica", 18), fg="#FFFFFF", bg="#00A6FF", activebackground="#0095E2", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.plus)
button2.pack(side="left", padx=10)

button3 = tk.Button(button_frame, text="-", font=("Helvetica", 18), fg="#FFFFFF", bg="#00A6FF", activebackground="#0095E2", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.minus)
button3.pack(side="left", padx=10)




root.mainloop()
