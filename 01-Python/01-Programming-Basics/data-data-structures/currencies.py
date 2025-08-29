# pylint: disable=missing-docstring

RATES = {"USDEUR": 0.85, "GBPEUR": 1.13, "CHFEUR": 0.86, 'EURGBP':0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    if amount[1] == "USD":
        return round(amount[0] * RATES['USDEUR'], 0)
    if amount[1] == 'GBP':
        return round(amount[0] * RATES["GBPEUR"],0)
    if amount[1] == 'CHF':
        return round(amount[0] * RATES["CHFEUR"],0)
    if currency == "GBP":
        return round(amount[0] * RATES['EURGBP'],0)
    return None
print(convert((200, "CHF"), "EUR"))
