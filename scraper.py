import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

data = []

page = 1
while page <= 5:
    print("Page:", page)

    if page == 1:
        url = "https://scrapeme.live/shop/"
    else:
        url = f"https://scrapeme.live/shop/page/{page}/"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("li", class_="product")

    for product in products:
        name = product.find("h2").text.strip()
        price = product.find("span", class_="woocommerce-Price-amount").text.strip()
        link = product.find("a")["href"]

        data.append([name, price, link])

    page += 1

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Link"])
    writer.writerows(data)

print(f"Done! {len(data)} products saved to products.csv")