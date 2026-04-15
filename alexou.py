
from colorama import Fore, Style, init


init(autoreset=True)

WIDTH = 30


def frame_line() -> str:
	return "═" * WIDTH


def center(text: str) -> str:
	return text.center(WIDTH)


title = " ACCESS NOTICE "
message = "This file has expired.\nPlease contact :@vishaldied for Paid Access."
contact = "Contact: @vishaldied"

print(Fore.RED + Style.BRIGHT + frame_line())
print(Fore.RED + Style.BRIGHT + center(title))
print(Fore.RED + Style.BRIGHT + frame_line())
print()
print(Fore.YELLOW + Style.BRIGHT + center("⚠  " + message))
print(Fore.CYAN + center(contact))
print()
print(Fore.RED + frame_line())
