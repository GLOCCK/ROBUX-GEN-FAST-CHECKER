from zipfile import ZipFile
from colorama import Fore
import requests
import shutil
import time
import os


r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
ml = Fore.LIGHTMAGENTA_EX
m = Fore.MAGENTA
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE
inf = f"[{c}i{w}]"
err = f"[{r}-{w}]"


def title(content: str):
    os.system(
        f"title Roblox Account Gen   ^|    {content}    ^|   Made by TerrificTable55™#5297")


def github_version():
    try:
        version = requests.get(
            "https://raw.githubusercontent.com/TerrificTable/Roblox-Account-Gen/main/VERSION").text
        return version
    except Exception as e:
        return 'error'


def update():
    choise = input(f"""
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
    {inf} Install or dont install {w}[{g}y{w}/{r}n{w}]
    {w}[{ml}>>>{w}]{w} """)
    choise = choise == choise

    if choise:
        title("Updating")

        try:
            new_version = requests.get(
                "https://github.com/TerrificTable/Roblox-Account-Gen/archive/refs/heads/main.zip")

            with open("Roblox-Account-Gen-main.zip", 'wb')as zipfile:
                zipfile.write(new_version.content)

            with ZipFile("Roblox-Account-Gen-main.zip", 'r') as filezip:
                filezip.extractall()

            os.remove("Roblox-Account-Gen-main.zip")
            cwd = os.getcwd()+'\\Roblox-Account-Gen-main'
            shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
            shutil.rmtree(cwd)

            title("Finished Updating")
            time.sleep(1)
            os.startfile("run.bat")
            exit()
        except Exception as err:
            os.system("cls;clear")
            time.sleep(7)


def updateChecker(local, offical):
    if str(local) == str(offical):
        return
    elif str(local) < str(offical):
        update()


def updateMain(localVer):
    updateChecker(localVer, github_version())
