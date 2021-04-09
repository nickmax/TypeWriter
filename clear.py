import os
import platform

#clear optimized for all operating systems
def clear():
    user_os=platform.system()
    if user_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    