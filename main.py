import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def sanitize_filename(url):
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    return name if name else f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

def is_duplicate(filepath, content):
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'rb') as f:
        return f.read() == content

def fetch_image(url, dest_dir):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"Skipped (not an image): {url}")
            return

        filename = sanitize_filename(url)
        filepath = os.path.join(dest_dir, filename)

        if is_duplicate(filepath, response.content):
            print(f"Duplicate skipped: {filename}")
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter image URLs (comma-separated): ").split(',')

    dest_dir = "Fetched_Images"
    os.makedirs(dest_dir, exist_ok=True)

    for url in map(str.strip, urls):
        if url:
            fetch_image(url, dest_dir)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()