BASE_IMAGE = "assets/base-white.jpg"

NSE_API_52_WEEK_LOW = "https://www1.nseindia.com/products/dynaContent/equities/equities/json/online52NewLow.json"
NSE_API_52_WEEK_HIGH = "https://www1.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json"
NSE_API_TOP_GAINERS = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
NSE_API_TOP_LOSER = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json"

LIMIT_ROWS = 5

NSE_COL = ['symbol', 'openPrice', 'highPrice', 'lowPrice', 'ltp', 'netPrice']
NSE_RENAME_COL = {"symbol": "Symbol", "openPrice": "Open Price ",
                  "highPrice": "High Price", "lowPrice": "Low Price", "ltp": "Close Price", "netPrice": "Change %"}

NSE_GAINER_SORT_DETAILS = {"column": "netPrice", "order": False}
NSE_LOSER_SORT_DETAILS = {"column": "netPrice", "order": True}

NSE_52_WEEK_COL = ['symbol', 'value', 'ltp', 'pChange']
NSE_52_WEEK_RENAME_COL = {"symbol": "Symbol", "value": "52 Week High ",
                          "ltp": "Last Traded Price", "pChange": "Change %"}

NSE_52_WEEK_HIGH_SORT_DETAILS = {"column": "pChange", "order": False}
NSE_52_WEEK_LOW_SORT_DETAILS = {"column": "pChange", "order": True}

