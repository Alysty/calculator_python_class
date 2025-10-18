import tkinter as tk
from tkinter import ttk

def on_button_click(
    value: str, 
    display: ttk.Entry,
    state: dict[str, str]
):
    
    current_display_value = display.get()


    if value == "C":
        state["first_value"] = ""
        state["operator"] = ""
        display.delete(0,tk.END)
    if value == "←":
        display.delete(len(display.get()) - 1, tk.END)
        #Resets Display if only the '-' is left without numbers
        if display.get() == "-":
            display.delete(0,tk.END)
        return
    if value in "1234567890" or value == ".":
        #check if . already exists or if the user is trying to start a number with .
        if value == "." and (
            "." in current_display_value or current_display_value == ""):
            return
        # prevents useless input like 00 or 000
        if value == "0" and current_display_value == "0":
            return
        display.insert(tk.END, value)
        # moves display to the last typed number
        display.xview_moveto(1)
    if value == "±":
        if current_display_value == "" or current_display_value == 0:
            return
        result_flippled_f = float(current_display_value) * -1
        #this formating after the conversion is because before adding this the 
        #calculator used to add a .0 to integer values even if the user did not
        #intend to type them
        result_flippled = f"{result_flippled_f:g}"
        display.delete(0, tk.END)
        display.insert(tk.END, result_flippled)
    if value in "^/*-+=":
        print("test")
    
