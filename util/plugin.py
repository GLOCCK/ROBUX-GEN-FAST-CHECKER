from colorama import Fore
import os


r = Fore.RED
rl = Fore.LIGHTRED_EX
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
ml = Fore.LIGHTMAGENTA_EX
m = Fore.MAGENTA
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


def title(content: str):
    os.system(
        f"title Roblox Account Gen   ^|    {content}    ^|   Made by TerrificTable55™#5297")


def clear():
    os.system("cls;clear")


class debug:
    @staticmethod
    def inp(text):
        inpu = input(f"{w}[{m}>{w}] {text}")
        return inpu

    @staticmethod
    def info(text):
        print(f"{w}[{c}i{w}] {text}")

    @staticmethod
    def error(text):
        print(f"{w}[{r}!{w}] {text}")

    @staticmethod
    def warning(text):
        print(f"{w}[{rl}-{w}] {text}")

    @staticmethod
    def log(text):
        print(f"{w}[{g}={w}] {text}")
