"""
1_scraper.py

Question 2 – Web Scraping (A)
Target: http://books.toscrape.com

Collects (>= 100 books; we scrape ~200):
- Book title
- Price (£)
- Star rating (1-5)
- Category
- Availability status

Requirements:
1) requests and BeautifulSoup4
2) Scrape at least 3 pages (we scrape 10 pages for ~200 books)
3) try-except error handling
4) 1–2 second delay between requests
5) Save to CSV
Bonus (+2): Retry logic with 3 attempts

Output:
question2_data_analysis/data/raw_books_data.csv
"""

import csv
import os
import random
import time
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"
CATALOGUE_URL = urljoin(BASE_URL, "catalogue/")
PAGE_URL = urljoin(BASE_URL, "catalogue/page-{}.html")

OUTPUT_CSV = "question2_data_analysis/data/raw_books_data.csv"

HEADERS = {"User-Agent": "Mozilla/5.0"}

TIMEOUT = (5, 20)  # connect timeout, read timeout (prevents hanging)
MAX_RETRIES = 3
PAGES_TO_SCRAPE = 10  # 10 pages ≈ 200 books

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def sleep_polite() -> None:
    """Requirement: 1–2 second delay between requests."""
    time.sleep(random.uniform(1, 2))


def request_with_retry(session: requests.Session, url: str) -> Optional[requests.Response]:
    """Bonus: retry logic (3 attempts)."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, headers=HEADERS, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            print(f"[WARN] Attempt {attempt}/{MAX_RETRIES} failed for {url}: {e}")
            if attempt < MAX_RETRIES:
                sleep_polite()
            else:
                return None
    return None


def extract_category(session: requests.Session, product_url: str) -> str:
    """Extract category from product detail page breadcrumb."""
    resp = request_with_retry(session, product_url)
    sleep_polite()

    if resp is None:
        return "Unknown"

    try:
        # IMPORTANT: use resp.content (bytes) to avoid encoding issues like Â£
        soup = BeautifulSoup(resp.content, "html.parser")
        breadcrumbs = soup.select("ul.breadcrumb li a")
        if len(breadcrumbs) >= 3:
            return breadcrumbs[2].get_text(strip=True)
    except Exception:
        pass

    return "Unknown"


def scrape_books() -> list[dict]:
    books: list[dict] = []

    with requests.Session() as session:
        for page in range(1, PAGES_TO_SCRAPE + 1):
            url = PAGE_URL.format(page)
            print(f"[INFO] Scraping page {page}/{PAGES_TO_SCRAPE} -> {url}")

            resp = request_with_retry(session, url)
            sleep_polite()

            if resp is None:
                print(f"[ERROR] Skipping page {page} (failed after retries).")
                continue

            try:
                # IMPORTANT: use resp.content (bytes) for correct £ encoding
                soup = BeautifulSoup(resp.content, "html.parser")
                products = soup.select("article.product_pod")

                for product in products:
                    try:
                        title = product.select_one("h3 a")["title"].strip()
                        price = product.select_one("p.price_color").get_text(strip=True)
                        availability = product.select_one("p.instock.availability").get_text(" ", strip=True)

                        rating_class = product.select_one("p.star-rating")["class"]
                        rating_word = next((c for c in rating_class if c != "star-rating"), "")
                        rating = RATING_MAP.get(rating_word, 0)

                        rel_link = product.select_one("h3 a")["href"]
                        product_url = urljoin(CATALOGUE_URL, rel_link)

                        category = extract_category(session, product_url)

                        books.append(
                            {
                                "title": title,
                                "price_gbp": price,
                                "rating": rating,
                                "category": category,
                                "availability": availability,
                            }
                        )

                    except Exception as e:
                        # Requirement: try-except error handling
                        print(f"[WARN] Failed parsing a book: {e}")
                        continue

            except Exception as e:
                print(f"[ERROR] Failed parsing page {page}: {e}")

    return books


def save_to_csv(data: list[dict]) -> None:
    if not data:
        print("[ERROR] No data scraped. CSV not created.")
        return

    os.makedirs("question2_data_analysis/data", exist_ok=True)

    # IMPORTANT: utf-8-sig helps Excel show £ correctly (no Â£)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f, fieldnames=["title", "price_gbp", "rating", "category", "availability"]
        )
        writer.writeheader()
        writer.writerows(data)

    print(f"[SUCCESS] Saved {len(data)} books -> {OUTPUT_CSV}")


if __name__ == "__main__":
    scraped_books = scrape_books()
    print(f"[INFO] Total books scraped: {len(scraped_books)}")

    if len(scraped_books) < 100:
        print("[WARNING] Less than 100 books scraped. Increase PAGES_TO_SCRAPE.")

    save_to_csv(scraped_books)