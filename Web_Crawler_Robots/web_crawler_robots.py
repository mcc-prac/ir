import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

start_url = input("Enter starting URL: ")
max_pages = int(input("Enter number of pages: "))
delay = float(input("Enter crawling delay (seconds): "))

domain = urlparse(start_url).netloc

robots = RobotFileParser()
robots.set_url(urljoin(start_url, "/robots.txt"))

try:
    robots.read()
except Exception:
    print("Could not read robots.txt")

queue = [start_url]
visited = set()

while queue and len(visited) < max_pages:
    url = queue.pop(0)

    if url in visited:
        continue

    if not robots.can_fetch("*", url):
        print("Blocked by robots.txt:", url)
        continue

    try:
        time.sleep(delay)

        response = requests.get(
            url,
            headers={"User-Agent": "Educational-Web-Crawler"},
            timeout=10
        )

        if response.status_code != 200:
            print("Failed:", url, response.status_code)
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        visited.add(url)

        print("\nPage", len(visited))
        print("URL:", url)
        print(
            "Title:",
            soup.title.text.strip()
            if soup.title
            else "No Title"
        )

        for link in soup.find_all("a", href=True):
            new_url = urljoin(url, link["href"])
            new_domain = urlparse(new_url).netloc

            if (
                new_domain == domain
                and new_url not in visited
                and new_url not in queue
            ):
                queue.append(new_url)

    except requests.RequestException as e:
        print("Error:", e)

print("\nCrawling completed.")
print("Total pages crawled:", len(visited))

# Sample input:
# https://example.com
# 1
# 0
