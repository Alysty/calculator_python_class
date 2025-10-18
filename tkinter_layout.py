import tkinter as tk
from tkinter import ttk

def config_app():
    # style fixed
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)
    root.geometry("340x480")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16), padding=10)
    style.configure("TEntry", font=("Arial", 20))

    display = ttk.Entry(root, justify="right")
    display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10, sticky="nsew")
    #state for the calculator to keep in memory
    state = {"first_value": "", "operator": ""}

    # procedural style for the calculator, 
    # so that I don't have to style multiple  buttons
    buttons = [
        ["sin", "cos", "tan", "C"],
        ["^", "±", "/", "*"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", ""],
        ["0", ".", "", ""]
    ]

    for r, row in enumerate(buttons, start=1):
        for c, text in enumerate(row):
            if not text:
                continue
            btn = ttk.Button(root, text=text)
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    equal_btn = ttk.Button(root, text="=")
    equal_btn.grid(row=5, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")

    for i in range(4):
        root.columnconfigure(i, weight=1)
    for i in range(1, len(buttons) + 1):
        root.rowconfigure(i, weight=1)
    return root


