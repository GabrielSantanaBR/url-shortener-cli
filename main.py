import os
import random
import string
import json


def shorten_url(urls):
    clear_screen()

    original_url = input("Enter URL: ")

    if not is_valid_url(original_url):
        print("Invalid URL. The URL must start with http:// or https://")
        pause()
        return

    code = generate_short_code(urls)

    urls[code] = {
        "url": original_url,
        "clicks": 0
    }
    save_urls(urls)

    print(f"Generated code: {code}")
    pause()

def list_urls(urls):
    clear_screen()

    if not urls:
        print("No URLs found.")
    else:
        print("Stored URLs:\n")

        for code, data in urls.items():
            print(f"{code}: {data['url']} | Clicks: {data['clicks']}")

    pause()

def find_url(urls):
    clear_screen()

    code = input("Enter short code: ")

    if code in urls:
        urls[code]["clicks"] += 1
        save_urls(urls)

        print(f"Original URL: {urls[code]['url']}")
        print(f"Clicks: {urls[code]['clicks']}")
    else:
        print("URL not found.")

    pause()

def delete_url(urls):
    clear_screen()

    code = input("Enter short code to delete: ")

    if code in urls:
        del urls[code]
        save_urls(urls)
        print("URL deleted successfully.")
    else:
        print("URL not found.")

    pause()

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def pause():
    input("\nPress Enter to continue...")

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

if __name__ == "__main__":
    urls = load_urls()
    while True:
        clear_screen()
        show_menu()

        option = input("Choose an option: ")

        if option == "1":
            shorten_url(urls)

        elif option == "2":
           list_urls(urls)

        elif option == "3":
            find_url(urls)

        elif option == "4":
            delete_url(urls)

        elif option == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option.")
            pause()

