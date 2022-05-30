from ImageProcessing import prepareGainerAndLoserImage
from NSE import get52WeekHigh, get52WeekLow, getTopGainers, getTopLosers

gainers = getTopGainers()
losers = getTopLosers()
_52WeekHigh = get52WeekHigh()
_52WeekLow = get52WeekLow()

dailyImage = prepareGainerAndLoserImage(gainers,losers,  "output/dailyImage.jpg")
yearLongImage = prepareGainerAndLoserImage(_52WeekHigh,_52WeekLow, "output/yearImage.jpg")

