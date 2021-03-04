from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import validators
import requests
class PyAmazon(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()
 
    def get_url(self, url: str):
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        link = "https://www.amazon.com"
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

    def createWidgets(self):
        self.label_url = Label(self, font=("Arial", 12), bg="orange", fg="black", text="Place URL for an amazon product: ", borderwidth=0, justify=LEFT)
        self.label_url.grid(row=0, column=0)
        self.entry_url = Text(self, font=("Arial", 12), borderwidth=0)
        self.entry_url.grid(row=0, column=1)
        self.button_get_url = Button(self, text="Search for product", command=lambda: self.get_url(str(self.entry_url)))
        self.button_get_url.grid(row=0, column=2)
        self.label_price = Label(self, font=("Arial", 12), text=self.button_get_url, borderwidth=0, justify=LEFT)
        self.label_price.grid(row=1, column=2)
Calculator = Tk()
Calculator.title("AdictoCalculator")
Calculator.resizable(True, True)
Calculator.config(cursor="pencil")
root = PyAmazon(Calculator).grid()
Calculator.mainloop()