from bs4 import BeautifulSoup
import requests
import validators

url = input("Please enter url of your product: ")

validate_url = validators.url(url)

if validate_url:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find_all("div", class_="a-box-inner")
    print(price)
else:
    print("URL no valida!")