import calendar
import json

class Salaries:
    def __init__(self, fileName):
        self.fileName = fileName
        self.totalMoney = 0

    def readAndPresentValue(self):
        try:
            with open(f"{self.fileName}.json", 'r') as f:
                salaries = json.load(f)
                if (len(salaries)) > 0:
                    printValue = salaries[0]["Name"]
                    print(f"{printValue} received following salaries in this year:")
                    for k in salaries:
                        print(str(calendar.month_abbr[k["Month"]] + ": "+str(k["GrossSalary"])+" PLN"))
                        self.totalMoney += k["GrossSalary"]
                print(f"In total: {self.totalMoney} PLN Gross")
        except FileNotFoundError:
                print("File has not been found")







