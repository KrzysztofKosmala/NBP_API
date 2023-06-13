import matplotlib.pyplot as plt
import matplotlib.dates as mdates
class DataVisualizer:
    def printDiagrams(listMap):

        for key, value in listMap.items():
            sortedMap = dict(sorted(value.items()))
            dates = list(sortedMap.keys())
            values = list(sortedMap.values())
            currencyCode = key
            plt.figure(figsize=(16, 6))
            plt.plot(dates, values)
            plt.xlabel('Data')
            plt.ylabel('Wartość')
            plt.title(currencyCode)
            ax = plt.gca()
            plt.xticks(rotation=90, fontsize=9)
            plt.show()