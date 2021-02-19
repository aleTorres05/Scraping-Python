from bs4 import BeautifulSoup
import requests
import validators


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            
link = "https://www.amazon.com"
def get_price():
    url = input("Place URL for an amazon product: ")

    validate_url = validators.url(url)
    if validate_url:
        if link in url:
            page = requests.get(url, headers=HEADERS)

            soup = BeautifulSoup(page.content, "html.parser")

            span = soup.find("span", attrs={"id":"price_inside_buybox"}).string.strip()
            return span
        else:
            return "URL not valid, Please place an Amazon URL!"
    else:
            return "Not a URL!"

print(get_price())
