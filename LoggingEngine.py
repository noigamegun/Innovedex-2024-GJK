import datetime
from colorama import Fore, Back, Style

def log(logtype, message,kill):
    output = ""
    output += str(datetime.datetime.now())

    if str(logtype) == "info":
        output += " [INFO] "
    elif str(logtype) == "warn":
        output += " [WARN] "
    elif str(logtype) == "error":
        output += " [ERROR] "
    elif str(logtype) == "fatal":
        output += " [FATAL] "

    output += str(message)
    if str(logtype) == "info":
        print(output)
    elif str(logtype) == "warn":
        print(Fore.YELLOW + output + Style.RESET_ALL)
    elif str(logtype) == "error":
        print(Fore.RED + output + Style.RESET_ALL)
    elif str(logtype) == "fatal":
        print(Fore.BLACK + Back.RED + output + Style.RESET_ALL)

    if kill:
        exit(0)
