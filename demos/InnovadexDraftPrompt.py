# Import Libs
from LoggingEngine import log
import tkinter as tk

# Declare Vars
objcount = 0
on = False

# Checks
if not isinstance(objcount, int):
    log("fatal", "Unknown \"objcount\" value.", True)
if not isinstance(on, bool):
    log("fatal", "Unknown \"on\" value.", True)
if objcount < 0:
    log("fatal", "objcount is less than 0.", True)
# Declare Funcs


def counterreset():
    log("info", "counterreset() called.", False)
    global objcount
    objcount = 0


def start():
    global on
    if not isinstance(on, bool):
        log("fatal", "Unknown \"on\" value when running start()", True)
    elif on:
        log("warn", "System already started when start() called.", False)
    elif not on:
        log("info", "Starting system.", False)
        on = True


def stop():
    global on
    if not isinstance(on, bool):
        log("fatal", "Unknown \"on\" value when running stop()", True)
    elif not on:
        log("warn", "System already stopped when stop() called.", False)
    elif on:
        log("info", "Stopping system.", False)
        on = False



def updatecounter():
    ConPanCount.config(text="Items Count : " + str(objcount))
    ConPanCount.after(100, updatecounter)


def updateonstatus():
    global on
    if not isinstance(on, bool):
        log("fatal", "Unknown \"on\" value when running updateonstatus()", True)
    if on:
        ConPanOnStatus.config(text="System is ON", fg="chartreuse")
    elif not on:
        ConPanOnStatus.config(text="System is OFF", fg="red")
    ConPanOnStatus.after(100, updateonstatus)


# Make Window
root = tk.Tk()
root.title("Local Control Panel")
# root.geometry("500x500")

ConPanTitle = tk.Label(root, text="Local Control Panel", font=("Arial", 20, "bold"))
ConPanTitle.grid(row=0, column=0, columnspan=3)

ConPanCount = tk.Label(root, text="Items Count : " + str(objcount), font=("Arial", 18), fg="green")
ConPanCount.grid(row=1, column=0, columnspan=3)

ConPanOnStatus = tk.Label(root, font=("Arial", 18))
ConPanOnStatus.grid(row=2, column=0, columnspan=3)

ConPanStartButton = tk.Button(root, text="Start", command=start)
ConPanStartButton.grid(row=3, column=0, pady=20, padx=10)

ConPanStopButton = tk.Button(root, text="Stop", command=stop)
ConPanStopButton.grid(row=3, column=2, pady=20, padx=10)

ConPanResetButton = tk.Button(root, text="Reset Counter", command=counterreset)
ConPanResetButton.grid(row=4, column=1, pady=10)

updatecounter()
updateonstatus()

root.mainloop()
