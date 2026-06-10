import os
import random
import string


def is_valid_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choice(characters) for _ in range(length))

        from database import code_exists

        if not code_exists(code):
            return code


def clear_screen() -> None:
    os.system("cls")


def pause() -> None:
    input("Press Enter...")