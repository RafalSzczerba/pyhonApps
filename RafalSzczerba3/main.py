import SalariesReader
if __name__ == '__main__':
    fileName = "salaries"
    sal = SalariesReader.Salaries(fileName)
    sal.readAndPresentValue()
