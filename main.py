import os
import random
import string

def generate_short_code(length = 6):
    characters = string.ascii_letters + string.digits
    short_code = ""

    for i in range(length):
        short_code += random.choice(characters)
    return short_code


def clear_screen():
    os.system("cls")

def show_menu():
    print("""
    URL Shortener CLI
    
    [1] Shorten URL
    [2] List URLs
    [3] Find URL
    [4] Exit
    => 
    """)

while True:
    clear_screen()
    show_menu()

    option = input("Choose an option: ")

    if option == "1":
        code = generate_short_code()
        print(f"Generated code: {code}")
        input("Press Enter to continue...")
    elif option == "2":
        print("List URLs")
        input("Press Enter to continue...")

    elif option == "3":
        print("Find URL")
        input("Press Enter to continue...")

    elif option == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
        input("Press Enter to continue...")

