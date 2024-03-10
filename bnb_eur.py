# region imports
from bs4 import BeautifulSoup
import requests
# endregion

# region request
bnb_eur = "https://www.google.com/finance/quote/BNB-EUR?hl=tr"

request_bnb = requests.get(bnb_eur)
# endregion

# region result
if not (request_bnb is None):
    soup_bnb = BeautifulSoup(request_bnb.content, "html.parser")

    if not (soup_bnb is None):
        bnb = soup_bnb.find("div", {"class": "YMlKec fxKbKc"})

        if not (bnb is None):
            getTextBnb = bnb.getText()

            if not (getTextBnb is None):
                getTextBnb = float(getTextBnb.replace(',', '.'))
# endregion