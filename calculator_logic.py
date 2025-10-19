import tkinter as tk
import math
from tkinter import ttk

def on_button_click(
    value: str, 
    display: ttk.Entry,
    state: dict[str, str]
):
    current_display_value = display.get()

    #resets the calculator to the inital state
    if value == "C" or current_display_value == "ERROR":
        state["first_value"] = ""
        state["operator"] = ""
        display.delete(0,tk.END)

    #removes the right most digit
    if value == "←":
        display.delete(len(display.get()) - 1, tk.END)
        #Resets Display if only the '-' is left without numbers
        if display.get() == "-":
            display.delete(0,tk.END)
        return
    
    #add values to the calculator screen
    if value in "1234567890" or value == ".":
        add_number_or_dot(value, display)
    
    #inver the sign of the number
    if value == "±":
        invert_sign(display)

    #stores the operation and number that will be used with the second number
    if value in "^/*-+":
        state["first_value"] = current_display_value
        state["operator"] = value
        display.delete(0,tk.END)

    #run the calculation
    if value in "=cossintan":
        equals_operation(value, display, state)
        return


def add_number_or_dot(value: str, display: ttk.Entry):
    current_display_value = display.get()
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
    return


def invert_sign(display: ttk.Entry):
    current_display_value = display.get()
    if current_display_value == "" or current_display_value == 0:
            return
    result_flippled_f = float(current_display_value) * -1
    #this formating after the conversion is necessary because
    #before adding this, the calculator used to add a .0 to integer values 
    #even if the user did not intend to type them
    result_flippled = f"{result_flippled_f:g}"
    display.delete(0, tk.END)
    display.insert(tk.END, result_flippled)
    return


def equals_operation(
    value: str,
    display: ttk.Entry,
    state: dict[str, str]
):
    result: float = 0.0
    current_display_value = display.get()
    if current_display_value == "":
        return
    #receives values as radian, not degrees
    if value in "cossintan":
        match value:
            case "cos":
                result = math.cos(float(current_display_value))
            case "sin":
                result = math.sin(float(current_display_value))
            case "tan":
                result = math.tan(float(current_display_value))
        result_str: str = f"{result:g}"
        state["first_value"] = ""
        state["operator"] = ""
        display.delete(0,tk.END)
        display.insert(tk.END, result_str)

    # make sure at least 1 number and 1 value are typed for operations that need two numbers
    if state["operator"] == "" or state["first_value"] == "":
            return

    match state["operator"]:
        case "+":
            result = float(state["first_value"]) + float(current_display_value)
        case "-":
            result = float(state["first_value"]) - float(current_display_value)
        case "*":
            result = float(state["first_value"]) * float(current_display_value)
        case "/":
            if float(current_display_value) == 0.0:
                display.delete(0,tk.END)
                display.insert(tk.END, "ERROR")
                return 
            result = float(state["first_value"]) / float(current_display_value)
        case "^":
            result = float(state["first_value"]) ** float(current_display_value)
        case _:
            display.delete(0,tk.END)
            display.insert(tk.END, "ERROR")
            return
    result_str: str = f"{result:g}"
    state["first_value"] = ""
    state["operator"] = ""
    display.delete(0,tk.END)
    display.insert(tk.END, result_str)
