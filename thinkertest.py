import tkinter as tk
import LoggingEngine as le

def move_forward():
    le.log("info","Moving forward",False)


def move_backward():
    le.log("info", "Moving backward", False)


def move_left():
    le.log("info", "Moving left", False)


def move_right():
    le.log("info", "Moving right", False)

def move_up():
    le.log("info", "Moving Up", False)

def move_down():
    le.log("info", "Moving Down", False)


root = tk.Tk()

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=0, column=1)

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.grid(row=2, column=1)

left_button = tk.Button(root, text="Left", command=move_left)
left_button.grid(row=1, column=0)

right_button = tk.Button(root, text="Right", command=move_right)
right_button.grid(row=1, column=2)

up_button = tk.Button(root, text="Up", command=move_up)
up_button.grid(row=5, column=0, pady=30)

down_button = tk.Button(root, text="Down", command=move_down)
down_button.grid(row=5, column=2)

root.mainloop()
