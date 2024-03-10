# region imports
from bs4 import BeautifulSoup
import requests
# endregion

# region request
eur_try = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

request_eur = requests.get(eur_try)
# endregion

# region result
if not (request_eur is None):
    soup_eur = BeautifulSoup(request_eur.content, "html.parser")

    if not (soup_eur is None):
        tl = soup_eur.find("div", {"class": "YMlKec fxKbKc"})

        if not (tl is None):
            getTextTry = tl.getText()

            if not (getTextTry is None):
                getTextTry = float(getTextTry.replace(',', '.'))
# endregion