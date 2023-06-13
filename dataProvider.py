import requests
from datetime import datetime, timedelta

class DataProvider:
    maxDayRange = 93
    suffixUrl = "/?format=json"
    exchangeRatesUrlPrefix = 'http://api.nbp.pl/api/exchangerates/tables/a/'
    ratesUrlPrefix = 'http://api.nbp.pl/api/exchangerates/rates/a/'
    goldPricesUrlPrefix = 'http://api.nbp.pl/api/cenyzlota/'
    tableAUrl = 'http://api.nbp.pl/api/exchangerates/tables/a/'




    def fetchExchangeRatesFromLastDays(howManyDays):
        mergedResponse = []
        endDate = datetime.now().date()
        startDate = datetime.now().date() - timedelta(days=howManyDays)

        while (endDate - startDate).days > DataProvider.maxDayRange:
            mergedResponse.extend(DataProvider.fetchExchangeRatesFromTableA(startDate, startDate + timedelta(days=DataProvider.maxDayRange)))
            startDate = startDate + timedelta(days=DataProvider.maxDayRange)

        mergedResponse.extend(DataProvider.fetchExchangeRatesFromTableA(startDate, endDate))

        return mergedResponse

    def fetchExchangeRatesFromTableAWithCode(startDate, endDate, code):

        url = DataProvider.ratesUrlPrefix + str(code) + "/" + str(startDate) + "/" + str(endDate) + DataProvider.suffixUrl
        response = requests.get(url
            )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Błąd podczas pobierania danych. Kod odpowiedzi: " + str(response.status_code))

    def fetchExchangeRatesFromTableA(startDate, endDate):

        response = requests.get(DataProvider.exchangeRatesUrlPrefix + "/" + str(startDate) + "/" + str(endDate) + DataProvider.suffixUrl)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Błąd podczas pobierania danych. Kod odpowiedzi: " + str(response.status_code))


    def fetchTodaysTable(today):
        url = DataProvider.tableAUrl  + str(today) + DataProvider.suffixUrl
        response = requests.get(url)
        return response

    def fetchRateForCodeByDate(day, code):
        url = DataProvider.ratesUrlPrefix+ code + "/" + str(day) + DataProvider.suffixUrl
        response = requests.get(url)
        return response

    def fetchGoldPrices(startDate, endDate):

        response = requests.get(DataProvider.goldPricesUrlPrefix + str(startDate) + "/" + str(endDate) + DataProvider.suffixUrl)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Błąd podczas pobierania danych. Kod odpowiedzi: " + str(response.status_code))

    def fetchGoldPrice(date):

        response = requests.get(DataProvider.goldPricesUrlPrefix + str(date) )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Błąd podczas pobierania danych. Kod odpowiedzi: " + str(response.status_code))
