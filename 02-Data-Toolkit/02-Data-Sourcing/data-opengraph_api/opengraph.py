# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    base = 'https://opengraph.lewagon.com'
    params = {'url': url}
    response1 = requests.get(base,params=params)
    response = response1.json()
    vazio = {}
    if response1.status_code == 200:
        return response['data']
    return vazio

# # To manually test, uncomment the following lines and run `python opengraph.py`:
# if __name__ == "__main__":
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fetch_metadata("https://www.github.com"))
