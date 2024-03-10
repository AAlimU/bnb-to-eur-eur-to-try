# region imports
from eur_try import getTextTry
from bnb_eur import getTextBnb
# endregion

# region result
result = float(getTextTry * getTextBnb)

if not (result is None):
    # currency format
    resultTry = "{:0,.2f}".format(float(result))

    if not (resultTry is None):
        print('BNB şu anda: ' + resultTry + ' TL')
# endregion