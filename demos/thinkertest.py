import random
import tkinter as tk
import LoggingEngine as le
import time


def move_forward():
    le.log("info", "Moving forward", False)


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


def update_status_number():

    random_number = random.randint(1, 100)
    random_x = random.randint(0, 255)
    random_y = random.randint(0, 255)
    random_z = random.randint(0, 255)

    le.log("info", "Random Status Number : " + str(random_number), False)
    status.config(text="Random Status Number : " + str(random_number))

    le.log("info", "Random X : " + str(random_x), False)
    x.config(text="Random X : " + str(random_x))

    le.log("info", "Random Y : " + str(random_y), False)
    y.config(text="Random Y : " + str(random_y))

    le.log("info", "Random Z : " + str(random_z), False)
    z.config(text="Random Z : " + str(random_z))

    statuswindow.after(1000, update_status_number)


def update_color():
    random_color = "#" + str("%06x" % random.randint(0, 0xFFFFFF))
    le.log("info", "Random Color HEX : " + str(random_color), False)
    randomcolorwindow.config(bg=random_color)
    randomcolorwindow.after(100, update_color)


le.log("info", "Starting TK", False)
loadtime = time.time()

root = tk.Tk()
statuswindow = tk.Tk()
randomcolorwindow = tk.Tk()

root.title("Robot Control Panel")
statuswindow.title("Status Window")
randomcolorwindow.title("Color Sensor?")

# statuswindow.geometry("300x100")
randomcolorwindow.geometry("200x200")

header = tk.Label(root, text="Robot Control Panel", font=("Arial", 16, "bold"))
header.grid(row=0, column=0, columnspan=3)

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=1, column=1)

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.grid(row=3, column=1)

left_button = tk.Button(root, text="Left", command=move_left)
left_button.grid(row=2, column=0)

right_button = tk.Button(root, text="Right", command=move_right)
right_button.grid(row=2, column=2)

up_button = tk.Button(root, text="Up", command=move_up)
up_button.grid(row=6, column=0, pady=15)

down_button = tk.Button(root, text="Down", command=move_down)
down_button.grid(row=6, column=2)

le.log("info", "Started TK", False)
le.log("info", "TK Load Time: " + str(time.time() - loadtime), False)

status = tk.Label(statuswindow, text="", font=("Arial", 16, "bold"))
status.grid(row=1, column=0, columnspan=3)

x = tk.Label(statuswindow, text="", font=("Arial", 16, "bold"))
x.grid(row=2, column=0, columnspan=3)

y = tk.Label(statuswindow, text="", font=("Arial", 16, "bold"))
y.grid(row=3, column=0, columnspan=3)

z = tk.Label(statuswindow, text="", font=("Arial", 16, "bold"))
z.grid(row=4, column=0, columnspan=3)
update_color()

update_status_number()  # Initial call to the function

root.mainloop()
