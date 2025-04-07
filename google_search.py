from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)

def google_search_companies(keywords, area, max_results=10):
    driver = init_driver()
    query = f"{area} {keywords} 会社"
    url = f"https://www.google.com/search?q={query}"
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = []

    for g in soup.select("div.g"):
        title = g.select_one("h3")
        link = g.select_one("a")
        if title and link:
            results.append({
                "title": title.get_text(),
                "url": link["href"]
            })
        if len(results) >= max_results:
            break

    driver.quit()
    return results

