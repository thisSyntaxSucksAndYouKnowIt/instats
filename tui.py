import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def title_screen():
    print("")
    print("  _____           _        _       ")
    print(" |_   _|         | |      | |      ")
    print("   | |  _ __  ___| |_ __ _| |_ ___ ")
    print("   | | | '_ \/ __| __/ _` | __/ __|")
    print("  _| |_| | | \__ \ || (_| | |_\__ \\")
    print(" |_____|_| |_|___/\__\__,_|\__|___/")
    print("")
