import os
import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    tags = soup.find_all('img', alt="What is Algorithm?")

    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    for index, tag in enumerate(tags):
        img_url = tag.get('src')

        if not img_url.startswith("http"):
            img_url = urllib.parse.urljoin(url, img_url)

        img_path = f"downloaded_images/image_{index}.jpg"

        try:
            urllib.request.urlretrieve(img_url, img_path)
            print(f"Downloaded: {img_url}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

print("Image have been downloaded!")