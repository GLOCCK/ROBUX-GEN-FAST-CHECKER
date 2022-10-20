from typing import Any, Dict, Iterable, Literal, Optional, Tuple
from maxminddb import open_database
from maxminddb.reader import Reader
from ipaddress import IPv4Address
from threading import Thread
from shutil import rmtree
from loguru import logger
from requests import get
from time import sleep
from sys import stderr
from os import mkdir
import config


class ProxyScraperChecker:
    def __init__(
        self,
        timeout: float = 5,
        geolite2_city_mmdb: str = None,
        ip_service: str = "https://ident.me",
        http_sources: Iterable[str] = None,
        socks4_sources: Iterable[str] = None,
        socks5_sources: Iterable[str] = None,
    ) -> None:
        """Scrape and check proxies from sources and save them to files.

        Args:
            geolite2_city_mmdb (str): Path to the GeoLite2-City.mmdb if you
                want to add location info for each proxy.
            ip_service (str): Service for getting your IP address and checking
                if proxies are valid.
            timeout (float): How many seconds to wait for the connection.
        """
        self.IP_SERVICE = ip_service.strip()
        self.TIMEOUT = timeout
        self.MMDB = geolite2_city_mmdb
        self.SOURCES = {
            proto: (sources,)
            if isinstance(sources, str)
            else tuple(set(sources))
            for proto, sources in (
                ("http", http_sources),
                ("socks4", socks4_sources),
                ("socks5", socks5_sources),
            )
            if sources
        }
        self.proxies: Dict[str, Dict[str, Optional[str]]] = {
            proto: {} for proto in self.SOURCES
        }

    @staticmethod
    def is_ipv4(ip: str) -> bool:
        """Return True if ip is IPv4."""
        try:
            IPv4Address(ip)
        except Exception:
            return False
        return True

    @staticmethod
    def append_to_file(file_path: str, content: str) -> None:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{content}\n")

    @staticmethod
    def get_geolocation(ip: str, reader: Reader) -> str:
        """Get proxy's geolocation.

        Args:
            ip (str): Proxy's ip.
            reader (Reader): mmdb Reader instance.

        Returns:
            str: ::Country Name::Region::City
        """
        geolocation = reader.get(ip)
        if not isinstance(geolocation, dict):
            return "::None::None::None"
        country = geolocation.get("country")
        if country:
            country = country["names"]["en"]
        else:
            country = geolocation.get("continent")
            if country:
                country = country["names"]["en"]
        region = geolocation.get("subdivisions")
        if region:
            region = region[0]["names"]["en"]
        city = geolocation.get("city")
        if city:
            city = city["names"]["en"]
        return f"::{country}::{region}::{city}"

    def start_threads(self, threads: Iterable[Thread]) -> None:
        """Start and join threads."""
        for t in threads:
            try:
                t.start()
            except RuntimeError:
                sleep(self.TIMEOUT)
                t.start()
        for t in threads:
            t.join()

    def get_source(
        self, source: str, proto: Literal["http", "socks4", "socks5"]
    ) -> None:
        """Get proxies from source.

        Args:
            source (str): Proxy list URL.
            proto (str): http/socks4/socks5.
        """
        try:
            r = get(source.strip(), timeout=15)
        except Exception as e:
            logger.error(f"{source}: {e}")
            return
        status_code = r.status_code
        if status_code == 200:
            for proxy in r.text.splitlines():
                proxy = (
                    proxy.replace(f"{proto}://", "")
                    .replace("https://", "")
                    .strip()
                )
                if self.is_ipv4(proxy.split(":")[0]):
                    self.proxies[proto][proxy] = None
        else:
            logger.error(f"{source} status code: {status_code}")

    def check_proxy(
        self, proxy: str, proto: Literal["http", "socks4", "socks5"]
    ) -> None:
        """Check proxy validity.

        Args:
            proxy (str): ip:port.
            proto (str): http/socks4/socks5.
        """
        try:
            exit_node = get(
                self.IP_SERVICE,
                proxies={
                    "http": f"{proto}://{proxy}",
                    "https": f"{proto}://{proxy}",
                },
                timeout=self.TIMEOUT,
            ).text.strip()
        except Exception:
            return
        if self.is_ipv4(exit_node):
            self.proxies[proto][proxy] = exit_node

    def get_all_sources(self) -> None:
        """Get proxies from sources."""
        logger.info("Getting sources")
        threads = [
            Thread(target=self.get_source, args=(source, proto), daemon=True)
            for proto, sources in self.SOURCES.items()
            for source in sources
        ]
        self.start_threads(threads)

    def check_all_proxies(self) -> None:
        for proto, proxies in self.proxies.items():
            logger.info(f"Checking {len(proxies)} {proto} proxies")
        threads = [
            Thread(target=self.check_proxy, args=(proxy, proto), daemon=True)
            for proto, proxies in self.proxies.items()
            for proxy in proxies
        ]
        self.start_threads(threads)

    @staticmethod
    def _get_sorting_key(x: Tuple[str, Any]) -> Tuple[int, ...]:
        octets = x[0].replace(":", ".").split(".")
        return tuple(map(int, octets))

    def sort_proxies(self) -> None:
        """Delete invalid proxies and sort working ones."""
        prox = [
            (
                proto,
                [
                    (proxy, exit_node)
                    for proxy, exit_node in proxies.items()
                    if exit_node
                ],
            )
            for proto, proxies in self.proxies.items()
        ]
        self.proxies = {
            proto: dict(sorted(proxies, key=self._get_sorting_key))
            for proto, proxies in prox
        }

    def save_proxies(self) -> None:
        """Delete old proxies and save new ones."""
        self.sort_proxies()
        directories_to_delete = (
            "proxies",
            "proxies_anonymous",
            "proxies_geolocation",
            "proxies_geolocation_anonymous",
        )
        for directory in directories_to_delete:
            try:
                rmtree(directory)
            except FileNotFoundError:
                pass
        directories_to_create = (
            directories_to_delete
            if self.MMDB
            else ("proxies", "proxies_anonymous")
        )
        for directory in directories_to_create:
            mkdir(directory)

        # proxies and proxies_anonymous folders
        for proto, proxies in self.proxies.items():
            path = f"proxies/{proto}.txt"
            path_anonymous = f"proxies/proxies_anonymous/{proto}.txt"
            for proxy, exit_node in proxies.items():
                self.append_to_file(path, proxy)
                if exit_node != proxy.split(":")[0]:
                    self.append_to_file(path_anonymous, proxy)

        # proxies_geolocation and proxies_geolocation_anonymous folders
        if self.MMDB:
            with open_database(self.MMDB) as reader:
                for proto, proxies in self.proxies.items():
                    path = f"proxy/proxies_geolocation/{proto}.txt"
                    path_anonymous = (
                        f"proxies/proxies_geolocation_anonymous/{proto}.txt"
                    )
                    for proxy, exit_node in proxies.items():
                        # type: ignore
                        line = proxy + self.get_geolocation(exit_node, reader)
                        self.append_to_file(path, line)
                        if exit_node != proxy.split(":")[0]:
                            self.append_to_file(path_anonymous, line)

    def main(self) -> None:
        self.get_all_sources()
        self.check_all_proxies()
        self.save_proxies()
        logger.success("Result:")
        for proto, proxies in self.proxies.items():
            logger.success(f"{proto} - {len(proxies)}")
            return proxies


def main() -> None:
    logger.remove()
    logger.add(
        stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>",
        colorize=True,
    )
    proxyscraper = ProxyScraperChecker(
        timeout=config.TIMEOUT,
        geolite2_city_mmdb="GeoLite2-City.mmdb"
        if config.GEOLOCATION
        else None,
        ip_service=config.IP_SERVICE,
        http_sources=config.HTTP_SOURCES if config.HTTP else None,
        socks4_sources=config.SOCKS4_SOURCES if config.SOCKS4 else None,
        socks5_sources=config.SOCKS5_SOURCES if config.SOCKS5 else None,
    )
    proxies = proxyscraper.main()
    logger.success("Thank you for using proxy-scraper-checker :)")
    return proxies
