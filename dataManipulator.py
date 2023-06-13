from dataProvider import DataProvider
from datetime import datetime, timedelta

class DataManipulator:

    def addLackingDaysToMap(maps, startDate, endDate, selectedCodes):
        currentDate = startDate
        delta = timedelta(days=1)

        if startDate.weekday()==5 or startDate.weekday()==6:
            lastValidRates = []

            for code in selectedCodes:
                daysBackToFindValidDay = 1
                lastValidRate = DataProvider.fetchRateForCodeByDate(startDate - timedelta(daysBackToFindValidDay), code)

                while lastValidRate.status_code != 200:
                    daysBackToFindValidDay += 1
                    lastValidRate = DataProvider.fetchRateForCodeByDate(startDate - timedelta(daysBackToFindValidDay), code)

                lastValidRates.append(lastValidRate)

            dateToFetchGoldPriceFrom = lastValidRates[0].json()['rates'][0]['effectiveDate']
            goldPrice = DataProvider.fetchGoldPrice(dateToFetchGoldPriceFrom)[0]['cena']
            listToAddOnWeekend = []
            for validRate in lastValidRates:
                valid = validRate.json()
                code = valid['code']
                value = valid['rates'][0]['mid']
                date = valid['rates'][0]['effectiveDate']
                listToAddOnWeekend.append((code, value))

            listToAddOnWeekend.append(("Gold", goldPrice))

            if(startDate.weekday()==5):
                for i in range(0, 2):
                    maps[(startDate + timedelta(i)).strftime('%Y-%m-%d')] = listToAddOnWeekend

            elif startDate.weekday()==6:
                maps[startDate.strftime('%Y-%m-%d')] = listToAddOnWeekend



        while currentDate <= endDate:
            key = currentDate.strftime('%Y-%m-%d')

            if key not in maps:
                previousKey = (currentDate - delta).strftime('%Y-%m-%d')
                maps[key] = maps.get(previousKey)

            currentDate += delta

        return maps



    def createMap(ratesAndGold):
        outputMap = {}
        for elem in ratesAndGold:
            for rate in elem['rates']:
                if rate['effectiveDate'] in outputMap:
                    outputMap[rate['effectiveDate']].append((elem['code'], rate['mid']))
                else:
                    outputMap[rate['effectiveDate']] = [(elem['code'], rate['mid'])]
        return outputMap


        return outputMap

    def transformMap(completedMap, startDate):
        listMap = {}
        rangeValue = len(completedMap[startDate.strftime('%Y-%m-%d')]) - 1
        for i in range(rangeValue):
            newMap = {}
            for key, values in zip(completedMap.keys(), completedMap.values()):
                newMap[key] = (values[len(values) - 1][1] / values[i][1])
            listMap[(values[i][0])] = newMap

        return listMap