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
    print(" Made by: https://github.com/thisSyntaxSucksAndYouKnowIt")
    print(" Second version, the first was lost when my hard drive broke")
    print("")


def main_menu(lists):
    print("")
    print(" a: collect likers from specific post")
    print(" b: sort profiles collected " + str(len(lists.likers_collected)))
    print(" c: mass like from sorted list " + str(len(lists.likers_collected_clean)))
    print(" d: collect followers from specific profile")
    print(" e: sort " + str(len(lists.followers_collected)) + " followers collected from: " + str(lists.user_name_followers))
    print(" f: collect following from specific profile")
    print(" g: sort " + str(len(lists.following_collected)) + " followers collected from: " + str(lists.user_name_following))
    print(" q: quit instats")
    print("")
