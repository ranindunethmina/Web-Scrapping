import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    headings = []
    content = []

    for heading in soup.find_all('h2'):
        heading_text = heading.text.strip()

        next_paragraph = heading.find_next('p')

        headings.append(heading_text)
        if next_paragraph:
            content.append(next_paragraph.text.strip())
        else:
            content.append("")

    df = pd.DataFrame({'Heading': headings, 'Content': content})

    df.to_excel("scramp.xlsx", sheet_name="Headings and Content", index=False)

    print("Data writed")

else:
    print('Error')