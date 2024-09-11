import os
import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image

# URL of the webpage
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

# Send a GET request to fetch the page content
response = requests.get(url)

# Ensure the response is successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all 'img' tags
    tags = soup.find_all('img', alt="What is Algorithm?")

    # Create a directory to store the images
    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    # Iterate over the image tags and download them
    for index, tag in enumerate(tags):
        # Get the 'src' attribute (image URL)
        img_url = tag.get('src')

        # Handle relative URLs by combining them with the base URL
        if not img_url.startswith("http"):
            img_url = urllib.parse.urljoin(url, img_url)

        # Define the path to save the image
        img_path = f"downloaded_images/image_{index}.jpg"

        # Download and save the image
        try:
            urllib.request.urlretrieve(img_url, img_path)
            print(f"Downloaded: {img_url}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

print("Image have been downloaded!")
