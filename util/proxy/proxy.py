import colorama
import requests
import time
import os


def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def proxy_scrape():
    startTime = time.time()
    temp = os.getenv("temp")+"\\proxies.txt"
    print(f"{colorama.Fore.YELLOW}Please wait while we Scraped proxies for you!")
    r = requests.get(
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=8500&country=all&ssl=all&anonymity=elite&simplified=true", headers=getheaders())
    with open(temp, "wb") as f:
        f.write(r.content)
    execution_time = (time.time() - startTime)
    print(f"{colorama.Fore.GREEN}Done scraping proxies => {temp}{colorama.Fore.RESET} | {execution_time}ms")


def proxy():
    temp = os.getenv("temp")+"\\proxies.txt"
    if not os.path.exists(temp):
        with open(temp, "w") as f:
            f.close()
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[1]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy
