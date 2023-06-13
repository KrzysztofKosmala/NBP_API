
class Utils:

    def fetchCodesFromRates(data):
        if len(data) > 0:
            first_element = data[0]
            rates = first_element["rates"]
            codes = [rate["code"] for rate in rates]
            return codes
        else:
            return []

