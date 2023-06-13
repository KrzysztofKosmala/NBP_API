from UI import UI
from dataManipulator import DataManipulator
from dataProvider import DataProvider
from datetime import datetime, timedelta

from dataVisualizer import DataVisualizer
from utils import Utils

endDate = datetime.now().date()
startDate = datetime.now().date() - timedelta(100)
table = DataProvider.fetchTodaysTable(endDate-timedelta(1)).json()


codes = Utils.fetchCodesFromRates(table)

selectedCodes = UI.selecyCurrencyCodes(codes)

fetchedRates = []

for elem in selectedCodes:
    fetchedRates.append(DataProvider.fetchExchangeRatesFromTableAWithCode(startDate, endDate, elem))

goldPrices = DataProvider.fetchGoldPrices(startDate, endDate)

outputMap = DataManipulator.createMap(fetchedRates)

for elem in goldPrices:
    outputMap[elem['data']].append(("Gold", elem['cena']))

completedMap = DataManipulator.addLackingDaysToMap(outputMap, startDate, endDate, selectedCodes)
listmap = DataManipulator.transformMap(completedMap, startDate)

DataVisualizer.printDiagrams(listmap)

