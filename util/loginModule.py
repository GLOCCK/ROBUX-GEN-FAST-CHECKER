import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from plyer import notification
from selenium import webdriver
from colorama import Fore
import random
import time


months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
y = Fore.LIGHTYELLOW_EX
w = Fore.WHITE


def main(bot, username, password, timeout, config=None):
    try:
        day = Select(bot.find_element_by_xpath('//*[@id="DayDropdown"]'))
    except:
        main(bot, username, password, timeout, config)
    month = Select(bot.find_element_by_xpath('//*[@id="MonthDropdown"]'))
    year = Select(bot.find_element_by_xpath('//*[@id="YearDropdown"]'))
    usernameInput = bot.find_element_by_xpath('//*[@id="signup-username"]')
    passwordInput = bot.find_element_by_xpath('//*[@id="signup-password"]')
    register = bot.find_element_by_xpath('//*[@id="signup-button"]')
    accept = bot.find_element_by_xpath(
        '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')

    # Dob - Day Selector
    dayVal = random.randint(1, 27)
    if dayVal < 10:
        dayVal = "0" + str(dayVal)
    day.select_by_value(str(dayVal))

    # Dob - Month Selector
    monthVal = random.choice(months)
    month.select_by_visible_text(str(monthVal))

    # Dob - Year Selector
    yearVal = random.randint(1960, 2010)
    year.select_by_visible_text(str(yearVal))

    # Username
    usernameInput.clear()
    usernameInput.send_keys(username)

    # Password
    passwordInput.clear()
    passwordInput.send_keys(password)

    # Register
    try:
        accept.click()
        time.sleep(1)
        register.click()
        time.sleep(timeout)

        # try:
        #     bot.find_element_by_xpath('//*[@id="header"]/div/ul[1]/li[2]/a')
        # except:
        #     try:
        #         bot.find_element_by_xpath('//*[@id="signup-button"]')
        #         log(username, password, None)
        #     except:
        #         time.sleep(1)
        #         checker(bot, username, password, config)
        #     time.sleep(3)

        checker(bot, username, password, config)
    except Exception as e:
        print("ERROR, " + e)
        bot.close()

# time.sleep(1)
# try:
#     invalid = bot.find_element_by_xpath(
#         '//*[@id="signup-usernameInputValidation"]')  # /text()

#     if invalid != None or str(invalid) != "":
#         print(invalid)
#         log(username, password, None, config)
#         # bot.close()
# except Exception as e:
#     print("unavailable " + e)
#     # log(username, password, True, config)
#     pass


def checker(bot, username: str, password: str, config=None) -> None:
    bot.get("https://www.roblox.com/login")
    # time.sleep(2)

    try:
        bot.find_element_by_xpath('//*[@id="header"]/div/ul[1]/li[2]/a')
    except:
        try:
            bot.find_element_by_xpath('//*[@id="login-username"]')
        except:
            checker(bot, username, password, config)
        checker(bot, username, password, config)

    try:
        usernameInput = bot.find_element_by_xpath('//*[@id="login-username"]')
        passwordInput = bot.find_element_by_xpath('//*[@id="login-password"]')
        login = bot.find_element_by_xpath('//button[@id="login-button"]')
        try:
            accept = bot.find_element_by_xpath(
                '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')
        except:
            print("Accept element cant be located")

        # Username
        usernameInput.clear()
        usernameInput.send_keys(username)

        # Password
        passwordInput.clear()
        passwordInput.send_keys(password)

        # Login
        time.sleep(2)
        accept.click()
        time.sleep(1)
        bot.execute_script("arguments[0].click();", login)
        bot.manage().timeouts().implicitlyWait()
        time.sleep(1)

        try:
            if str(bot.find_element_by_xpath('//p[@class="form-control-label xsmall text-error login-error ng-binding"]')) != "":
                log(username, password, False)
                bot.close()
            else:
                log(username, password, True, config)
                bot.close()
        except:
            log(username, password, True, config)
            bot.close()

    except:
        log(username, password, True, config)
        bot.close()


def log(username, password, valid, config=None) -> None:
    if valid == True:
        print(f"\n[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {g}Valid{w}\n")

        with open("./logins.txt", "a") as f:
            f.write(f"[Info] {username}:{password}\n")

        if config != None and config["options"]["NOTIFICATIONS"] == "True":
            def notifyMe(title, message, icon=None):
                notification.notify(title=title, message=message,
                                    app_icon=icon, timeout=10)

            notifyMe("Roblox Account Generator",
                     f"Account Generated Username: {username} Password: {password}", "./assets/icon.ico")

    elif valid == False:
        print(f"\n[{g}Username{w}] {y}{username}{w} \n[{b}Password{w}] {y}{password}{w} \n[{m}Account-Valid{w}] {r}Invalid{w}\n")

    elif valid == None:
        print(f"\n[{r}Username Unavalable or Inapropreat{w}]")

    else:
        pass


def login(username: str, password: str, timeout: int, proxyList, headless: bool = True, config=None) -> None:
    options = Options()
    options.headless = headless

    if proxyList != None:
        proxy = random.choice(proxyList)
        options.add_argument(f'--proxy-server={proxy}')
        time.sleep(12)

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    bot = webdriver.Chrome(chrome_options=options)
    bot.get("https://roblox.com")

    try:
        bot.find_element_by_xpath(
            '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')
    except:
        try:
            bot.find_element_by_xpath('//*[@id="DayDropdown"]')
        except:
            login(username, password, timeout, proxyList, headless)
        login(username, password, timeout, proxyList, headless)

    if len(username) > 20:
        username = str(username[:20])

    try:
        main(bot, username, password, timeout, config)
    except Exception as e:
        print(e)
        bot.close()
