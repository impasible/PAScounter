import tkinter as tk

def get_buttons(root, counter):
    button_frame = tk.Frame(root, bg="#F5F5F5")
    button_frame.pack()

    button1 = tk.Button(button_frame, text="Reset", font=("Helvetica", 18), 
                fg="#FFFFFF", bg="#CC0000", activebackground="#FF0000", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.reset)
    button2 = tk.Button(button_frame, text="+", font=("Helvetica", 18), 
                fg="#FFFFFF", bg="#00A6FF", activebackground="#0095E2", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.plus)
    button3 = tk.Button(button_frame, text="-", font=("Helvetica", 18), 
                fg="#FFFFFF", bg="#00A6FF", activebackground="#0095E2", bd=0, highlightthickness=0, pady=10, padx=20, command=counter.minus)
    
    button1.pack(side="left", padx=10)
    button2.pack(side="left", padx=10)
    button3.pack(side="left", padx=10)

    return button1,button2,button3