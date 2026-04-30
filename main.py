import os
import random
import string
import json


def load_urls():
    try:
        with open("urls.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return{}

def save_urls(data):
    with open("urls.json", "w") as file:
        json.dump(data, file, indent = 4)


def generate_short_code(existing_urls, length = 6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = ""

        for i in range(length):
            short_code += random.choice(characters)

        if short_code not in existing_urls:
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

urls = load_urls()

while True:
    clear_screen()
    show_menu()

    option = input("Choose an option: ")

    if option == "1":
        clear_screen()

        original_url = input("Enter URL: ")

        code = generate_short_code(urls)

        urls[code] = original_url
        save_urls(urls)

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

