import os
import random
import string
import json

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")


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
    [4] Delete URL
    [0] Exit
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
        if not is_valid_url(original_url):
            print("Invalid URL. The URL must start with http:// or https://")
            input("Press Enter to continue...")
            continue

        code = generate_short_code(urls)

        urls[code] = {
            "url": original_url,
            "clicks": 0
        }
        save_urls(urls)

        print(f"Generated code: {code}")
        input("Press Enter to continue...")

    elif option == "2":
        clear_screen()

        print("List URLs")
        if not urls:
            print("No URLs found.")
        else:
            print("Stored URLs:\n")

            for code, data in urls.items():
                print(f"{code}: {data["url"]} | Clicks: {data['clicks']}")
        input("Press Enter to continue...")

        input("Press Enter to continue...")

    elif option == "3":

        clear_screen()

        code = input("Enter short code: ")

        if code in urls:
            urls[code]["clicks"]+=1
            save_urls(urls)

            print(f"Original URL: {urls[code]['url']}")
            print(f"Clicks: {urls[code]['clicks']}")
        else:
            print("URL not found.")

        input("\nPress Enter to continue...")

    elif option == "4":
        clear_screen()

        code = input("Enter short code delete: ")

        if code in urls:
            del urls[code]
            save_urls(urls)
            print("URL deleted successfully")
        else:
            print("URL not found")

        input("\nPress Enter to continue...")

    elif option == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
        input("Press Enter to continue...")

