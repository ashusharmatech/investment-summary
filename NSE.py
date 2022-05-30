from urllib import response
import requests

from Constants import NSE_52_WEEK_COL, NSE_52_WEEK_HIGH_SORT_DETAILS, NSE_52_WEEK_LOW_SORT_DETAILS, NSE_52_WEEK_RENAME_COL, NSE_API_52_WEEK_HIGH, NSE_API_52_WEEK_LOW, NSE_API_TOP_GAINERS, NSE_API_TOP_LOSER, NSE_COL, NSE_GAINER_SORT_DETAILS, NSE_LOSER_SORT_DETAILS, NSE_RENAME_COL
from DataConversion import convert


def getData(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/88.0.4324.182 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.nseindia.com/get-quotes/equity?symbol=COALINDIA',
    }

    response = requests.get(url=url, headers=headers)
    return response.json()


def getTopGainers():
    response = getData(NSE_API_TOP_GAINERS)
    data = response['data']
    return convert(data, NSE_COL, NSE_RENAME_COL, NSE_GAINER_SORT_DETAILS)
    
def getTopLosers():
    response = getData(NSE_API_TOP_LOSER)
    data = response['data']
    return convert(data, NSE_COL, NSE_RENAME_COL, NSE_LOSER_SORT_DETAILS)

def get52WeekHigh():
    response =  getData(NSE_API_52_WEEK_HIGH)
    data = response['data']
    return convert(data, NSE_52_WEEK_COL, NSE_52_WEEK_RENAME_COL, NSE_52_WEEK_HIGH_SORT_DETAILS)


def get52WeekLow():
    response = getData(NSE_API_52_WEEK_LOW)
    data = response['data']
    return convert(data, NSE_52_WEEK_COL, NSE_52_WEEK_RENAME_COL, NSE_52_WEEK_LOW_SORT_DETAILS)



